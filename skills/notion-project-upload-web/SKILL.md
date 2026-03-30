---
name: notion-project-upload-web
description: "Notion 프로젝트 데이터베이스에 프로젝트를 업로드/업데이트하는 스킬. Claude.ai 환경 전용 (Notion MCP + Filesystem 도구 활용). 트리거: 프로젝트 업로드, 노션에 올려줘, 프로젝트 등록, 포트폴리오 업로드, 프로젝트 DB 등록. 직군 무관하게 프로젝트 내용을 최대한 상세하게 기록한다. Notion을 프로젝트 원장 DB로 활용하며, 나중에 어떤 직무 포트폴리오를 만들어도 여기서 꺼내 쓸 수 있도록 팩트를 완전하게 보존한다."
---

# Notion Project Upload (Web Edition) v2.3.0

> Claude.ai 환경에서 Notion MCP 도구를 활용한 프로젝트 원장 DB 업로드/업데이트 스킬
> Synced with: notion-project-upload v2.3.0 (Claude Code)

**핵심 철학**:
> **"직군 색 없이 팩트를 최대한 상세하게 기록한다."**
> Notion은 포트폴리오가 아니라 **원장(元帳)**이다.
> 포트폴리오 작성은 이 원장을 기반으로 별도로 진행한다.

---

## 환경 요구사항

| 도구 | 용도 |
|------|------|
| **Notion MCP** | notion-fetch, notion-search, notion-create-pages, notion-update-page |
| **Filesystem** | 사용자 로컬 파일 읽기 (README.md, CLAUDE.md 등) |
| **Chrome 브라우저** | 웹앱 스크린샷 캡처 (선택적) |
| **bash_tool** | Claude 컴퓨터에서 파일 처리 |

### Claude Code v2.3.0 vs Web Edition v2.3.0

| 기능 | Claude Code | Web Edition |
|------|-------------|-------------|
| Notion CRUD | Python + Notion API | ✅ Notion MCP 도구 |
| 프로퍼티 자동 분석 | Python 스크립트 | ✅ LLM 직접 분석 |
| 스크린샷 캡처 | Playwright | ✅ Chrome 브라우저 도구 |
| 스크린샷 → Notion | Notion File Upload API | ❌ 수동 첨부 안내 |
| 터미널 UI | Catppuccin 렌더링 | ❌ 해당 없음 |

---

## 핵심 설정

### 데이터베이스 정보

```
data_source_id: ce6722a9-00b2-4d0e-8eda-190f4ce97cb6
database_url: https://www.notion.so/3249e5d70c6c4fbebe400ee3d8d2d4c7?v=02606e8cf18042bfb4fcee0a48732f7c
```

### 업데이트 날짜 형식

`YYYY.MM.DD` — 항상 오늘 날짜로 자동 갱신

---

## 프로젝트 타입 감지 (5-Type System)

직군이 아닌 **프로젝트 성격**으로 분류. 섹션 구성에만 사용:

| Type | Triggers | 강화할 섹션 | 글로우색상 |
|------|----------|------------|-----------|
| **1. Impact** | 성과 수치, KPI, A/B 테스트, 개선율 | Before/After 테이블, A/B Test, 비용·시간 절감 정량화 | teal / red |
| **2. Analysis** | 분석, EDA, 인사이트, 가설검증, 퍼널, 코호트 | 방법론, 데이터 출처, 가설-검증-결과, 핵심 발견 | teal |
| **3. Product** | 서비스, 앱, 기획, 출시, UX, 기능 | 기능 목록, 아키텍처, UX 플로우, 사용자 가치 | pink |
| **4. Learning** | 학습, Kaggle, 자격증, 스터디 | 학습 목표, Before/After 역량, 실무 적용 계획 | purple |
| **5. Automation** | 자동화, 봇, 파이프라인, 크롤링 | 워크플로우 다이어그램, 에러 처리, 효율화 수치 | amber |

**Default**: 수치 성과 있으면 Type 1, 기획/서비스면 Type 3, 자동화면 Type 5, 그 외 Type 2.

---

## 실행 워크플로우

### Step 1: 프로젝트 파일 수집

```
우선순위:
1. README.md (핵심)
2. CLAUDE.md (보조)
3. package.json / requirements.txt (기술스택)
4. .git/logs/HEAD (진행기간: 첫 커밋 ~ 마지막 커밋)
5. vercel.json / netlify.toml (배포 정보)
```

**도구**: `Filesystem:list_directory` → `Filesystem:read_text_file` → `Filesystem:search_files`

### Step 2: 기존 프로젝트 확인 + 포트폴리오 밸런스 체크

```
도구: Notion:notion-search
  query: "{프로젝트명 키워드}"
  data_source_url: "collection://ce6722a9-00b2-4d0e-8eda-190f4ce97cb6"
```

- 검색 결과 있음 → **업데이트** → notion-fetch로 기존 내용 조회
- 검색 결과 없음 → **신규 생성**

**포트폴리오 밸런스 체크** (신규 등록 시):
```
📊 포트폴리오 현황
✅ Type 분포: Impact 2개, Analysis 2개, Automation 1개
⚠️ Product(Type 3) 없음 — 기획/서비스 프로젝트 추가 검토
✅ Approach 필드: 4/5개 작성됨
⚠️ Challenge 미작성: 2개 (소급 보완 권장)
```

체크 항목: Type 분포 (최소 3개 타입), 글로우 색상 (3개+), PACRL 완성도

### Step 3: 프로퍼티 자동 분석 — PACRL Framework

#### 필수 프로퍼티 (16개)

| 프로퍼티 | 분석 방법 |
|----------|-----------|
| **프로젝트명** | README 제목 + 이모지 접두사 |
| **Problem** | "문제", "Pain Point", "배경" 섹션. 왜 이게 문제인가 (맥락 포함) |
| **Approach** | 왜 이 방법을 선택했는가. 대안 검토, 기술적 근거 (2-3문장) |
| **Solution** | "해결", "구현" 섹션. 어떻게 구현했는가. `<br>` 줄바꿈, 번호 매기기 |
| **Challenge** | 시행착오, A→B 피벗, 실패 케이스. 구현 전·중 마주한 어려움 |
| **Result** | **있는 수치 전부 기록** — 직군 필터 없이. 처리 시간, 정확도, 에러율, 전환율, 리텐션, 비용, 공수, 사용자 수 등 |
| **Learning** | 기술적 배움, 설계 패턴, 방법론 체득, 다음에 다르게 할 것 |
| **기술스택** | DB 등록 옵션에서 매칭 (아래 목록 참조) |
| **글로우색상** | 타입별 매핑 (위 표 참조) |
| **카테고리** | 프로젝트 성격 기반으로 자유롭게 |
| **한줄설명** | 핵심 한 문장 요약 |
| **상세제목** | 영문 부제목 |
| **Extra-Label** | 영어 대문자 섹션 제목 (아래 참조) |
| **Extra** | `**제목** — 설명` 형식 5-8개 항목 |
| **업데이트 날짜** | 오늘 날짜 YYYY.MM.DD |
| **진행기간** | Git 히스토리 또는 README에서 추출 |

> **PACRL 핵심 포인트**
> - **Approach + Challenge가 차별점이다.** 대부분의 프로젝트에 이 두 필드가 없다.
> - **Result는 있는 수치 전부 기록한다.** 나중에 포트폴리오 작성 시 직군별로 어떤 수치를 앞세울지 결정.
> - Problem → Solution → Result만 있으면 미완성이다.

#### Extra-Label 추천 (범용)

| Extra-Label | 사용 시점 |
|-------------|----------|
| **APPROACH & DECISION** | 왜 이 방법/기술을 선택했는가 (대안 비교) |
| **CHALLENGE & PIVOT** | 시행착오, A→B 피벗 상세 |
| **A/B TEST DESIGN** | A/B 테스트 수행 시 |
| **WORKFLOW DESIGN** | 자동화 흐름이 핵심일 때 |
| **TECH STACK DECISIONS** | 기술 선택 이유가 중요할 때 |
| **HYPOTHESIS TESTING FRAMEWORK** | 가설 검증 프로젝트 |
| **FEATURE SPEC** | 핵심 기능 상세 스펙 |
| **EFFICIENCY REPORT** | 자동화 전후 비교 데이터 |
| **SYSTEM ARCHITECTURE** | 여러 컴포넌트 연동 시 |
| **DATA DETAILS** | 데이터 규모/품질이 중요할 때 |
| **LEARNING JOURNEY** | 학습 과정 타임라인 |
| **REAL-WORLD APPLICATION** | 실무 적용 계획 |

#### 기술스택 (DB 등록 옵션)

**분석/데이터**:
Python, Pandas, NumPy, SQL, BigQuery, PostgreSQL, MySQL, Tableau, Power BI,
Looker Studio, Google Sheets, Matplotlib, Seaborn, Plotly, scikit-learn,
XGBoost, LightGBM, Prophet, ARIMA, scipy, statistics

**PA/프로덕트 분석**:
Amplitude, Mixpanel, Google Analytics (GA4), Firebase, Hotjar, Segment,
Braze, Appsflyer

**자동화/백엔드**:
LangChain, OpenAI API, FAISS, RAG, Streamlit, FastAPI, Flask, React,
Node.js, Playwright, Selenium, GitHub Actions, Vercel, Discord API,
Slack API, n8n Webhook, Apache Airflow, Docker, pytest

**PM/기획/BA**:
Figma, Jira, Confluence, Notion, Miro, Lucidchart, Power Automate,
Excel, Visio

**기타**:
Canvas API, Pillow, BeautifulSoup4, Supabase, PostgreSQL 17,
Remotion, TypeScript, JavaScript

> README에서 발견한 기술이 목록에 없으면 가장 가까운 것으로 매핑하거나 생략.

### Step 4: 콘텐츠 생성

#### 공통 필수 구조

```markdown
> 💡 **"핵심 성과/발견/제품을 한 줄로"**
>
> 부연 설명 한 줄

---

## 🎯 Performance Overview

(30초 스캔용 테이블 — 타입별로 다른 컬럼)

**Impact Summary**: 한 문장 요약

---

(타입별 권장 섹션 2-3개)

---

## 💡 Key Takeaways
## 🔗 Links
```

#### 타입별 권장 섹션 흐름

```
Type 1 (Impact):     Overview → Problem → Approach & Solution → Challenge → A/B Test / Result → Takeaways
Type 2 (Analysis):   Overview → Problem → Approach & Methodology → Key Findings → Challenge → Takeaways
Type 3 (Product):    Overview → Problem + Approach → Feature Showcase → Architecture → Challenge → Takeaways
Type 4 (Learning):   Overview → Learning Goal + Approach → What I Learned → Challenge → Before/After → Takeaways
Type 5 (Automation): Overview → Problem + Approach → Workflow Design → Challenge → Efficiency Gains → Takeaways
```

#### 섹션 순서 변형 (프로젝트간 차별화용)

| 전략 | 순서 |
|------|------|
| 기본 (추천) | Overview → Problem → Approach → Solution → Challenge → Takeaways |
| 성과 최우선 | Overview → Result → Approach → Details → Takeaways |
| 데모 최우선 | Overview → Feature → Approach → Architecture → Takeaways |
| 자동화 최우선 | Overview → Workflow → Approach → Efficiency → Takeaways |

#### Design Rules

- **섹션 제목**: Emoji + English (e.g., `🎯 Performance Overview`)
- **본문**: 한국어, 기술 용어는 영어 원문 유지
- **F-Pattern**: 성과/발견을 상위 50%에 배치
- **코드 블록**: 핵심 10-15줄 (최대 20줄), 주석 포함
- **Mermaid**: 3-5단계 간소화, 노드 15개 이하
- **수치**: **볼드** 처리

### Step 5: Notion 페이지 생성/업데이트

#### 신규 생성

```
도구: Notion:notion-create-pages
  parent: { data_source_id: "ce6722a9-00b2-4d0e-8eda-190f4ce97cb6" }
  pages: [{
    properties: {
      "프로젝트명": "📊 프로젝트 이름",
      "Problem": "...",
      "Approach": "왜 이 방법을 선택했는가...",
      "Solution": "...",
      "Challenge": "시행착오, 피벗 과정...",
      "Result": "있는 수치 전부 기록...",
      "Learning": "...",
      "기술스택": "[\"Python\", \"SQL\"]",
      "글로우색상": "teal",
      "카테고리": "데이터 분석",
      "한줄설명": "...",
      "상세제목": "...",
      "업데이트 날짜": "2026.03.30",
      "진행기간": "2026.01 ~ 2026.02",
      "Extra-Label": "APPROACH & DECISION",
      "Extra": "**선택 이유** — ...\n**대안 검토** — ..."
    },
    content: "... (타입별 마크다운 콘텐츠)"
  }]
```

#### 업데이트

```
도구: Notion:notion-update-page
  page_id: "기존 페이지 ID"
  command: "update_properties"
  properties: { ... 변경된 프로퍼티만 ... }
```

**Diff 프리뷰** (업데이트 시 필수):
```
📝 변경 사항 프리뷰
- [수정] Problem: 맥락 보강
- [추가] Approach: 대안 검토 내용 추가
- [추가] Challenge: 피벗 과정 추가
- [수정] Result: 있는 수치 전부 추가 기록
- [유지] Performance Overview (변경 없음)
- [수정] 업데이트 날짜: 2026.02.11 → 2026.03.30
진행할까요? (Y/N)
```

### Step 6: 스크린샷 (선택적)

Chrome 브라우저 도구가 사용 가능하고 프로젝트에 라이브 URL이 있는 경우:

1. `Claude in Chrome:navigate` → URL 접속
2. `Claude in Chrome:computer` → action: "screenshot"
3. 사용자에게 Notion 페이지에 수동 첨부 안내

**타입별 캡처 우선순위**:
- Type 3 (Product): **최우선** — 앱 스크린샷이 핵심
- Type 1 (Impact): 대시보드/차트 캡처
- Type 5 (Automation): 워크플로우 실행 결과

> ⚠️ Claude.ai에서는 스크린샷을 Notion에 직접 업로드할 수 없습니다.

---

## Metric Guidelines (수치 현실성)

**원칙**: 있는 수치 전부 기록, 직군 필터 없이

| 프로젝트 규모 | 수치 스케일 |
|-------------|-----------|
| 개인/사이드 | 수백~수천 건, 수십만 원, 수 시간 절약 |
| 팀/소규모 | 수천~수만 건, 수백만 원, 수십 시간 |
| 부서/중규모 | 수만~수십만 건, 수천만 원 |

**규칙**: 비율(%) 중심 / 보수적 추정 / 가정 명시
**금지**: 근거 없는 ROI 1,000%+ / 실제보다 부풀린 수치

---

## Quality Checklist

- ✅ Performance Overview가 최상단에 있는가?
- ✅ Key Takeaways가 상위 50%에 있는가?
- ✅ **Approach: 왜 이 방법인지 근거가 있는가?**
- ✅ **Challenge: 시행착오/피벗 과정이 있는가?**
- ✅ **Result: 있는 수치 전부 기록했는가? (직군 필터 없이)**
- ✅ 다른 프로젝트와 섹션 구조가 다른가?
- ✅ 수치가 실제 규모에 맞는가?
- ✅ 16개 properties 전부 채워졌는가?

---

## 결과 보고 형식

```
📋 프로젝트 업로드 결과

| 프로젝트 | 작업 | Type | 상태 | 변경 내용 |
|----------|------|------|------|----------|
| 📊 프로젝트 A | 업데이트 | Impact | ✅ | Approach/Challenge 필드 추가 |
| 🌿 프로젝트 B | 신규 | Product | ✅ | 전체 생성 |
| 🤖 프로젝트 C | 신규 | Automation | ✅ | 전체 생성 |
```

---

## 주의사항

1. **기술스택은 DB 등록 옵션만 사용** — 없으면 가장 가까운 것으로 매핑
2. **Solution은 `<br>` 줄바꿈 사용** — Notion rich_text 줄바꿈
3. **Extra 구분자는 `\|`** — Notion 텍스트에서 파이프 이스케이프
4. **업데이트 시 기존 콘텐츠 보존** — 프로퍼티만 변경이 기본, 콘텐츠는 사용자 확인 후
5. **메인 표시 / 순서는 건드리지 않음** — 사용자 직접 설정
6. **Approach는 "왜"에 집중** — 구현 방법(Solution)과 혼동 금지
7. **Challenge는 넓게 정의** — 구현 전 실패한 시도 + 구현 중 난관 모두 포함
8. **Result는 직군 필터 없이** — 모든 수치를 원장에 기록, 포트폴리오 작성 시 선택
