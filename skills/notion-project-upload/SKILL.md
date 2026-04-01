---
name: notion-project-upload
description: "Notion 프로젝트 데이터베이스에 프로젝트를 업로드/업데이트하는 스킬. 트리거: 프로젝트 업로드, 노션에 올려줘, 프로젝트 등록, 포트폴리오 업로드, 프로젝트 DB 등록. 직군 무관하게 프로젝트 내용을 최대한 상세하게 기록한다. Notion을 프로젝트 원장 DB로 활용하며, 나중에 어떤 직무 포트폴리오를 만들어도 여기서 꺼내 쓸 수 있도록 팩트를 완전하게 보존한다."
---

# Notion Project Upload — v2.3.0

> **Notion = 프로젝트 원장 DB**
> 직군 색 없이 팩트를 최대한 상세하게 기록한다.
> 포트폴리오 작성은 별도로 진행한다.

## Database Configuration

- **Data Source ID**: `ce6722a9-00b2-4d0e-8eda-190f4ce97cb6`
- **Database URL**: https://www.notion.so/3249e5d70c6c4fbebe400ee3d8d2d4c7

## Portfolio Structure: PACRL Framework

모든 프로젝트는 아래 6단계 서술 구조를 따른다:

| 필드 | 역할 | 핵심 질문 |
|------|------|-----------|
| **Problem** | 배경 + 문제 정의 | 왜 이게 문제인가? |
| **Approach** | 방법 선택 근거 | 왜 이 방법인가? 다른 대안은 왜 아닌가? |
| **Solution** | 구현 내용 | 어떻게 해결했는가? |
| **Challenge** | 시행착오 | 어떤 어려움이 있었고 어떻게 극복했는가? |
| **Result** | 정량 성과 | 수치로 무엇이 달라졌는가? |
| **Learning** | 인사이트 | 이 경험에서 무엇을 배웠는가? |

> ⚠️ **Approach와 Challenge가 핵심 차별점이다.** 대부분의 포트폴리오는 Problem → Solution → Result만 있다.
> Approach(왜 이 방법?)와 Challenge(시행착오)를 채울 때 가장 강력한 포트폴리오가 된다.

### PACRL 진단 체크리스트

각 프로젝트 업로드 전 아래 항목이 채워졌는지 확인:

```
☐ Problem   — 배경 + 왜 이게 문제인지 설득 가능한가?
☐ Approach  — 왜 이 방법을 선택했는지 근거(데이터, 리서치, 벤치마킹)가 있는가?
☐ Solution  — 구현 내용이 구체적인가?
☐ Challenge — A시도 → B시도 피벗 등 시행착오가 포함됐는가?
☐ Result    — 정량 수치가 있는가? (없으면 정성적 변화라도)
☐ Learning  — 이 프로젝트로 무엇을 체득했는지 명시됐는가?
```

빈 항목은 README/CLAUDE.md에서 단서를 찾거나, 사용자에게 질문하여 채운다.

---

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

---

## Workflow

### Step 1: 타입별 권장 섹션 결정

타입 감지 후 아래 힌트를 참고해 섹션을 구성한다. 외부 파일 참조 불필요.

| Type | 강화할 섹션 |
|------|-----------|
| 1. Impact | Before/After 테이블, A/B Test, 비용·시간 절감 정량화 |
| 2. Analysis | 방법론, 데이터 출처, 가설-검증-결과, 핵심 발견 |
| 3. Product | 기능 목록, 아키텍처, UX 플로우, 사용자 가치 |
| 4. Learning | 학습 목표, Before/After 역량, 실무 적용 계획 |
| 5. Automation | 워크플로우 다이어그램, 에러 처리, 효율화 수치 |

필요 시만 가이드 참조:
```
Mermaid  → references/guides/mermaid-guide.md
스크린샷 → references/guides/screenshot-guide.md
예시     → references/examples/project-record-example.md
```

### Step 2: Portfolio Balance Check (업로드 전 자동 실행)

기존 Notion DB 조회 후 밸런스 분석:

**체크 항목**:
1. **Type 분포**: 5개 타입 중 최소 3개 이상 존재 권장
2. **기술스택 커버리지**: 핵심 역량 (SQL, Python, Tableau) 중 빠진 것 확인
3. **글로우 색상**: 3개 이상 다른 색상 권장
4. **섹션 구조**: 프로젝트 간 구조가 80%+ 동일하면 경고
5. **수치 스케일**: 프로젝트 간 임팩트 규모 일관성
6. **PACRL 완성도**: Approach, Challenge 필드가 빈 프로젝트 수 확인

**출력 형식**:
```
📊 포트폴리오 밸런스 체크
⚠️ Product Development(Type 3) 프로젝트가 없습니다.
✅ Type 분포 OK (Type 1: 2개, Type 2: 1개, Type 5: 1개)
✅ 글로우 색상 3종 사용 중 (teal, amber, purple)
⚠️ Approach 필드 미작성 프로젝트: 3개 (소급 보완 권장)
```

### Step 3: 프로젝트 파일 수집 후 PACRL 진단

#### 파일 수집 (우선순위 기반 선택 읽기)

전체 폴더를 무조건 읽지 않는다. 아래 순서로 필요한 것만 읽는다.

**1단계 — 폴더 구조 파악 (목록만, 읽기 아님)**
```
ls -1 프로젝트루트/     → 최상위 파일/폴더 목록 확인
```
이 결과로 어떤 파일이 있는지 파악하고 읽을 대상 결정.

**2단계 — 항상 읽기 (핵심 문서)**
```
README.md       → 프로젝트 개요, 문제/해결/성과
CLAUDE.md       → 설계 결정, 아키텍처, 개발 컨텍스트 (있으면)
CLAUDE_DEV.md   → 개발 노트 (있으면)
```

**3단계 — 기술스택/환경 파악**
```
package.json          → 기술스택, 스크립트
requirements.txt      → Python 의존성
pyproject.toml        → Python 프로젝트 설정
.env.example          → 사용 기술 파악용 (실제 .env 읽기 금지)
```

**4단계 — 조건부 읽기 (필요 시만)**
```
.git/logs/HEAD              → 진행기간 추출 (첫/마지막 커밋 날짜)
docs/ 또는 architecture.*   → 설계 문서 (있으면)
main.py / app.py / index.ts → 핵심 진입점 (README만으로 부족할 때)
vercel.json / netlify.toml  → 배포 환경
```

**건너뛸 것 (읽지 않음)**
```
node_modules/  dist/  build/  __pycache__/
.git/objects/  *.lock  테스트 파일  바이너리
```

> 수집한 파일들을 종합해서 PACRL 6개 필드를 채운다.
> README만으로 충분하면 추가 파일 읽기 불필요.

**Approach 작성 가이드**:
- 왜 이 방법을 선택했는가? 근거(데이터, 리서치, 벤치마킹)를 포함
- 다른 대안(라이브러리, 방법론, 아키텍처)은 왜 배제했는가?
- 예: "초기에는 X를 검토했으나 Y 이유로 Z를 선택했다"

**Challenge 작성 가이드**:
- A시도 → 실패 → B시도 피벗 과정을 서술
- 기술적 난관, 데이터 품질 문제, 설계 변경 등 포함
- 실패 사례도 OK — 면접관은 시행착오를 높이 평가한다
- 예: "초기 모델 MAPE 18%로 목표 미달 → feature engineering 재설계 후 11.3% 달성"

### Step 4: Screenshot Capture (자동)

프로젝트 분석 결과를 기반으로 스크린샷 자동 캡처.
상세: `references/guides/screenshot-guide.md` 참조.

### Step 5: Upload/Update

**신규**: Notion DB에 새 페이지 생성
**업데이트**: 기존 페이지 수정 + Diff 프리뷰 표시

#### ⚠️ 업데이트 시 강제 재평가 항목

기존 내용이 있어도 아래 항목은 **반드시 프로젝트 파일(README 등)과 비교해서 재평가**한다.
"이미 채워져 있음"은 유지 이유가 되지 않는다.

| 필드 | 재평가 기준 | 업데이트 트리거 |
|------|------------|----------------|
| **Approach** | 왜 이 방법을 선택했는가 + 대안 검토가 모두 있는가? | 대안 비교 없으면 → 보강 |
| **Challenge** | 실패 시도 / A→B 피벗 / 구현 중 난관이 구체적으로 있는가? | 추상적이거나 빈 경우 → 보강 |
| **Result** | 처리 시간, 에러율, 비용, 공수 등 **모든 측정 가능한 수치**가 있는가? | 수치 누락 있으면 → 추가 |
| **Extra** | 현재 Extra-Label이 프로젝트 핵심 포인트를 반영하는가? | 구식이거나 부적합하면 → 교체 |
| **기술스택** | README 기반으로 누락된 태그가 없는가? | 누락 있으면 → 추가 |
| **업데이트 날짜** | 오늘 날짜인가? | 항상 갱신 |

> **판단 기준**: "이미 내용이 있다"가 아니라 **"v2.3 기준으로 완성됐는가"**를 판단한다.
> Approach에 내용이 있어도 대안 검토가 없으면 → 업데이트.
> Result에 수치가 있어도 일부 수치만 있으면 → 추가.

---

## Update Diff Preview (업데이트 시 필수)

```
📝 변경 사항 프리뷰
- [수정] Problem: "데이터 부족" → "12만 건 데이터에서 패턴 미발견"
- [추가] Approach: 왜 Prophet을 선택했는지 근거 추가
- [추가] Challenge: MAPE 18% → 11.3% 피벗 과정 추가
- [유지] Performance Overview (변경 없음)
- [수정] 업데이트 날짜: 2026.02.11 → 2026.03.06
진행할까요? (Y/N)
```

---

## Section Structure (유연한 구조)

### 필수 섹션 (모든 프로젝트)
- **Performance Overview** — 상단 고정, 30초 스캔용 테이블
- **Key Takeaways** — 상위 50% 배치
- **Links** — 하단

### 권장 섹션 (프로젝트 특성에 따라 2-3개 선택)
- Problem & Root Cause / Why This Approach / Data & Methodology
- Findings / Collaboration & Impact / Statistical Validation / Deployment & Usage
- Feature Showcase / Architecture & System Design (Type 3)
- Workflow & Automation / Efficiency Gains (Type 5)

### 선택 섹션 (해당 시에만)
- A/B Test / Error Analysis / Real-world Application
- User Feedback & Metrics (Type 3) / Monitoring & Observability (Type 5)

### 타입별 섹션 흐름 예시
```
Type 1: Overview → Problem → Why This Approach → A/B Test → Challenge → Impact → Takeaways
Type 2: Overview → Problem → Methodology → Why This Approach → Findings → Challenge → Takeaways
Type 3: Overview → Problem → Why This Approach → Feature Showcase → Challenge → User Metrics → Takeaways
Type 4: Overview → Learning Goal → Why This Approach → Competition → Challenge → Before/After → Reflection
Type 5: Overview → Problem → Why This Approach → Workflow Design → Challenge → Efficiency → Takeaways
```

---

## Metric Guidelines (수치 현실성)

**원칙**: 있는 수치 전부 기록, 직군 필터 없이

| 프로젝트 규모 | 수치 스케일 |
|-------------|-----------|
| 개인/사이드 | 수백~수천 건, 수십만 원, 수 시간 절약 |
| 팀/소규모 | 수천~수만 건, 수백만 원, 수십 시간 |
| 부서/중규모 | 수만~수십만 건, 수천만 원 |

**규칙**: 비율(%) 중심 / 보수적 추정 / 가정 명시

**⚠️ 절대 금지**: 근거 없는 ROI 1,000%+ / 실제보다 부풀린 수치

---

## Language Rules

| 요소 | 언어 | 이유 |
|------|------|------|
| 섹션 제목 | Emoji + English | 글로벌 가독성 |
| 본문 | 한국어 | 타겟 채용시장 |
| Property 값 | 한국어 | Problem, Approach, Solution, Challenge, Result, Learning |
| Extra-Label | 영어 대문자 | 카드 UI 가독성 |
| 기술 용어 | 영어 원문 유지 | XGBoost, A/B Test, ROI |

---

## Design Rules

- **F-Pattern**: 성과/발견/학습을 상위 50%에 배치
- **Toggle blocks**: 최소화. 100줄+ 코드나 부가 자료만 토글
- **Bullets**: 리스트는 불릿, 배경설명은 단락, 숫자 비교는 테이블(선호)
- **Code blocks**: 핵심 로직 10-15줄, 최대 20줄, 주석 포함
- **Mermaid diagrams**: 3-5단계 간소화
- **Quantitative metrics**: **볼드** 처리

---

## Properties (16 Fields)

| Property | Format / Description |
|----------|---------------------|
| **Problem** | 배경 + 문제 정의 (2-3문장, 비즈니스 맥락 포함) |
| **Approach** | 왜 이 방법을 선택했는가 (근거, 대안 검토 포함) |
| **Solution** | 구현 내용 (번호 매기기, 어떻게 해결했는가) |
| **Challenge** | 시행착오, A→B 피벗, 기술적 난관 |
| **Result** | 정량/정성 성과 — **있는 수치 전부 기록** (직군 필터 없이) |
| **Learning** | 학습 내용 및 회고 |
| **프로젝트명** | 이모지 + 프로젝트명 (한국어) |
| **상세제목** | 영문 또는 한글 상세 제목 |
| **한줄설명** | 한 문장 요약 |
| **기술스택** | 배열 태그 (Python, Tableau, LangChain, etc.) |
| **카테고리** | 데이터 분석 / AI & Automation / 웹 개발 등 |
| **글로우색상** | teal(분석), amber(자동화), red(비즈니스), purple(AI/ML), pink(시각화) |
| **Extra-Label** | 영어 대문자 섹션 제목 (e.g., "WHY THIS APPROACH") |
| **Extra** | `**제목** — 설명` 형식 (마크다운 볼드) |
| **업데이트 날짜** | YYYY.MM.DD (오늘 날짜 자동) |
| **진행기간** | YYYY.MM ~ YYYY.MM |

---

## Tech Stack Tags

Python, Pandas, NumPy, Matplotlib, Seaborn, Tableau, Power BI, SQL, BigQuery, PostgreSQL, MySQL, LangChain, OpenAI API, FAISS, RAG, Streamlit, Flask, FastAPI, Playwright, Selenium, JavaScript, React, Node.js, Google Sheets, Looker Studio, Discord API, Slack API, GitHub Actions, Vercel, Amplitude, Mixpanel, Google Analytics (GA4), Firebase, Figma, Jira, Confluence, Notion, Power Automate, Excel, Miro, Lucidchart

---

## Quality Checklist

- ✅ Performance Overview 테이블이 최상단에 있는가?
- ✅ 섹션 제목이 Emoji + English인가?
- ✅ Key Takeaways가 상위 50%에 위치하는가?
- ✅ **다른 프로젝트와 섹션 구조가 다른가?**
- ✅ 코드 블록이 10-15줄 이내인가?
- ✅ 수치가 현실적 스케일인가?
- ✅ 16개 properties 전부 채워졌는가?
- ✅ Extra/Extra-Label이 채워졌는가?
- ✅ **Approach 필드: 왜 이 방법인지 근거가 있는가?**
- ✅ **Challenge 필드: 시행착오/피벗 과정이 포함됐는가?**
- ✅ Type별 필수 요소: Before/After(1), 통계검증(2), Demo/Feature(3), Reflection(4), Workflow(5)
- ✅ Result: 있는 수치 전부 기록했는가? (직군 필터 없이)
