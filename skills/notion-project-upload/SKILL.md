---
name: notion-project-upload
description: "Notion 프로젝트 데이터베이스에 프로젝트를 업로드/업데이트하는 스킬. Claude Code 환경 전용. 트리거: 프로젝트 업로드, 프로젝트 업데이트, 노션 프로젝트, 포트폴리오 업로드, README 기반 업로드, 프로젝트 DB 등록. 사용자의 프로젝트 폴더(README.md, CLAUDE.md 등)를 분석하여 Problem/Solution/Impact/Learning/기술스택/글로우색상/한줄설명/상세제목/Extra/Extra-Label을 자동 추출하고 Notion DB에 생성 또는 업데이트한다. 프로젝트 업로드, 프로젝트 수정, 포트폴리오 관리라는 키워드가 보이면 반드시 이 스킬을 사용할 것."
---

# Notion Project Upload

Upload or update projects in Notion portfolio database with optimized, recruiter-friendly templates.

**Version**: 2.0.0

## Database Configuration

- **Data Source ID**: `ce6722a9-00b2-4d0e-8eda-190f4ce97cb6`
- **Database URL**: https://www.notion.so/3249e5d70c6c4fbebe400ee3d8d2d4c7

## Project Type Detection

Analyze content and classify into one of 5 types:

| Type | Triggers | Template Focus |
|------|----------|---------------|
| **1. Business Impact** | 매출, ROI, KPI, conversion, A/B 테스트, 감소, 증가, 개선 | Before/After tables, metrics, Collaboration & Deployment |
| **2. Exploratory Analysis** | 분석, EDA, 인사이트, 상관관계, 패턴, 데이터 품질 | Finding-oriented, Statistical Validation, charts/tables |
| **3. Product Development** | 웹앱, 모바일앱, 게임, SaaS, 서비스, UI/UX, 배포, 유저 | Feature showcase, architecture, user metrics, demo |
| **4. Learning Project** | Kaggle, 학습, 연습, 튜토리얼, 강의, 공부 | Learning-focused, ranking/score, reflection |
| **5. Automation & Tools** | 봇, 자동화, 파이프라인, 크롤링, CLI, 스케줄러, 모니터링 | Workflow diagram, efficiency gains, system design |

**Default**: 정량 지표 있으면 Type 1, 앱/서비스면 Type 3, 자동화면 Type 5, 없으면 Type 2.

## Workflow

### Step 1: Read Template

타입 감지 후 해당 템플릿 파일만 읽기 (전체 읽기 금지):

```
Type 1 → references/type1-template.md
Type 2 → references/type2-template.md
Type 3 → references/type3-template.md
Type 4 → references/type4-template.md
Type 5 → references/type5-template.md
```

필요 시에만 추가 가이드 참조:
```
Mermaid 다이어그램 → references/guides/mermaid-guide.md
Extra-Label 작성 → references/guides/extra-label-guide.md
차별화 전략 → references/guides/differentiation-guide.md
스크린샷 캡처 → references/guides/screenshot-guide.md
```

### Step 2: Portfolio Balance Check (업로드 전 자동 실행)

기존 Notion DB 조회 후 밸런스 분석:

**체크 항목**:
1. **Type 분포**: 5개 타입 중 최소 3개 이상 존재 권장
2. **기술스택 커버리지**: 핵심 역량 (SQL, Python, Tableau) 중 빠진 것 확인
3. **글로우 색상**: 3개 이상 다른 색상 권장
4. **섹션 구조**: 프로젝트 간 구조가 80%+ 동일하면 경고
5. **수치 스케일**: 프로젝트 간 임팩트 규모 일관성

**출력 형식**:
```
📊 포트폴리오 밸런스 체크
⚠️ Product Development(Type 3) 프로젝트가 없습니다.
✅ Type 분포 OK (Type 1: 2개, Type 2: 1개, Type 5: 1개)
✅ 글로우 색상 3종 사용 중 (teal, amber, purple)
```

### Step 3: Generate Content

템플릿 기반으로 콘텐츠 생성. 아래 규칙 준수.

### Step 4: Screenshot Capture (자동)

프로젝트 분석 결과를 기반으로 스크린샷 자동 캡처.
상세: `references/guides/screenshot-guide.md` 참조.

### Step 5: Upload/Update

**신규**: Notion DB에 새 페이지 생성
**업데이트**: 기존 페이지 수정 + Diff 프리뷰 표시

## Update Diff Preview (업데이트 시 필수)

```
📝 변경 사항 프리뷰
- [수정] Problem: "데이터 부족" → "12만 건 데이터에서 패턴 미발견"
- [추가] Statistical Validation 섹션 신규
- [유지] Performance Overview (변경 없음)
- [수정] 업데이트 날짜: 2026.02.11 → 2026.02.27
진행할까요? (Y/N)
```

## Section Structure (유연한 구조)

### 필수 섹션 (모든 프로젝트)
- **Performance Overview** — 상단 고정, 30초 스캔용 테이블
- **Key Takeaways** — 상위 50% 배치
- **Links** — 하단

### 권장 섹션 (프로젝트 특성에 따라 2-3개 선택)
- Problem & Root Cause / Data & Methodology / Findings / Collaboration & Impact
- Statistical Validation / Deployment & Usage
- Feature Showcase / Architecture & System Design (Type 3)
- Workflow & Automation / Efficiency Gains (Type 5)

### 선택 섹션 (해당 시에만)
- A/B Test / Error Analysis / Real-world Application
- User Feedback & Metrics (Type 3) / Monitoring & Observability (Type 5)

### 프로젝트별 차별화 예시
```
Type 1: Overview → Problem → A/B Test → Impact → Takeaways
Type 2: Overview → Methodology → Findings → Collaboration → Takeaways
Type 3: Overview → Feature Showcase → Architecture → User Metrics → Takeaways
Type 4: Overview → Learning Goal → Competition → Before/After → Reflection
Type 5: Overview → Workflow Design → System Architecture → Efficiency → Takeaways
```

## Metric Guidelines (수치 현실성)

**대원칙**: 3년차 커리어 전환자 포트폴리오에 맞는 현실적 수치 사용

| 레벨 | 데이터 규모 | 임팩트 규모 | 예시 |
|------|------------|------------|------|
| 개인/사이드 | 수백~수천 건 | 수십만 원 절감 | 개인 대시보드, 스터디 |
| 팀/소규모 | 수천~수만 건 | 수백만 원 절감 | 팀 자동화, 리포트 |
| 부서/중규모 | 수만~수십만 건 | 수천만 원 임팩트 | 부서 분석, A/B 테스트 |

**규칙**: 실제 경험 기반 / 비율(%) 중심 / 보수적 추정("최소 ~") / 가정 명시

**⚠️ 절대 금지**: ROI 1,000%+ / 연 수억 원 임팩트 / 120K+ 유저 데이터 without context

## Language Rules

| 요소 | 언어 | 이유 |
|------|------|------|
| 섹션 제목 | Emoji + English | 글로벌 가독성 |
| 본문 | 한국어 | 타겟 채용시장 |
| Property 값 | 한국어 | Problem, Solution, Impact, Learning |
| Extra-Label | 영어 대문자 | 카드 UI 가독성 |
| 기술 용어 | 영어 원문 유지 | XGBoost, A/B Test, ROI |

## Design Rules

- **F-Pattern**: 성과/발견/학습을 상위 50%에 배치
- **Toggle blocks**: 최소화. 100줄+ 코드나 부가 자료만 토글
- **Bullets**: 리스트는 불릿, 배경설명은 단락, 숫자 비교는 테이블(선호)
- **Code blocks**: 핵심 로직 10-15줄, 최대 20줄, 주석 포함
- **Mermaid diagrams**: 3-5단계 간소화
- **Quantitative metrics**: **볼드** 처리

## Properties (14 Fields)

| Property | Format / Description |
|----------|---------------------|
| **Problem** | 문제 정의 (2-3문장, 비즈니스 맥락 포함) |
| **Solution** | 해결 방법 (번호 매기기) |
| **Impact** | 성과 (정량/정성, 현실적 스케일) |
| **Learning** | 학습 내용 및 회고 |
| **프로젝트명** | 이모지 + 프로젝트명 (한국어) |
| **상세제목** | 영문 또는 한글 상세 제목 |
| **한줄설명** | 한 문장 요약 |
| **기술스택** | 배열 태그 (Python, Tableau, LangChain, etc.) |
| **카테고리** | 데이터 분석 / AI & Automation / 웹 개발 등 |
| **글로우색상** | teal(분석), amber(자동화), red(비즈니스), purple(AI/ML), pink(시각화) |
| **Extra-Label** | 영어 대문자 섹션 제목 (e.g., "A/B TEST DESIGN") |
| **Extra** | `**제목** — 설명` 형식 (마크다운 볼드) |
| **업데이트 날짜** | YYYY.MM.DD (오늘 날짜 자동) |

## Tech Stack Tags

Python, Pandas, NumPy, Matplotlib, Seaborn, Tableau, Power BI, SQL, BigQuery, PostgreSQL, MySQL, LangChain, OpenAI API, FAISS, RAG, Streamlit, Flask, FastAPI, Playwright, Selenium, JavaScript, React, Node.js, Google Sheets, Looker Studio, Discord API, GitHub Actions, Vercel

## Quality Checklist

- ✅ Performance Overview 테이블이 최상단에 있는가?
- ✅ 섹션 제목이 Emoji + English인가?
- ✅ Key Takeaways가 상위 50%에 위치하는가?
- ✅ **다른 프로젝트와 섹션 구조가 다른가?**
- ✅ 코드 블록이 10-15줄 이내인가?
- ✅ 수치가 현실적 스케일인가?
- ✅ 14개 properties 전부 채워졌는가?
- ✅ Extra/Extra-Label이 채워졌는가?
- ✅ Type별 필수 요소: Before/After(1), 통계검증(2), Demo/Feature(3), Reflection(4), Workflow(5)
