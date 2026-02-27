# Screenshot Capture Guide

## 개요

프로젝트 분석 결과를 기반으로 스크린샷을 자동 캡처하여 Notion 페이지에 업로드.

**모듈 위치**: `screenshot-capture/`

## 캡처 흐름

```
1. 프로젝트 분석 → 캡처 전략 수립
2. 웹앱 감지 → 프레임워크별 자동 실행
3. 캡처 실행 → Playwright / Terminal Renderer
4. Notion 업로드 → File Upload API
```

## 웹앱 프레임워크 감지

| Framework | 감지 방법 | 실행 명령 |
|-----------|----------|----------|
| Streamlit | `streamlit` in requirements.txt | `streamlit run app.py` |
| React | `react` in package.json | `npm start` or `npm run dev` |
| Flask | `flask` in requirements.txt | `flask run` or `python app.py` |
| Gradio | `gradio` in requirements.txt | `python app.py` |
| Dash | `dash` in requirements.txt | `python app.py` |

## 캡처 타입별 전략

### 1. 웹앱 캡처 (Playwright)
- 앱 자동 시작 → 포트 대기 → Playwright 캡처
- 반응형: 1280x800 (데스크톱) + 375x812 (모바일)
- 핵심 페이지 2-3장 캡처

### 2. 터미널 캡처 (Catppuccin Renderer)
- CLI 출력을 이미지로 변환
- Catppuccin Mocha 테마 적용
- Pillow로 PNG 생성

### 3. 정적 파일 캡처
- 차트/그래프 이미지 자동 탐색
- `output/`, `plots/`, `figures/` 디렉토리 스캔

## 캡처 계획 프리뷰

캡처 실행 전 유저에게 계획 표시:

```
📸 캡처 계획
1. [웹앱] 메인 대시보드 (1280x800)
2. [웹앱] 상세 분석 페이지 (1280x800)
3. [터미널] 모델 학습 결과 출력

진행할까요? (Y/N)
```

## Notion File Upload

캡처 완료 후 Notion File Upload API로 페이지에 직접 업로드:
- 파일 형식: PNG (최대 5MB)
- 업로드 후 file_upload_id 반환
- 페이지 콘텐츠에 이미지 블록으로 삽입

## 의존성

- **필수**: Pillow (터미널 렌더링)
- **선택**: playwright (웹앱 캡처, 미설치 시 스킵)

## 타입별 캡처 전략

| Type | 추천 캡처 | 우선순위 |
|------|----------|---------|
| Type 1 | 대시보드, Before/After 차트 | 성과 시각화 |
| Type 2 | 분석 노트북 출력, 차트 | 인사이트 시각화 |
| Type 3 | 앱 스크린샷, UI, 데모 | **최우선** — 프로덕트는 보여주는 게 핵심 |
| Type 4 | Kaggle 노트북, 학습 결과 | 성장 증거 |
| Type 5 | 워크플로우 실행 결과, 로그 | 자동화 증거 |
