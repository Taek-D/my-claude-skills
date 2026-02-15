"""
Terminal Renderer
=================
터미널 출력을 깔끔한 이미지로 변환한다.
Catppuccin Mocha 테마 기반 HTML 생성 → Playwright로 캡처.

Usage:
    renderer = TerminalRenderer()
    renderer.render("$ python main.py\n✅ Complete!", "output.png", title="실행 결과")
"""

import html
import os
import re
import subprocess
from pathlib import Path
from typing import Optional


# ─────────────────────────────────────────────
# Catppuccin Mocha 컬러 팔레트
# ─────────────────────────────────────────────
CATPPUCCIN = {
    "base": "#1e1e2e",
    "mantle": "#181825",
    "surface0": "#313244",
    "surface1": "#45475a",
    "text": "#cdd6f4",
    "subtext0": "#a6adc8",
    "subtext1": "#bac2de",
    "red": "#f38ba8",
    "green": "#a6e3a1",
    "yellow": "#f9e2af",
    "blue": "#89b4fa",
    "mauve": "#cba6f7",
    "teal": "#94e2d5",
    "peach": "#fab387",
    "overlay0": "#6c7086",
}


class TerminalRenderer:
    """터미널 출력을 스타일이 적용된 이미지로 렌더링"""

    def __init__(self, theme: str = "catppuccin"):
        self.colors = CATPPUCCIN
        self.font_family = "'JetBrains Mono', 'Fira Code', 'Cascadia Code', 'Consolas', monospace"

    def render(
        self,
        text: str,
        output_path: str,
        title: str = "Terminal",
        max_lines: int = 50,
        width: int = 820,
    ) -> str:
        """
        터미널 텍스트를 이미지로 렌더링.

        Args:
            text: 터미널 출력 텍스트
            output_path: 출력 이미지 경로
            title: 터미널 창 제목
            max_lines: 최대 라인 수 (초과 시 잘림)
            width: 이미지 너비 (px)

        Returns:
            출력 파일 경로
        """
        # 텍스트 전처리
        text = self._truncate_lines(text, max_lines)

        # Pillow로 직접 렌더링
        self._render_with_pillow(text, output_path, title, width)

        return output_path

    def render_command(
        self,
        command: str,
        output_path: str,
        title: str = "Terminal",
        cwd: str = None,
        timeout: int = 60,
        max_lines: int = 50,
    ) -> dict:
        """
        명령을 실행하고 결과를 이미지로 렌더링.

        Args:
            command: 실행할 명령
            output_path: 출력 이미지 경로
            title: 터미널 창 제목
            cwd: 작업 디렉토리
            timeout: 실행 타임아웃 (초)
            max_lines: 최대 라인 수

        Returns:
            {"path": str, "stdout": str, "stderr": str, "returncode": int}
        """
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=cwd,
            )

            output = ""
            if result.stdout:
                output += result.stdout
            if result.stderr:
                if output:
                    output += "\n"
                output += result.stderr

            # 명령어 프롬프트 추가
            display_text = f"$ {command}\n{output}"

            self.render(display_text, output_path, title, max_lines)

            return {
                "path": output_path,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode,
            }

        except subprocess.TimeoutExpired:
            error_text = f"$ {command}\n⏱ Timeout after {timeout}s"
            self.render(error_text, output_path, title)
            return {
                "path": output_path,
                "stdout": "",
                "stderr": f"Timeout after {timeout}s",
                "returncode": -1,
            }

    # ─────────────────────────────────────────────
    # HTML 빌더
    # ─────────────────────────────────────────────
    def _build_html(self, styled_content: str, title: str, width: int) -> str:
        c = self.colors
        return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    background: {c['mantle']};
    padding: 20px;
    display: inline-block;
  }}

  .terminal {{
    background: {c['base']};
    border-radius: 12px;
    width: {width}px;
    overflow: hidden;
    box-shadow:
      0 4px 6px -1px rgba(0,0,0,0.3),
      0 2px 4px -2px rgba(0,0,0,0.2),
      0 0 0 1px {c['surface0']};
  }}

  .terminal-header {{
    background: {c['mantle']};
    padding: 12px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid {c['surface0']};
  }}

  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
  }}
  .dot-red {{ background: {c['red']}; }}
  .dot-green {{ background: {c['green']}; }}
  .dot-yellow {{ background: {c['yellow']}; }}

  .terminal-title {{
    color: {c['overlay0']};
    font-family: {self.font_family};
    font-size: 13px;
    margin-left: 8px;
    flex: 1;
    text-align: center;
  }}

  .terminal-body {{
    padding: 20px 24px;
    font-family: {self.font_family};
    font-size: 14px;
    line-height: 1.7;
    color: {c['text']};
  }}

  .terminal-body pre {{
    margin: 0;
    white-space: pre-wrap;
    word-wrap: break-word;
  }}

  /* Syntax highlighting */
  .prompt {{ color: {c['green']}; font-weight: bold; }}
  .command {{ color: {c['blue']}; font-weight: bold; }}
  .success {{ color: {c['green']}; }}
  .error {{ color: {c['red']}; }}
  .warning {{ color: {c['yellow']}; }}
  .info {{ color: {c['blue']}; }}
  .number {{ color: {c['peach']}; }}
  .path {{ color: {c['mauve']}; }}
  .comment {{ color: {c['overlay0']}; }}
  .highlight {{ color: {c['teal']}; font-weight: bold; }}
</style>
</head>
<body>
  <div class="terminal">
    <div class="terminal-header">
      <span class="dot dot-red"></span>
      <span class="dot dot-green"></span>
      <span class="dot dot-yellow"></span>
      <span class="terminal-title">{html.escape(title)}</span>
    </div>
    <div class="terminal-body">
      <pre>{styled_content}</pre>
    </div>
  </div>
</body>
</html>"""

    # ─────────────────────────────────────────────
    # 구문 강조 (간이)
    # ─────────────────────────────────────────────
    def _apply_syntax_highlighting(self, text: str) -> str:
        """간단한 구문 강조 적용"""
        lines = text.split("\n")
        styled_lines = []

        for line in lines:
            styled = line

            # $ 프롬프트 라인
            if re.match(r"^\$\s", line):
                parts = line.split(" ", 2)
                prompt = f'<span class="prompt">{parts[0]}</span>'
                cmd = f' <span class="command">{" ".join(parts[1:])}</span>' if len(parts) > 1 else ""
                styled = prompt + cmd

            # ✅ ✓ 성공 표시
            elif re.match(r"^[✅✓⭐]", line) or "success" in line.lower() or "complete" in line.lower():
                styled = f'<span class="success">{line}</span>'

            # ❌ ✗ 에러 표시
            elif re.match(r"^[❌✗⛔]", line) or "error" in line.lower() or "fail" in line.lower():
                styled = f'<span class="error">{line}</span>'

            # ⚠ 경고
            elif re.match(r"^[⚠️⚡]", line) or "warning" in line.lower():
                styled = f'<span class="warning">{line}</span>'

            # ℹ 정보
            elif re.match(r"^[ℹ️📊📈📉]", line) or line.startswith("INFO"):
                styled = f'<span class="info">{line}</span>'

            # # 주석
            elif re.match(r"^#", line):
                styled = f'<span class="comment">{line}</span>'

            # ─── 구분선
            elif re.match(r"^[-─═]{3,}", line):
                styled = f'<span class="comment">{line}</span>'

            else:
                # 숫자 강조 (퍼센트, 금액 등)
                styled = re.sub(
                    r"(\$[\d,]+\.?\d*|₩[\d,]+|[\d,]+\.?\d*%|\b\d{1,3}(,\d{3})+\b)",
                    r'<span class="number">\1</span>',
                    styled,
                )
                # 파일 경로 강조
                styled = re.sub(
                    r"((?:/[\w.-]+)+)",
                    r'<span class="path">\1</span>',
                    styled,
                )

            styled_lines.append(styled)

        return "\n".join(styled_lines)

    def _truncate_lines(self, text: str, max_lines: int) -> str:
        """라인 수 제한"""
        lines = text.split("\n")
        if len(lines) <= max_lines:
            return text

        half = max_lines // 2
        truncated = lines[:half] + [f"\n... ({len(lines) - max_lines} lines omitted) ...\n"] + lines[-half:]
        return "\n".join(truncated)

    # ─────────────────────────────────────────────
    # 이미지 렌더링 (Pillow 기반)
    # ─────────────────────────────────────────────
    def _html_to_image(self, html_content: str, output_path: str) -> None:
        """Pillow로 터미널 스타일 이미지를 직접 생성 (Playwright 대체)"""
        # HTML이 아닌 원본 텍스트를 사용하여 Pillow로 직접 렌더링
        # _build_html 호출 전 원본 텍스트를 저장해두므로 여기서는
        # 실제로 render() 메서드에서 직접 _render_with_pillow를 호출
        pass  # render()에서 직접 호출

    def _render_with_pillow(
        self, text: str, output_path: str, title: str = "Terminal", width: int = 820
    ) -> None:
        """Pillow로 터미널 스타일 이미지 직접 렌더링"""
        from PIL import Image, ImageDraw, ImageFont

        c = self.colors

        # 폰트 설정
        font_paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
        ]
        try:
            font = ImageFont.truetype(font_paths[0], 14)
            font_bold = ImageFont.truetype(font_paths[1], 14)
            font_title = ImageFont.truetype(font_paths[0], 13)
        except (OSError, IndexError):
            font = ImageFont.load_default()
            font_bold = font
            font_title = font

        # 텍스트 라인 분석
        lines = text.split("\n")
        line_height = 24
        padding_x = 28
        padding_y = 24
        header_height = 44
        dot_radius = 6
        corner_radius = 12

        # 이미지 크기 계산
        content_height = len(lines) * line_height + padding_y * 2
        total_height = header_height + content_height
        img_padding = 24

        img_width = width + img_padding * 2
        img_height = total_height + img_padding * 2

        # 이미지 생성
        img = Image.new("RGB", (img_width, img_height), self._hex_to_rgb(c["mantle"]))
        draw = ImageDraw.Draw(img)

        # 터미널 박스 (rounded rect)
        box_x = img_padding
        box_y = img_padding
        box_w = width
        box_h = total_height

        # 배경 (rounded rectangle)
        draw.rounded_rectangle(
            [box_x, box_y, box_x + box_w, box_y + box_h],
            radius=corner_radius,
            fill=self._hex_to_rgb(c["base"]),
            outline=self._hex_to_rgb(c["surface0"]),
            width=1,
        )

        # 헤더 영역 배경
        draw.rounded_rectangle(
            [box_x, box_y, box_x + box_w, box_y + header_height],
            radius=corner_radius,
            fill=self._hex_to_rgb(c["mantle"]),
        )
        # 헤더 하단 직선 부분 채우기 (코너 아래)
        draw.rectangle(
            [box_x, box_y + corner_radius, box_x + box_w, box_y + header_height],
            fill=self._hex_to_rgb(c["mantle"]),
        )
        # 헤더 구분선
        draw.line(
            [box_x, box_y + header_height, box_x + box_w, box_y + header_height],
            fill=self._hex_to_rgb(c["surface0"]),
            width=1,
        )

        # 트래픽 라이트 dots
        dot_y = box_y + header_height // 2
        dot_colors = [c["red"], c["green"], c["yellow"]]
        for i, color in enumerate(dot_colors):
            cx = box_x + 20 + i * 22
            draw.ellipse(
                [cx - dot_radius, dot_y - dot_radius, cx + dot_radius, dot_y + dot_radius],
                fill=self._hex_to_rgb(color),
            )

        # 타이틀
        title_bbox = draw.textbbox((0, 0), title, font=font_title)
        title_w = title_bbox[2] - title_bbox[0]
        title_x = box_x + (box_w - title_w) // 2
        draw.text(
            (title_x, dot_y - 7),
            title,
            fill=self._hex_to_rgb(c["overlay0"]),
            font=font_title,
        )

        # 본문 텍스트
        content_y = box_y + header_height + padding_y
        for i, line in enumerate(lines):
            y = content_y + i * line_height
            color, use_bold = self._get_line_style(line)
            f = font_bold if use_bold else font
            draw.text(
                (box_x + padding_x, y),
                line,
                fill=self._hex_to_rgb(color),
                font=f,
            )

        # output 디렉토리 생성 & 저장
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        img.save(output_path, "PNG", optimize=True)

    def _get_line_style(self, line: str) -> tuple[str, bool]:
        """라인 내용에 따라 색상과 볼드 여부 결정"""
        c = self.colors

        if line.startswith("$ "):
            return c["green"], True
        elif any(line.startswith(ch) for ch in ["✅", "✓", "⭐"]) or "complete" in line.lower() or "success" in line.lower():
            return c["green"], False
        elif any(line.startswith(ch) for ch in ["❌", "✗", "⛔"]) or "error" in line.lower() or "fail" in line.lower():
            return c["red"], False
        elif any(line.startswith(ch) for ch in ["⚠", "⚡"]) or "warning" in line.lower():
            return c["yellow"], False
        elif any(line.startswith(ch) for ch in ["ℹ", "📊", "📈", "📉", "🔍"]) or line.startswith("INFO"):
            return c["blue"], False
        elif line.startswith("#"):
            return c["overlay0"], False
        elif re.match(r"^[-─═]{3,}", line):
            return c["overlay0"], False
        else:
            return c["text"], False

    @staticmethod
    def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
        """#RRGGBB → (R, G, B)"""
        h = hex_color.lstrip("#")
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


# ─────────────────────────────────────────────
# CLI 테스트
# ─────────────────────────────────────────────
if __name__ == "__main__":
    import sys

    renderer = TerminalRenderer()

    if len(sys.argv) > 1 and sys.argv[1] == "--command":
        cmd = sys.argv[2] if len(sys.argv) > 2 else "echo 'Hello World!'"
        result = renderer.render_command(cmd, "/tmp/terminal_test.png", title="Test")
        print(f"✅ 캡처 완료: {result['path']}")
    else:
        sample = """$ python analyze.py --dataset aws_costs.csv
📊 Loading dataset: aws_costs.csv (12,345 rows)
🔍 Analyzing cost patterns...

───────────────────────────────────
Service         Monthly Cost    Change
───────────────────────────────────
EC2             $12,450.00      -38%
RDS             $3,200.00       -15%
S3              $890.00         +2%
Lambda          $125.00         -52%
───────────────────────────────────
Total Savings:  $8,340.00/month

✅ Analysis complete! Report saved to /output/report.html
✅ Dashboard updated at http://localhost:8501"""

        renderer.render(sample, "/tmp/terminal_test.png", title="AWS Cost Analysis")
        print("✅ 테스트 이미지 생성: /tmp/terminal_test.png")
