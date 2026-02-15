---
name: notion-project-upload
description: Upload projects to Notion with optimized portfolio templates and auto-captured screenshots. Automatically analyzes project type (business/exploratory/learning), applies the appropriate template, and captures portfolio-optimized screenshots using Playwright/Pillow. Handles 14 property fields including Problem/Solution/Impact/Learning, tech stack tagging, glow colors, auto-updated dates, and intelligent screenshot placement.
---

# Notion Project Upload

Upload or update projects in Notion portfolio database with optimized, recruiter-friendly templates.

**Version**: 1.5.0

## Database Configuration

- **Data Source ID**: `ce6722a9-00b2-4d0e-8eda-190f4ce97cb6`
- **Database URL**: https://www.notion.so/3249e5d70c6c4fbebe400ee3d8d2d4c7

## Project Type Detection

Analyze content and classify into one of 3 types:
Analyze content and classify into one of 3 types:

| Type | Triggers | Template Focus |
|------|----------|---------------|
| **1. Business Impact** | 매출, ROI, KPI, conversion, A/B 테스트, 감소, 증가, 개선 | Before/After tables, metrics in **bold**, Collaboration & Deployment |
| **2. Exploratory Analysis** | 분석, EDA, 인사이트, 상관관계, 패턴, 데이터 품질 | Finding-oriented, Statistical Validation, charts/tables |
| **4. Learning Project** | Kaggle, 학습, 연습, 튜토리얼, 강의, 공부 | Learning-focused, ranking/score, reflection |
| **1. Business Impact** | 매출, ROI, KPI, conversion, A/B 테스트, 감소, 증가, 개선 | Before/After tables, metrics in **bold**, Collaboration & Deployment |
| **2. Exploratory Analysis** | 분석, EDA, 인사이트, 상관관계, 패턴, 데이터 품질 | Finding-oriented, Statistical Validation, charts/tables |
| **4. Learning Project** | Kaggle, 학습, 연습, 튜토리얼, 강의, 공부 | Learning-focused, ranking/score, reflection |

**Default**: 정량 지표 있으면 Type 1, 없으면 Type 2.

## Workflow

### Step 1: Read Template

타입 감지 후 해당 템플릿 파일만 읽기 (전체 읽기 금지):

```
Type 1 → references/type1-template.md
Type 2 → references/type2-template.md
Type 4 → references/type4-template.md
```

필요 시에만 추가 가이드 참조:
```
Mermaid 다이어그램 필요 → references/guides/mermaid-guide.md
Extra-Label 작성 필요 → references/guides/extra-label-guide.md
차별화 전략 필요 → references/guides/differentiation-guide.md
```

### Step 2: Portfolio Balance Check (업로드 전 자동 실행)

기존 Notion DB 조회 후 밸런스 분석:

**체크 항목**:
1. **Type 분포**: Type 1/2/4 각 최소 1개 이상 권장
2. **기술스택 커버리지**: 핵심 역량 (SQL, Python, Tableau) 중 빠진 것 확인
3. **글로우 색상**: 3개 이상 다른 색상 권장
4. **섹션 구조**: 프로젝트 간 구조가 80%+ 동일하면 경고
5. **수치 스케일**: 프로젝트 간 임팩트 규모 일관성

**출력 형식**:
```
📊 포트폴리오 밸런스 체크
⚠️ SQL 프로젝트가 없습니다. Type 2에 BigQuery 분석 추가를 권장합니다.
⚠️ 3개 프로젝트 모두 동일 6단계 구조입니다. 섹션 순서 변경을 권장합니다.
✅ Type 분포 OK (Type 1: 2개, Type 2: 1개, Type 4: 1개)
✅ 글로우 색상 3종 사용 중 (teal, amber, purple)
```

밸런스 결과를 유저에게 보여준 후 업로드 진행.

### Step 3: Generate Content

템플릿 기반으로 콘텐츠 생성. 아래 규칙 준수.

### Step 4: Screenshot Capture (자동)

프로젝트 분석 결과를 기반으로 스크린샷 자동 캡처. 상세: [Screenshot Auto-Capture](#screenshot-auto-capture-v150) 섹션 참조.

1. **캡처 전략 수립**: 유형별 캡처 템플릿 선택 + Impact 정량 수치 감지
2. **웹앱 감지**: Streamlit/React/Flask/Gradio 자동 감지 → 실행 → Playwright 캡처
3. **터미널 캡처**: CLI 프로젝트 → 실행 결과를 Catppuccin 테마 이미지로 변환 (Pillow)
4. **캡처 계획 프리뷰**: 유저에게 캡처 목록 보여준 후 진행

### Step 5: Upload/Update

**신규**: Notion DB에 새 페이지 생성
**업데이트**: 기존 페이지 수정 + Diff 프리뷰 표시

## Update Diff Preview (업데이트 시 필수)

업데이트 적용 전에 변경 요약을 유저에게 보여주고 확인받기:

```
📝 변경 사항 프리뷰
- [수정] Problem: "데이터 부족" → "12만 건 데이터에서 패턴 미발견"
- [추가] Statistical Validation 섹션 신규
- [유지] Performance Overview (변경 없음)
- [수정] 업데이트 날짜: 2026.02.11 → 2026.02.14

진행할까요? (Y/N)
```

## Section Structure (유연한 구조)

### 필수 섹션 (모든 프로젝트)
- **Performance Overview** — 상단 고정, 30초 스캔용 테이블
- **Key Takeaways** — 상위 50% 배치
- **Links** — 하단

### 권장 섹션 (프로젝트 특성에 따라 2-3개 선택)
- Problem & Root Cause
- Data & Methodology
- Findings / Results
- Collaboration & Impact
- Statistical Validation
- Deployment & Usage

### 선택 섹션 (해당 시에만)
- A/B Test
- Error Analysis
- Real-world Application

### 프로젝트별 차별화 예시
```
프로젝트 A: Overview → Methodology → Findings → Collaboration → Takeaways
프로젝트 B: Overview → Problem → A/B Test → Impact → Takeaways
프로젝트 C: Overview → Data Deep-dive → Statistical Validation → Takeaways
```

**핵심**: 포트폴리오 내 프로젝트들이 서로 다른 구조를 가져야 함. 동일한 6단계 프로세스 반복 금지.

## Metric Guidelines (수치 현실성)

**대원칙**: 3년차 커리어 전환자 포트폴리오에 맞는 현실적 수치 사용

### 스케일 가이드
| 레벨 | 데이터 규모 | 임팩트 규모 | 예시 |
|------|------------|------------|------|
| 개인/사이드 | 수백~수천 건 | 수십만 원 절감 | 개인 대시보드, 스터디 |
| 팀/소규모 | 수천~수만 건 | 수백만 원 절감 | 팀 자동화, 리포트 |
| 부서/중규모 | 수만~수십만 건 | 수천만 원 임팩트 | 부서 분석, A/B 테스트 |

### 규칙
- **실제 경험 기반**: 없는 수치를 만들지 말 것
- **과정 중심**: 임팩트가 작아도 분석 과정이 탄탄하면 OK
- **비율(%) 중심**: 절대 금액보다 개선율이 더 설득력 있음
- **보수적 추정**: "최소 ~" 표현으로 신뢰성 확보
- **가정 명시**: "월 방문자 10,000명 가정 시" 등

**⚠️ 절대 금지**:
- ROI 1,000%+ (시니어 ML 엔지니어 수준)
- 연 수억 원 임팩트 (대기업 전담팀 규모)
- 120K+ 유저 데이터 without context (데이터 출처 명시 필수)

## Language Rules (언어 사용 규칙)

| 요소 | 언어 | 이유 |
|------|------|------|
| 섹션 제목 | Emoji + English | 글로벌 가독성 |
| 본문 | 한국어 | 타겟 채용시장 |
| 코드 주석 | 한국어 | 설명 목적 |
| Property 값 | 한국어 | Problem, Solution, Impact, Learning |
| Extra-Label | 영어 대문자 | 카드 UI 가독성 |
| 기술 용어 | 영어 원문 유지 | XGBoost, A/B Test, ROI |

## Design Rules

- **Section titles**: Emoji + English (e.g., `🎯 Performance Overview`)
- **F-Pattern**: 성과/발견/학습을 상위 50%에 배치
- **Toggle blocks**: 최소화. 100줄+ 코드나 부가 자료만 토글
- **Bullets**: 하이브리드 — 리스트는 불릿, 배경설명은 단락, 숫자 비교는 테이블(선호)
- **Emojis**: 섹션 헤딩만, 본문 최소화
- **Code blocks**: 핵심 로직 10-15줄, 최대 20줄, 주석 포함
- **Mermaid diagrams**: 3-5단계 간소화
- **Quantitative metrics**: **볼드** 처리
- **Section titles**: Emoji + English (e.g., `🎯 Performance Overview`)
- **F-Pattern**: 성과/발견/학습을 상위 50%에 배치
- **Toggle blocks**: 최소화. 100줄+ 코드나 부가 자료만 토글
- **Bullets**: 하이브리드 — 리스트는 불릿, 배경설명은 단락, 숫자 비교는 테이블(선호)
- **Emojis**: 섹션 헤딩만, 본문 최소화
- **Code blocks**: 핵심 로직 10-15줄, 최대 20줄, 주석 포함
- **Mermaid diagrams**: 3-5단계 간소화
- **Quantitative metrics**: **볼드** 처리

## Properties (14 Fields)

### Core Analysis
| Property | Description |
|----------|-------------|
| **Problem** | 문제 정의 (2-3문장, 비즈니스 맥락 포함) |
| **Solution** | 해결 방법 (번호 매기기) |
| **Impact** | 성과 (정량/정성, 현실적 스케일) |
| **Impact** | 성과 (정량/정성, 현실적 스케일) |
| **Learning** | 학습 내용 및 회고 |

### Metadata
| Property | Format |
|----------|--------|
| **프로젝트명** | 이모지 + 프로젝트명 (한국어) |
| **상세제목** | 영문 또는 한글 상세 제목 |
| **한줄설명** | 한 문장 요약 |
| **기술스택** | 배열 태그 (Python, Tableau, LangChain, etc.) |
| **카테고리** | 데이터 분석 / AI & Automation / 웹 개발 등 |
| **글로우색상** | teal(분석), amber(자동화), red(비즈니스), purple(AI/ML), pink(시각화) |

### Extra Fields
| Property | Format |
|----------|--------|
| **Extra-Label** | 영어 대문자 섹션 제목 (e.g., "A/B TEST DESIGN") |
| **Extra** | `**제목** — 설명` 형식 (마크다운 볼드) |
| **Extra-Label** | 영어 대문자 섹션 제목 (e.g., "A/B TEST DESIGN") |
| **Extra** | `**제목** — 설명` 형식 (마크다운 볼드) |

### Auto-Generated
| Property | Format |
|----------|--------|
| **업데이트 날짜** | YYYY.MM.DD (오늘 날짜 자동) |

## Tech Stack Tags

Python, Pandas, NumPy, Matplotlib, Seaborn, Tableau, Power BI, SQL, BigQuery, PostgreSQL, MySQL, LangChain, OpenAI API, FAISS, RAG, Streamlit, Flask, FastAPI, Playwright, Selenium, JavaScript, React, Node.js, Google Sheets, Looker Studio, Discord API, GitHub Actions, Vercel
Python, Pandas, NumPy, Matplotlib, Seaborn, Tableau, Power BI, SQL, BigQuery, PostgreSQL, MySQL, LangChain, OpenAI API, FAISS, RAG, Streamlit, Flask, FastAPI, Playwright, Selenium, JavaScript, React, Node.js, Google Sheets, Looker Studio, Discord API, GitHub Actions, Vercel

## Quality Checklist

### 구조
- ✅ Performance Overview 테이블이 최상단에 있는가?
- ✅ 섹션 제목이 Emoji + English인가?
- ✅ Key Takeaways가 상위 50%에 위치하는가?
- ✅ **다른 프로젝트와 섹션 구조가 다른가?** (동일 구조 반복 금지)
- ✅ 코드 블록이 10-15줄 이내인가? (최대 20줄)
- ✅ 섹션 중복이 없는가?

### 콘텐츠
- ✅ 수치가 현실적 스케일인가? (Metric Guidelines 참조)
- ✅ Before/After 테이블 있는가? (Type 1)
- ✅ 통계 검증 있는가? (Type 2: 가설, p-value, 효과크기)
- ✅ 비즈니스 맥락("왜 이게 중요한지") 설명했는가?
- ✅ Extra/Extra-Label이 채워졌는가?

### Properties
- ✅ 14개 properties 전부 채워졌는가?
- ✅ 날짜가 YYYY.MM.DD 형식인가?
- ✅ Problem에 비즈니스 맥락 포함?
- ✅ Impact가 정량+정성?
### 구조
- ✅ Performance Overview 테이블이 최상단에 있는가?
- ✅ 섹션 제목이 Emoji + English인가?
- ✅ Key Takeaways가 상위 50%에 위치하는가?
- ✅ **다른 프로젝트와 섹션 구조가 다른가?** (동일 구조 반복 금지)
- ✅ 코드 블록이 10-15줄 이내인가? (최대 20줄)
- ✅ 섹션 중복이 없는가?

### 콘텐츠
- ✅ 수치가 현실적 스케일인가? (Metric Guidelines 참조)
- ✅ Before/After 테이블 있는가? (Type 1)
- ✅ 통계 검증 있는가? (Type 2: 가설, p-value, 효과크기)
- ✅ 비즈니스 맥락("왜 이게 중요한지") 설명했는가?
- ✅ Extra/Extra-Label이 채워졌는가?

### Properties
- ✅ 14개 properties 전부 채워졌는가?
- ✅ 날짜가 YYYY.MM.DD 형식인가?
- ✅ Problem에 비즈니스 맥락 포함?
- ✅ Impact가 정량+정성?

## Version History

- **v1.4.0** (2026.02.14): Major restructure
  - **파일 분리**: templates.md(2,390줄) → 타입별 템플릿 + 가이드 파일로 분리 (토큰 75% 절감)
  - **유연한 섹션 구조**: 필수/권장/선택 섹션으로 프로젝트별 차별화
  - **수치 현실성 가이드**: 커리어 전환자 수준에 맞는 스케일 가이드 추가
  - **언어 규칙 명시**: 섹션 제목, 본문, 코드, Property별 언어 사용 기준
  - **포트폴리오 밸런스 체크**: 업로드 전 DB 조회 → Type/기술스택/색상/구조 밸런스 분석
  - **Update Diff 프리뷰**: 업데이트 전 변경사항 요약 표시
  - **버그 수정**: Type 3 잔재 제거, 예제 중복 섹션 제거, 코드블록 길이 준수
- **v1.3.2** (2026.02.12): 3-Type 구조로 단순화 (Type 3 제거)
- **v1.3.0** (2026.02.11): 차별화 전략, 임팩트 정량화, Mermaid/Extra 가이드
- **v1.2.0** (2026.02.11): Collaboration, Statistical Validation, Deployment 섹션 추가
- **v1.1.0** (2026.02.11): Dataset 섹션 추가
- **v1.0.0** (2026.02.10): 최초 릴리즈

## Screenshot Auto-Capture (v1.5.0)

프로젝트 업로드 시 포트폴리오에 최적화된 스크린샷을 **자동으로 판단하고 캡처**한다.
사용자가 별도로 요청하지 않아도, 프로젝트 분석 단계에서 캡처 전략을 수립한다.

### 판단 기준: "면접관이 10초 안에 파악하고 싶은 것"

**1. 결과물이 보이는가? (필수)**
- 대시보드 → 전체 화면 캡처
- 웹앱 → 메인 UI 캡처
- CLI 도구 → 실행 결과 터미널 캡처
- 분석 프로젝트 → 핵심 차트/테이블 캡처

**2. 임팩트가 보이는가? (필수)**
- 정량적 개선이 있으면 → 수치가 보이는 화면 캡처
- Impact에 %, $, 시간, 건수 등 수치 → 해당 지표 강조 캡처

**3. 기술적 깊이가 보이는가? (권장)**
- 복잡한 실행 결과 → 터미널 캡처
- 자동화 로그 → 성공 실행 로그 캡처

### 캡처하지 않는 것

- 코드 에디터 화면 (코드는 본문에 코드블록으로)
- 설정 파일 내용 / 에러·디버깅 화면
- 로그인/인증 화면 / README 화면

### 유형별 캡처 전략

| 프로젝트 유형 | 캡처 수 | 캡처 대상 |
|---|---|---|
| Dashboard/시각화 | 2~4장 | 대시보드 전체 + 핵심 차트 + 필터 인터랙션 |
| 자동화 | 2~3장 | 실행 로그 + Before/After + 결과물 |
| 데이터 분석 | 2~3장 | 핵심 발견 차트 + 분석 결과 + 파이프라인 |
| 웹앱 | 2~3장 | 메인 UI + 핵심 기능 동작 |
| ML/AI | 2~3장 | 모델 성능 지표 + 예측 결과 |

추가 우선순위 조정: Impact에 정량 수치 (`%`, `$`, `시간`) 감지 시 Before/After 캡처를 필수로 추가.

### 캡션 작성 규칙

캡션 템플릿: `{프로젝트명} — {캡처 대상} {핵심 수치}`

```
BAD:  "스크린샷 1", "dashboard.png"
GOOD: "월별 AWS 비용 추이 — EC2 Reserved Instance 전환 후 38% 절감"
GOOD: "A/B 테스트 결과 — 실험군 전환율 12.3% (p < 0.05)"
GOOD: "자동화 실행 로그 — 데이터 수집~리포트 생성 5분 완료"
```

### 이미지 Notion 배치 위치

Solution 섹션과 Technical 섹션 사이에 "Demo" 헤딩 아래 삽입:

```
├─ 🎯 Performance Overview
├─ Problem & Solution
├─ ── 📸 Demo ──              ← 이미지 섹션
│   ├─ [메인 스크린샷]           (전체 너비)
│   └─ [핵심 인사이트/상세]       (전체 너비)
├─ Technical Details
└─ Key Takeaways
```

메인 스크린샷은 페이지 커버로 자동 설정.

### 이미지 업로드 방식

**Notion File Upload API** 사용 (외부 호스팅 불필요):

```
Step 1: POST /v1/file_uploads → file_upload_id
Step 2: POST /v1/file_uploads/{id}/send → multipart/form-data
Step 3: PATCH /v1/blocks/{page_id}/children → image block 첨부
```

### 웹앱 자동 감지

| 프레임워크 | 감지 패턴 | 포트 |
|---|---|---|
| Streamlit | `import streamlit`, `st.` | 8501 |
| React/Next | `package.json` → `"react"` | 3000 |
| Flask | `from flask`, `Flask(` | 5000 |
| Gradio | `import gradio`, `gr.` | 7860 |
| Dash | `import dash` | 8050 |

### 터미널 캡처

CLI/자동화 프로젝트의 실행 결과를 Catppuccin Mocha 테마 이미지로 변환.
Pillow 기반 렌더링 (외부 의존성 최소화).
자동 구문 강조: `$` 프롬프트(초록), 성공✅(초록), 에러❌(빨강), 수치(주황).

### 모듈 구조

```
screenshot-capture/
├── __init__.py
├── capture_manager.py      ← 메인 오케스트레이터
├── strategies.py            ← 유형/JD 기반 캡처 전략
├── terminal_renderer.py     ← 터미널 → 이미지 (Pillow)
└── notion_file_upload.py    ← Notion File Upload API 래퍼
```

### 의존성

- `Pillow` — 터미널 이미지 렌더링 (필수)
- `playwright` — 웹앱 캡처 (선택, 웹앱 프로젝트만)
- Notion API token — File Upload API (기존 토큰 그대로 사용)
