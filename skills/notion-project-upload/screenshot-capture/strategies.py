"""
Capture Strategies
==================
프로젝트 유형/기술 스택/JD 키워드를 분석하여
포트폴리오에 최적화된 캡처 전략을 결정한다.

핵심 원칙: "면접관이 10초 안에 파악하고 싶은 것"
"""

import os
import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional


# ─────────────────────────────────────────────
# 데이터 모델
# ─────────────────────────────────────────────

class CaptureMethod(Enum):
    FULL_PAGE = "full_page"       # 전체 페이지 스크롤 캡처
    VIEWPORT = "viewport"         # 현재 뷰포트만 캡처
    ELEMENT = "element"           # 특정 CSS 셀렉터 요소 캡처
    TERMINAL = "terminal"         # 터미널 출력 → 이미지
    BEFORE_AFTER = "before_after" # 인터랙션 전/후 비교


class CaptureType(Enum):
    MAIN = "main"           # 메인 화면 (전체 너비 배치)
    KEY_INSIGHT = "insight"  # 핵심 인사이트/차트
    DETAIL = "detail"        # 상세 화면 (2열 배치 가능)
    TERMINAL = "terminal"    # 터미널 실행 결과
    COMPARISON = "comparison" # Before/After 비교


class Priority(Enum):
    REQUIRED = 1   # 필수 캡처
    RECOMMENDED = 2  # 권장 캡처
    OPTIONAL = 3   # 선택 캡처


@dataclass
class CaptureItem:
    """개별 캡처 항목"""
    name: str                     # 캡처 식별자 (예: "main_dashboard")
    description: str              # 설명 (예: "대시보드 메인 화면")
    method: CaptureMethod
    capture_type: CaptureType
    priority: Priority
    portfolio_value: str          # 포트폴리오 가치 설명
    caption_template: str         # 캡션 템플릿 ({project_name} 등 변수 사용)
    url: Optional[str] = None     # 웹앱 URL
    selector: Optional[str] = None  # CSS 셀렉터 (element 캡처 시)
    command: Optional[str] = None   # 터미널 명령 (terminal 캡처 시)
    wait_seconds: int = 3         # 캡처 전 대기 시간
    viewport: tuple = (1280, 720)


@dataclass
class CaptureStrategy:
    """프로젝트에 대한 전체 캡처 전략"""
    project_type: str
    items: list[CaptureItem] = field(default_factory=list)
    max_captures: int = 4
    cover_from: Optional[str] = None  # 커버로 사용할 캡처 name


# ─────────────────────────────────────────────
# 프레임워크 감지
# ─────────────────────────────────────────────

FRAMEWORK_SIGNATURES = {
    "streamlit": {
        "file_patterns": ["app.py", "main.py", "dashboard.py", "streamlit_app.py"],
        "code_patterns": [r"import\s+streamlit", r"st\.", r"streamlit"],
        "requirements_patterns": ["streamlit"],
        "port": 8501,
        "launch_cmd": "streamlit run {file} --server.headless true --server.port {port}",
        "wait_seconds": 5,
    },
    "react": {
        "file_patterns": ["package.json"],
        "code_patterns": [r'"react"', r'"next"', r'"vite"'],
        "requirements_patterns": [],
        "port": 3000,
        "launch_cmd": "npm start",
        "wait_seconds": 10,
    },
    "flask": {
        "file_patterns": ["app.py", "main.py", "server.py"],
        "code_patterns": [r"from\s+flask", r"import\s+flask", r"Flask\("],
        "requirements_patterns": ["flask"],
        "port": 5000,
        "launch_cmd": "python {file}",
        "wait_seconds": 3,
    },
    "gradio": {
        "file_patterns": ["app.py", "main.py", "demo.py"],
        "code_patterns": [r"import\s+gradio", r"gr\."],
        "requirements_patterns": ["gradio"],
        "port": 7860,
        "launch_cmd": "python {file}",
        "wait_seconds": 5,
    },
    "dash": {
        "file_patterns": ["app.py", "main.py", "dashboard.py"],
        "code_patterns": [r"import\s+dash", r"from\s+dash"],
        "requirements_patterns": ["dash"],
        "port": 8050,
        "launch_cmd": "python {file}",
        "wait_seconds": 5,
    },
}


def detect_framework(project_path: str) -> Optional[dict]:
    """
    프로젝트 디렉토리를 스캔하여 웹 프레임워크를 감지.

    Returns:
        {
            "framework": "streamlit",
            "entry_file": "/path/to/app.py",
            "port": 8501,
            "launch_cmd": "streamlit run app.py ...",
            "wait_seconds": 5,
        }
        또는 None (감지 실패)
    """
    project = Path(project_path)

    # requirements.txt / pyproject.toml 확인
    req_content = ""
    for req_file in ["requirements.txt", "pyproject.toml", "Pipfile"]:
        req_path = project / req_file
        if req_path.exists():
            req_content = req_path.read_text(errors="ignore")
            break

    # package.json 확인
    pkg_content = ""
    pkg_path = project / "package.json"
    if pkg_path.exists():
        pkg_content = pkg_path.read_text(errors="ignore")

    for fw_name, fw_config in FRAMEWORK_SIGNATURES.items():
        # requirements 파일에서 확인
        if fw_config["requirements_patterns"]:
            if any(pat in req_content.lower() for pat in fw_config["requirements_patterns"]):
                entry_file = _find_entry_file(project, fw_config, fw_name)
                if entry_file:
                    return _build_framework_result(fw_name, fw_config, entry_file)

        # package.json에서 확인 (JS 프레임워크)
        if fw_name == "react" and pkg_content:
            if any(re.search(pat, pkg_content) for pat in fw_config["code_patterns"]):
                return _build_framework_result(fw_name, fw_config, str(pkg_path))

        # 소스 파일에서 직접 확인
        for filename in fw_config["file_patterns"]:
            filepath = project / filename
            if filepath.exists():
                content = filepath.read_text(errors="ignore")
                if any(re.search(pat, content) for pat in fw_config["code_patterns"]):
                    return _build_framework_result(fw_name, fw_config, str(filepath))

    return None


def _find_entry_file(project: Path, fw_config: dict, fw_name: str) -> Optional[str]:
    """프레임워크의 엔트리 파일을 탐색"""
    for filename in fw_config["file_patterns"]:
        filepath = project / filename
        if filepath.exists():
            content = filepath.read_text(errors="ignore")
            if any(re.search(pat, content) for pat in fw_config["code_patterns"]):
                return str(filepath)
    return None


def _build_framework_result(fw_name: str, fw_config: dict, entry_file: str) -> dict:
    return {
        "framework": fw_name,
        "entry_file": entry_file,
        "port": fw_config["port"],
        "launch_cmd": fw_config["launch_cmd"].format(
            file=entry_file, port=fw_config["port"]
        ),
        "wait_seconds": fw_config["wait_seconds"],
    }


# ─────────────────────────────────────────────
# 유형별 캡처 전략 템플릿
# ─────────────────────────────────────────────

def get_dashboard_strategy(project_name: str, has_quantitative_impact: bool) -> CaptureStrategy:
    """대시보드/시각화 프로젝트 캡처 전략"""
    strategy = CaptureStrategy(project_type="dashboard", cover_from="main_dashboard")

    strategy.items = [
        CaptureItem(
            name="main_dashboard",
            description="대시보드 메인 화면 전체",
            method=CaptureMethod.VIEWPORT,
            capture_type=CaptureType.MAIN,
            priority=Priority.REQUIRED,
            portfolio_value="면접관이 결과물을 한눈에 파악",
            caption_template=f"{project_name} — 메인 대시보드",
        ),
        CaptureItem(
            name="key_chart",
            description="가장 임팩트 있는 차트/지표",
            method=CaptureMethod.ELEMENT,
            capture_type=CaptureType.KEY_INSIGHT,
            priority=Priority.REQUIRED,
            portfolio_value="데이터 시각화 역량 + 핵심 인사이트 전달",
            caption_template=f"{project_name} — 핵심 분석 차트",
            selector="[class*='chart'], [class*='plot'], canvas, svg.main-chart, .plotly",
        ),
    ]

    if has_quantitative_impact:
        strategy.items.append(
            CaptureItem(
                name="impact_metrics",
                description="정량적 성과 지표 영역",
                method=CaptureMethod.ELEMENT,
                capture_type=CaptureType.KEY_INSIGHT,
                priority=Priority.REQUIRED,
                portfolio_value="비즈니스 임팩트를 수치로 증명",
                caption_template=f"{project_name} — 핵심 성과 지표",
                selector="[class*='metric'], [class*='kpi'], [class*='summary'], [class*='stat']",
            )
        )

    return strategy


def get_automation_strategy(project_name: str, has_quantitative_impact: bool) -> CaptureStrategy:
    """자동화 프로젝트 캡처 전략"""
    strategy = CaptureStrategy(project_type="automation", cover_from="execution_result")

    strategy.items = [
        CaptureItem(
            name="execution_result",
            description="자동화 실행 성공 로그",
            method=CaptureMethod.TERMINAL,
            capture_type=CaptureType.MAIN,
            priority=Priority.REQUIRED,
            portfolio_value="실제 동작하는 코드임을 증명",
            caption_template=f"{project_name} — 자동화 실행 결과",
        ),
    ]

    if has_quantitative_impact:
        strategy.items.append(
            CaptureItem(
                name="before_after",
                description="자동화 전/후 효과 비교",
                method=CaptureMethod.TERMINAL,
                capture_type=CaptureType.COMPARISON,
                priority=Priority.REQUIRED,
                portfolio_value="자동화 효과를 시각적으로 증명",
                caption_template=f"{project_name} — 개선 효과 (Before/After)",
            )
        )

    strategy.items.append(
        CaptureItem(
            name="output_sample",
            description="자동화 결과물 샘플 (생성된 리포트/데이터)",
            method=CaptureMethod.TERMINAL,
            capture_type=CaptureType.DETAIL,
            priority=Priority.RECOMMENDED,
            portfolio_value="결과물의 품질과 실용성 증명",
            caption_template=f"{project_name} — 자동 생성 결과물",
        )
    )

    return strategy


def get_data_analysis_strategy(project_name: str, has_quantitative_impact: bool) -> CaptureStrategy:
    """데이터 분석/EDA 프로젝트 캡처 전략"""
    strategy = CaptureStrategy(project_type="data_analysis", cover_from="key_finding")

    strategy.items = [
        CaptureItem(
            name="key_finding",
            description="핵심 발견 차트 (EDA 결과)",
            method=CaptureMethod.VIEWPORT,
            capture_type=CaptureType.MAIN,
            priority=Priority.REQUIRED,
            portfolio_value="인사이트 도출 능력 증명",
            caption_template=f"{project_name} — 핵심 분석 결과",
        ),
        CaptureItem(
            name="analysis_output",
            description="분석 실행 결과 (통계 요약/테이블)",
            method=CaptureMethod.TERMINAL,
            capture_type=CaptureType.KEY_INSIGHT,
            priority=Priority.REQUIRED,
            portfolio_value="정량적 분석 결과 증명",
            caption_template=f"{project_name} — 분석 결과 요약",
        ),
    ]

    strategy.items.append(
        CaptureItem(
            name="process_log",
            description="데이터 처리 파이프라인 실행",
            method=CaptureMethod.TERMINAL,
            capture_type=CaptureType.TERMINAL,
            priority=Priority.RECOMMENDED,
            portfolio_value="기술적 깊이 증명",
            caption_template=f"{project_name} — 데이터 처리 파이프라인",
        )
    )

    return strategy


def get_webapp_strategy(project_name: str, has_quantitative_impact: bool) -> CaptureStrategy:
    """웹앱 프로젝트 캡처 전략"""
    strategy = CaptureStrategy(project_type="webapp", cover_from="hero_screen")

    strategy.items = [
        CaptureItem(
            name="hero_screen",
            description="메인 UI 화면",
            method=CaptureMethod.VIEWPORT,
            capture_type=CaptureType.MAIN,
            priority=Priority.REQUIRED,
            portfolio_value="완성도 있는 결과물 첫인상",
            caption_template=f"{project_name} — 메인 화면",
        ),
        CaptureItem(
            name="core_feature",
            description="핵심 기능 동작 화면",
            method=CaptureMethod.VIEWPORT,
            capture_type=CaptureType.KEY_INSIGHT,
            priority=Priority.REQUIRED,
            portfolio_value="기능 구현 역량 증명",
            caption_template=f"{project_name} — 핵심 기능",
        ),
    ]

    return strategy


def get_ml_strategy(project_name: str, has_quantitative_impact: bool) -> CaptureStrategy:
    """ML/AI 프로젝트 캡처 전략"""
    strategy = CaptureStrategy(project_type="ml_ai", cover_from="model_metrics")

    strategy.items = [
        CaptureItem(
            name="model_metrics",
            description="모델 성능 지표",
            method=CaptureMethod.TERMINAL,
            capture_type=CaptureType.MAIN,
            priority=Priority.REQUIRED,
            portfolio_value="ML 역량 정량 증명",
            caption_template=f"{project_name} — 모델 성능 평가",
        ),
        CaptureItem(
            name="prediction_example",
            description="예측/추론 결과 예시",
            method=CaptureMethod.TERMINAL,
            capture_type=CaptureType.KEY_INSIGHT,
            priority=Priority.REQUIRED,
            portfolio_value="실제 동작하는 모델 증명",
            caption_template=f"{project_name} — 예측 결과 예시",
        ),
    ]

    return strategy


# ─────────────────────────────────────────────
# 전략 팩토리
# ─────────────────────────────────────────────

# 프로젝트 유형 키워드 → 전략 매핑
TYPE_KEYWORDS = {
    "dashboard": {
        "keywords": ["dashboard", "대시보드", "looker", "tableau", "시각화", "visualization", "chart", "grafana"],
        "strategy_fn": get_dashboard_strategy,
    },
    "automation": {
        "keywords": ["자동화", "automation", "bot", "scraper", "cron", "scheduler", "pipeline", "etl", "workflow"],
        "strategy_fn": get_automation_strategy,
    },
    "data_analysis": {
        "keywords": ["분석", "analysis", "eda", "탐색", "exploratory", "sql", "bigquery", "a/b test", "ab test", "통계"],
        "strategy_fn": get_data_analysis_strategy,
    },
    "webapp": {
        "keywords": ["streamlit", "react", "flask", "gradio", "dash", "web app", "웹앱", "frontend", "ui"],
        "strategy_fn": get_webapp_strategy,
    },
    "ml_ai": {
        "keywords": ["ml", "machine learning", "딥러닝", "deep learning", "model", "모델", "prediction",
                      "classification", "regression", "nlp", "rag", "langchain", "embedding", "fine-tuning"],
        "strategy_fn": get_ml_strategy,
    },
}

# JD 키워드 → 추가 캡처 우선순위 조정
JD_PRIORITY_BOOST = {
    "대시보드": ["main_dashboard", "key_chart"],
    "dashboard": ["main_dashboard", "key_chart"],
    "시각화": ["key_chart", "key_finding"],
    "visualization": ["key_chart", "key_finding"],
    "자동화": ["execution_result", "before_after"],
    "automation": ["execution_result", "before_after"],
    "비용 절감": ["before_after", "impact_metrics"],
    "cost optimization": ["before_after", "impact_metrics"],
    "cost reduction": ["before_after", "impact_metrics"],
    "SQL": ["analysis_output", "key_finding"],
    "A/B test": ["analysis_output", "impact_metrics"],
    "ab test": ["analysis_output", "impact_metrics"],
    "ETL": ["execution_result", "process_log"],
    "ML": ["model_metrics", "prediction_example"],
    "API": ["core_feature", "execution_result"],
}


def determine_capture_strategy(
    project_name: str,
    project_description: str = "",
    tech_stack: list[str] = None,
    impact: str = "",
    project_type: str = "",
    jd_keywords: list[str] = None,
) -> CaptureStrategy:
    """
    프로젝트 정보를 종합 분석하여 최적의 캡처 전략을 결정.

    Args:
        project_name: 프로젝트 이름
        project_description: 프로젝트 설명 (README, Problem/Solution 등)
        tech_stack: 기술 스택 리스트
        impact: Impact 설명 텍스트
        project_type: 기존 분석된 프로젝트 유형 ("Business", "Exploratory", "Learning")
        jd_keywords: JD에서 추출된 키워드 리스트

    Returns:
        CaptureStrategy: 캡처 계획
    """
    tech_stack = tech_stack or []
    jd_keywords = jd_keywords or []

    # 정량적 임팩트 여부 판별
    has_quant_impact = _has_quantitative_impact(impact)

    # 프로젝트 유형 감지 (키워드 매칭)
    all_text = " ".join([
        project_description,
        " ".join(tech_stack),
        impact,
        project_type,
    ]).lower()

    detected_type = _detect_project_capture_type(all_text)

    # 전략 생성
    strategy_fn = TYPE_KEYWORDS.get(detected_type, {}).get(
        "strategy_fn", get_data_analysis_strategy
    )
    strategy = strategy_fn(project_name, has_quant_impact)

    # JD 키워드로 우선순위 조정
    if jd_keywords:
        strategy = _apply_jd_priorities(strategy, jd_keywords)

    # 최대 캡처 수 제한 (유형별)
    type_limits = {
        "Business": 4,
        "Exploratory": 3,
        "Learning": 2,
    }
    strategy.max_captures = type_limits.get(project_type, 3)

    # 우선순위 순 정렬 후 제한
    strategy.items = sorted(strategy.items, key=lambda x: x.priority.value)
    strategy.items = strategy.items[:strategy.max_captures]

    return strategy


def _detect_project_capture_type(text: str) -> str:
    """텍스트에서 프로젝트 캡처 유형을 감지"""
    scores = {}
    for type_name, config in TYPE_KEYWORDS.items():
        score = sum(1 for kw in config["keywords"] if kw.lower() in text)
        if score > 0:
            scores[type_name] = score

    if not scores:
        return "data_analysis"  # 기본값

    return max(scores, key=scores.get)


def _has_quantitative_impact(impact: str) -> bool:
    """Impact 텍스트에 정량적 수치가 포함되어 있는지 판별"""
    if not impact:
        return False

    patterns = [
        r"\d+%",                # 퍼센트
        r"\$[\d,]+",            # 달러
        r"₩[\d,]+",            # 원화
        r"\d+[배x]",            # 배수
        r"\d+시간",             # 시간
        r"\d+분",               # 분
        r"\d+건",               # 건수
        r"[\d.]+[KkMm]",       # K/M 단위
        r"\d+\s*(hours?|mins?|seconds?)",  # 영어 시간
    ]

    return any(re.search(pat, impact) for pat in patterns)


def _apply_jd_priorities(strategy: CaptureStrategy, jd_keywords: list[str]) -> CaptureStrategy:
    """JD 키워드에 매칭되는 캡처 항목의 우선순위를 올림"""
    boosted_names = set()
    for kw in jd_keywords:
        kw_lower = kw.lower()
        for jd_key, boost_targets in JD_PRIORITY_BOOST.items():
            if jd_key.lower() in kw_lower or kw_lower in jd_key.lower():
                boosted_names.update(boost_targets)

    for item in strategy.items:
        if item.name in boosted_names:
            item.priority = Priority.REQUIRED

    return strategy


def format_capture_plan_preview(strategy: CaptureStrategy) -> str:
    """캡처 계획을 사용자 프리뷰용 텍스트로 포맷"""
    lines = [f"📸 캡처 계획 ({strategy.project_type})"]
    lines.append("─" * 40)

    for i, item in enumerate(strategy.items, 1):
        priority_icon = {
            Priority.REQUIRED: "🔴",
            Priority.RECOMMENDED: "🟡",
            Priority.OPTIONAL: "⚪",
        }[item.priority]

        method_label = {
            CaptureMethod.FULL_PAGE: "전체 페이지",
            CaptureMethod.VIEWPORT: "뷰포트",
            CaptureMethod.ELEMENT: "요소 캡처",
            CaptureMethod.TERMINAL: "터미널",
            CaptureMethod.BEFORE_AFTER: "전후 비교",
        }[item.method]

        lines.append(f"  {priority_icon} {i}. {item.description}")
        lines.append(f"     방법: {method_label} | 가치: {item.portfolio_value}")

    lines.append("─" * 40)
    required_count = sum(1 for i in strategy.items if i.priority == Priority.REQUIRED)
    lines.append(f"  필수 {required_count}장 / 총 {len(strategy.items)}장")

    return "\n".join(lines)
