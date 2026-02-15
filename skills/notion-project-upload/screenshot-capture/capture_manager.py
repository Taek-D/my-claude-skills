"""
Capture Manager
===============
프로젝트 분석 → 캡처 전략 → 실행 → Notion 업로드를
오케스트레이션하는 메인 모듈.

기존 notion-project-upload 스킬의 업로드 프로세스에 통합되어
Phase 2 (캡처 전략) → Phase 3 (캡처 실행)을 담당한다.

Usage:
    manager = CaptureManager(notion_token="ntn_xxx")

    # 프로젝트 분석 결과를 기반으로 캡처 실행
    result = manager.auto_capture(
        project_path="/path/to/project",
        project_analysis={
            "name": "AWS FinOps Dashboard",
            "type": "Business",
            "tech_stack": ["Python", "BigQuery", "Looker Studio"],
            "impact": "연간 $38K+ 비용 절감 기회 식별",
            "problem": "...",
            "solution": "...",
        },
        page_id="notion-page-id",
    )
"""

import os
import signal
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .strategies import (
    CaptureItem,
    CaptureMethod,
    CaptureStrategy,
    CaptureType,
    detect_framework,
    determine_capture_strategy,
    format_capture_plan_preview,
)
from .terminal_renderer import TerminalRenderer
from .notion_file_upload import NotionFileUploader, NotionUploadError, FileValidationError


SCREENSHOT_DIR = "/tmp/screenshots"


@dataclass
class CaptureResult:
    """개별 캡처 결과"""
    name: str
    path: str
    caption: str
    capture_type: str
    success: bool
    file_upload_id: Optional[str] = None
    error: Optional[str] = None


@dataclass
class CaptureReport:
    """전체 캡처 결과 리포트"""
    strategy: CaptureStrategy
    results: list[CaptureResult]
    total: int = 0
    success_count: int = 0
    failed_count: int = 0

    def __post_init__(self):
        self.total = len(self.results)
        self.success_count = sum(1 for r in self.results if r.success)
        self.failed_count = self.total - self.success_count

    def summary(self) -> str:
        lines = [f"📸 캡처 완료: {self.success_count}/{self.total}장"]
        for r in self.results:
            icon = "✅" if r.success else "❌"
            lines.append(f"  {icon} {r.caption}")
            if r.error:
                lines.append(f"     └ {r.error}")
        return "\n".join(lines)


class CaptureManager:
    """스마트 스크린샷 캡처 오케스트레이터"""

    def __init__(self, notion_token: str):
        self.uploader = NotionFileUploader(notion_token)
        self.renderer = TerminalRenderer()
        self._app_process = None

    # ─────────────────────────────────────────────
    # 메인 API: 자동 캡처
    # ─────────────────────────────────────────────
    def auto_capture(
        self,
        project_path: str,
        project_analysis: dict,
        page_id: str,
        jd_keywords: list[str] = None,
        set_cover: bool = True,
    ) -> CaptureReport:
        """
        프로젝트를 분석하여 자동으로 스크린샷을 캡처하고 Notion에 업로드.

        Args:
            project_path: 프로젝트 루트 디렉토리 경로
            project_analysis: 기존 프로젝트 분석 결과 dict
                - name, type, tech_stack, impact, problem, solution
            page_id: Notion 페이지 ID (이미 생성된 페이지)
            jd_keywords: JD 키워드 (있으면 우선순위 조정)
            set_cover: 메인 스크린샷을 페이지 커버로 설정할지

        Returns:
            CaptureReport: 캡처 결과 리포트
        """
        # 스크린샷 디렉토리 초기화
        self._prepare_screenshot_dir()

        # 1. 캡처 전략 결정
        strategy = determine_capture_strategy(
            project_name=project_analysis.get("name", "Project"),
            project_description=project_analysis.get("problem", "")
                + " " + project_analysis.get("solution", ""),
            tech_stack=project_analysis.get("tech_stack", []),
            impact=project_analysis.get("impact", ""),
            project_type=project_analysis.get("type", ""),
            jd_keywords=jd_keywords,
        )

        # 2. 프리뷰 출력
        print(format_capture_plan_preview(strategy))
        print()

        # 3. 프레임워크 감지 & 앱 실행
        framework = detect_framework(project_path)
        app_url = None
        if framework:
            app_url = self._launch_app(framework, project_path)
            if app_url:
                # 웹앱 캡처 항목에 URL 설정
                for item in strategy.items:
                    if item.method in (CaptureMethod.FULL_PAGE, CaptureMethod.VIEWPORT, CaptureMethod.ELEMENT):
                        item.url = app_url

        # 4. 캡처 실행
        try:
            results = self._execute_captures(strategy, project_path, project_analysis)
        finally:
            # 앱 프로세스 정리
            self._stop_app()

        # 5. Notion 업로드
        uploaded_results = self._upload_to_notion(results, page_id)

        # 6. 페이지 커버 설정
        if set_cover:
            self._set_cover_image(uploaded_results, strategy, page_id)

        report = CaptureReport(strategy=strategy, results=uploaded_results)
        print()
        print(report.summary())

        return report

    # ─────────────────────────────────────────────
    # 수동 이미지 업로드
    # ─────────────────────────────────────────────
    def upload_manual_images(
        self,
        image_paths: list[str],
        page_id: str,
        captions: list[str] = None,
        section_title: str = "Demo",
    ) -> CaptureReport:
        """
        지정된 이미지 파일들을 Notion 페이지에 업로드.

        Args:
            image_paths: 이미지 파일 경로 리스트
            page_id: Notion 페이지 ID
            captions: 각 이미지의 캡션 (없으면 파일명 사용)
            section_title: Notion 섹션 제목

        Returns:
            CaptureReport
        """
        captions = captions or [Path(p).stem for p in image_paths]

        results = []
        for path, caption in zip(image_paths, captions):
            try:
                result = self.uploader.upload_and_attach(path, page_id, caption)
                results.append(CaptureResult(
                    name=Path(path).stem,
                    path=path,
                    caption=caption,
                    capture_type="manual",
                    success=True,
                    file_upload_id=result["file_upload_id"],
                ))
            except (NotionUploadError, FileValidationError) as e:
                results.append(CaptureResult(
                    name=Path(path).stem,
                    path=path,
                    caption=caption,
                    capture_type="manual",
                    success=False,
                    error=str(e),
                ))

        return CaptureReport(
            strategy=CaptureStrategy(project_type="manual"),
            results=results,
        )

    # ─────────────────────────────────────────────
    # 캡처 실행
    # ─────────────────────────────────────────────
    def _execute_captures(
        self,
        strategy: CaptureStrategy,
        project_path: str,
        project_analysis: dict,
    ) -> list[CaptureResult]:
        """전략에 따라 캡처 실행"""
        results = []

        for item in strategy.items:
            print(f"  📷 캡처 중: {item.description}...")

            try:
                if item.method == CaptureMethod.TERMINAL:
                    result = self._capture_terminal(item, project_path, project_analysis)
                elif item.method in (CaptureMethod.VIEWPORT, CaptureMethod.FULL_PAGE):
                    result = self._capture_webpage(item)
                elif item.method == CaptureMethod.ELEMENT:
                    result = self._capture_element(item)
                else:
                    result = CaptureResult(
                        name=item.name,
                        path="",
                        caption=item.caption_template,
                        capture_type=item.capture_type.value,
                        success=False,
                        error=f"미지원 캡처 방식: {item.method}",
                    )

                results.append(result)

            except Exception as e:
                results.append(CaptureResult(
                    name=item.name,
                    path="",
                    caption=item.caption_template,
                    capture_type=item.capture_type.value,
                    success=False,
                    error=str(e),
                ))

        return results

    def _capture_webpage(self, item: CaptureItem) -> CaptureResult:
        """웹페이지 캡처 (viewport 또는 full_page)"""
        if not item.url:
            return CaptureResult(
                name=item.name, path="", caption=item.caption_template,
                capture_type=item.capture_type.value, success=False,
                error="웹앱 URL이 설정되지 않음",
            )

        output_path = os.path.join(SCREENSHOT_DIR, f"{item.name}.png")
        full_page = item.method == CaptureMethod.FULL_PAGE

        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page(viewport_size={
                    "width": item.viewport[0],
                    "height": item.viewport[1],
                })
                page.goto(item.url, wait_until="networkidle", timeout=30000)

                # 추가 대기 (동적 렌더링)
                if item.wait_seconds > 0:
                    page.wait_for_timeout(item.wait_seconds * 1000)

                page.screenshot(path=output_path, full_page=full_page)
                browser.close()

            return CaptureResult(
                name=item.name,
                path=output_path,
                caption=item.caption_template,
                capture_type=item.capture_type.value,
                success=True,
            )

        except Exception as e:
            return CaptureResult(
                name=item.name, path="", caption=item.caption_template,
                capture_type=item.capture_type.value, success=False,
                error=f"웹 캡처 실패: {e}",
            )

    def _capture_element(self, item: CaptureItem) -> CaptureResult:
        """특정 DOM 요소 캡처"""
        if not item.url:
            return CaptureResult(
                name=item.name, path="", caption=item.caption_template,
                capture_type=item.capture_type.value, success=False,
                error="웹앱 URL이 설정되지 않음",
            )

        output_path = os.path.join(SCREENSHOT_DIR, f"{item.name}.png")

        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page(viewport_size={
                    "width": item.viewport[0],
                    "height": item.viewport[1],
                })
                page.goto(item.url, wait_until="networkidle", timeout=30000)

                if item.wait_seconds > 0:
                    page.wait_for_timeout(item.wait_seconds * 1000)

                # 셀렉터 후보들 순서대로 시도
                selectors = [s.strip() for s in (item.selector or "").split(",") if s.strip()]
                element = None

                for selector in selectors:
                    try:
                        el = page.query_selector(selector)
                        if el and el.is_visible():
                            element = el
                            break
                    except Exception:
                        continue

                if element:
                    element.screenshot(path=output_path)
                else:
                    # 요소를 찾지 못하면 viewport 캡처로 폴백
                    page.screenshot(path=output_path, full_page=False)

                browser.close()

            return CaptureResult(
                name=item.name,
                path=output_path,
                caption=item.caption_template,
                capture_type=item.capture_type.value,
                success=True,
            )

        except Exception as e:
            return CaptureResult(
                name=item.name, path="", caption=item.caption_template,
                capture_type=item.capture_type.value, success=False,
                error=f"요소 캡처 실패: {e}",
            )

    def _capture_terminal(
        self,
        item: CaptureItem,
        project_path: str,
        project_analysis: dict,
    ) -> CaptureResult:
        """터미널 출력 캡처"""
        output_path = os.path.join(SCREENSHOT_DIR, f"{item.name}.png")

        if item.command:
            # 명시적 명령이 있으면 실행
            result = self.renderer.render_command(
                command=item.command,
                output_path=output_path,
                title=item.description,
                cwd=project_path,
            )
        else:
            # 명령이 없으면 프로젝트 분석 기반 추론
            command = self._infer_terminal_command(project_path, project_analysis, item)
            if command:
                result = self.renderer.render_command(
                    command=command,
                    output_path=output_path,
                    title=item.description,
                    cwd=project_path,
                )
            else:
                # 명령을 추론할 수 없으면 프로젝트 설명 기반 텍스트 렌더링
                text = self._generate_demo_text(project_analysis, item)
                self.renderer.render(text, output_path, title=item.description)
                result = {"path": output_path}

        return CaptureResult(
            name=item.name,
            path=output_path,
            caption=item.caption_template,
            capture_type=item.capture_type.value,
            success=os.path.exists(output_path),
            error=None if os.path.exists(output_path) else "캡처 파일 생성 실패",
        )

    def _infer_terminal_command(
        self, project_path: str, analysis: dict, item: CaptureItem
    ) -> Optional[str]:
        """프로젝트 구조에서 실행할 명령을 추론"""
        project = Path(project_path)

        # 메인 실행 파일 탐색 우선순위
        entry_candidates = [
            "main.py", "app.py", "run.py", "analyze.py",
            "pipeline.py", "etl.py", "script.py",
        ]

        for candidate in entry_candidates:
            if (project / candidate).exists():
                return f"python {candidate}"

        # Makefile 확인
        if (project / "Makefile").exists():
            return "make run"

        # package.json scripts 확인
        pkg_path = project / "package.json"
        if pkg_path.exists():
            import json
            try:
                pkg = json.loads(pkg_path.read_text())
                if "scripts" in pkg and "start" in pkg["scripts"]:
                    return "npm start"
            except json.JSONDecodeError:
                pass

        return None

    def _generate_demo_text(self, analysis: dict, item: CaptureItem) -> str:
        """실행할 수 없는 경우 분석 결과 기반 데모 텍스트 생성"""
        name = analysis.get("name", "Project")
        impact = analysis.get("impact", "")
        tech = ", ".join(analysis.get("tech_stack", []))

        return f"""$ {name}
─────────────────────────────────
Project: {name}
Stack: {tech}
─────────────────────────────────

{impact if impact else 'Analysis complete.'}

✅ Done"""

    # ─────────────────────────────────────────────
    # 앱 실행/종료
    # ─────────────────────────────────────────────
    def _launch_app(self, framework: dict, project_path: str) -> Optional[str]:
        """웹앱을 백그라운드로 실행하고 URL 반환"""
        print(f"  🚀 {framework['framework']} 앱 실행 중...")

        try:
            self._app_process = subprocess.Popen(
                framework["launch_cmd"],
                shell=True,
                cwd=project_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid,  # 프로세스 그룹으로 관리
            )

            # 앱 로딩 대기
            wait_time = framework.get("wait_seconds", 5)
            print(f"  ⏳ 앱 로딩 대기 ({wait_time}초)...")
            time.sleep(wait_time)

            # 프로세스 살아있는지 확인
            if self._app_process.poll() is not None:
                stderr = self._app_process.stderr.read().decode() if self._app_process.stderr else ""
                print(f"  ⚠️ 앱 실행 실패: {stderr[:200]}")
                return None

            port = framework["port"]
            url = f"http://localhost:{port}"
            print(f"  ✅ 앱 실행 완료: {url}")
            return url

        except Exception as e:
            print(f"  ⚠️ 앱 실행 실패: {e}")
            return None

    def _stop_app(self):
        """실행 중인 앱 프로세스 종료"""
        if self._app_process:
            try:
                os.killpg(os.getpgid(self._app_process.pid), signal.SIGTERM)
                self._app_process.wait(timeout=5)
            except (ProcessLookupError, subprocess.TimeoutExpired, OSError):
                try:
                    os.killpg(os.getpgid(self._app_process.pid), signal.SIGKILL)
                except (ProcessLookupError, OSError):
                    pass
            self._app_process = None

    # ─────────────────────────────────────────────
    # Notion 업로드
    # ─────────────────────────────────────────────
    def _upload_to_notion(
        self, results: list[CaptureResult], page_id: str
    ) -> list[CaptureResult]:
        """성공한 캡처 결과를 Notion에 업로드"""
        uploaded = []

        for result in results:
            if not result.success or not result.path or not os.path.exists(result.path):
                uploaded.append(result)
                continue

            try:
                print(f"  📤 업로드 중: {result.caption}...")
                upload_result = self.uploader.upload_and_attach(
                    result.path, page_id, result.caption
                )
                result.file_upload_id = upload_result["file_upload_id"]
                uploaded.append(result)

            except (NotionUploadError, FileValidationError) as e:
                result.success = False
                result.error = f"업로드 실패: {e}"
                uploaded.append(result)

        return uploaded

    def _set_cover_image(
        self, results: list[CaptureResult], strategy: CaptureStrategy, page_id: str
    ):
        """메인 스크린샷을 페이지 커버로 설정"""
        if not strategy.cover_from:
            return

        cover_result = next(
            (r for r in results if r.name == strategy.cover_from and r.file_upload_id),
            None,
        )

        if not cover_result:
            # cover_from 이름 매칭 실패 시 첫 번째 성공한 결과 사용
            cover_result = next(
                (r for r in results if r.file_upload_id),
                None,
            )

        if cover_result and cover_result.file_upload_id:
            try:
                self.uploader.set_page_cover(page_id, cover_result.file_upload_id)
                print(f"  🖼 페이지 커버 설정: {cover_result.caption}")
            except NotionUploadError as e:
                print(f"  ⚠️ 커버 설정 실패: {e}")

    # ─────────────────────────────────────────────
    # 유틸리티
    # ─────────────────────────────────────────────
    def _prepare_screenshot_dir(self):
        """스크린샷 임시 디렉토리 초기화"""
        Path(SCREENSHOT_DIR).mkdir(parents=True, exist_ok=True)
        # 이전 캡처 정리
        for f in Path(SCREENSHOT_DIR).glob("*.png"):
            f.unlink()
