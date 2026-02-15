# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.5.0] - 2026-02-15

### Added

#### Screenshot Auto-Capture
- **Smart capture strategy engine** — 프로젝트 유형(dashboard/automation/data_analysis/webapp/ml_ai)별 자동 캡처 전략
  - Business: 2~4장 (메인 + 임팩트 + 상세)
  - Exploratory: 2~3장 (핵심 발견 + 프로세스)
  - Learning: 1~2장 (실행 결과)
- **JD keyword priority boost** — JD 키워드 매칭 시 관련 캡처 우선순위 자동 상향
- **Quantitative impact detection** — Impact 텍스트에서 %, $, 시간, 건수 등 자동 감지 → Before/After 캡처 추가

#### Notion File Upload API Integration
- **3-Step upload flow** — Create file upload → Send binary → Attach image block
- **No external hosting** — GitHub/Imgur/S3 불필요, Notion API 토큰만으로 동작
- **Batch upload** — 여러 이미지 순차 업로드 + 에러 핸들링
- **Page cover auto-set** — 메인 스크린샷을 페이지 커버로 자동 설정
- **Manual upload support** — 경로 지정으로 수동 이미지 업로드도 지원

#### Web App Auto-Detection & Capture
- **Framework detection** — Streamlit(8501), React(3000), Flask(5000), Gradio(7860), Dash(8050)
- **Auto launch & capture** — 앱 자동 실행 → 로딩 대기 → Playwright viewport/element 캡처
- **Process management** — 백그라운드 앱 실행/종료 자동 관리

#### Terminal Renderer (Catppuccin Theme)
- **Pillow-based rendering** — 외부 브라우저 의존 없이 터미널 이미지 생성
- **Auto syntax highlighting** — `$` 프롬프트(green), ✅ 성공(green), ❌ 에러(red), 수치(peach)
- **Catppuccin Mocha palette** — 다크 테마 터미널 스타일
- **Command execution** — 명령 실행 → 결과 캡처 one-shot 지원
- **Line truncation** — 50줄 초과 시 중간 생략 처리

#### Caption System
- **Template-based captions** — `{프로젝트명} — {캡처 대상} {핵심 수치}` 형식
- **Portfolio-optimized** — 면접관 관점 캡션 (BAD: "screenshot1.png" → GOOD: "월별 비용 추이 — 38% 절감")

#### Workflow Extension
- **Phase 2 (NEW)**: 캡처 전략 수립 (프로젝트 분석 직후)
- **Phase 3 (NEW)**: 캡처 실행 (웹앱 감지/터미널/Playwright)
- **Demo section**: Solution과 Technical 사이에 이미지 섹션 자동 삽입

### Changed
- **SKILL.md description** — 스크린샷 캡처 기능 반영
- **Upload workflow** — 4단계 → 5단계 (Screenshot Capture 단계 추가)
- **Version**: 1.4.0 → 1.5.0

### New Files
```
screenshot-capture/
├── __init__.py              (37 lines)
├── capture_manager.py       (577 lines) — 메인 오케스트레이터
├── strategies.py            (571 lines) — 캡처 전략 엔진
├── terminal_renderer.py     (495 lines) — 터미널 → 이미지
└── notion_file_upload.py    (388 lines) — Notion File Upload API
```
Total: 2,068 lines added

### Dependencies
- `Pillow` — 터미널 이미지 렌더링 (필수)
- `playwright` — 웹앱 캡처 (선택)

## [1.4.0] - 2026-02-14

### Changed

#### File Structure Overhaul (Token Optimization)
- **Removed** `templates.md` single file (2,390 lines)
- **Split into** type-specific templates: `type1-template.md`, `type2-template.md`, `type4-template.md` (~170 lines each)
- **Added** `references/guides/` directory with 3 focused guides:
  - `mermaid-guide.md` — Condensed diagram guide (6 types, best practices)
  - `extra-label-guide.md` — Extra/Extra-Label templates by type
  - `differentiation-guide.md` — Strategies + impact quantification formulas
- **Impact**: ~75% token reduction per upload (load only relevant type)

#### Flexible Section Structure
- **Required**: Performance Overview, Key Takeaways, Links
- **Recommended** (pick 2-3): Problem & Root Cause, Data & Methodology, Findings, Collaboration, Statistical Validation, Deployment
- **Optional**: A/B Test, Error Analysis, Real-world Application
- **Impact**: Each project gets unique structure instead of cookie-cutter layout

#### Metric Realism Adjustments
- Removed unrealistic metrics: ROI 1,422%, $600K/year, 120K users
- Applied scale guidelines: 개인/사이드 (수백~수천 건, 수십만 원), 팀 (수천~수만 건, 수백만 원)
- Updated all 3 examples with 3년차 data analyst-appropriate numbers
- Currency changed: USD → KRW where appropriate

### Added

#### Portfolio Balance Check (Pre-upload)
- Auto-checks Type distribution (Type 1/2/4 각 최소 1개 권장)
- Tech stack coverage (SQL, Python, Tableau 누락 확인)
- Glow color diversity (3개 이상 권장)
- Section structure duplication warning (80%+ 동일 시)
- Metric scale consistency

#### Update Diff Preview
- Shows before/after changes before committing updates
- Format: `[수정] Problem: "old" → "new"`, `[추가] Section`, `[유지] Section`
- User confirmation required (Y/N) before proceeding

#### Language Rules Standardization
- Section titles: Emoji + English (글로벌 가독성)
- Body text: 한국어 (타겟 채용시장)
- Extra-Label: 영어 대문자 (카드 UI)
- Technical terms: English original (XGBoost, A/B Test)

### Fixed

#### P0 Bugs
- **Type 3 remnants removed** — All references to deleted Type 3 cleaned from guides
- **Duplicate sections fixed** — type1 example had duplicate Collaboration & Links sections
- **Code block lengths** — All blocks trimmed to 15-20 lines max (was up to 57 lines)

## [1.3.2] - 2026-02-11

### Removed

#### Type 3 (Technical Implementation) Eliminated
- **Type 3 template and examples completely removed** from skill
  - Deleted `examples/type3-api-optimization.md`
  - Removed Type 3 section from `templates.md` (580-948 lines)
  - Updated all references in `SKILL.md` to 3-type structure
- **Rationale**: 
  - Type 3 (Technical Implementation) was backend/DevOps focused, not appropriate for data analyst portfolios
  - Visualization and automation are naturally integrated into all project types, making Type 3 redundant
  - User portfolio analysis showed existing projects already blend analysis + automation + visualization
  - Removing Type 3 prevents artificial categorization and content duplication

### Changed
- **Portfolio structure**: 4 types → **3 types** (Type 1, Type 2, Type 4)
- **Type classification logic**: Default changed from "Type 3" to "Type 2" when no clear match
- **Dataset section**: Updated requirement from "Type 1/2 required, Type 3 optional" → "Type 1/2 required, Type 4 optional"
- **Quality checklist**: Removed all Type 3 references
- **Template version**: Updated to 1.3.2

**Impact**: Clearer portfolio structure, reduced overlap, better alignment with data analyst job requirements

---

## [1.3.1] - 2026-02-11

### Added

#### Process Flow Integration Across All Templates
- **6-step process frameworks** added to all 4 project types
  - **Type 1 (Business Impact)**: Solution Process (Problem Discovery → Solution Design → Implementation → Validation → Deployment → Impact Measurement)
  - **Type 2 (Data Analysis)**: Analysis Process (Problem Definition → Data Collection → Hypothesis & Analysis → Key Findings → Recommendations & Impact → A/B Test & Validation)
  - **Type 3 (Technical)**: Optimization Process (Baseline Measurement → Bottleneck Analysis → Optimization Strategy → Implementation → Performance Validation → Monitoring & Maintenance)
  - **Type 4 (Learning)**: Learning Process (Learning Goal → Theory & Foundation → Hands-on Practice → Competition/Project → Reflection & Learning → Real-world Application)
- **Performance Overview table** consistently positioned at top for 30-second scan
- **Structured methodology display** helps hiring managers quickly understand approach

**Rationale**: User feedback "문제정의 - 데이터 분석 - 결과 도출" process valuable for Type 2 → extended to all types with type-specific frameworks

### Changed
- **SKILL.md** - Quality Checklist updated to include Process Flow verification
- **All example files** (type1-type4) updated with 6-step process structure
- **Section order** refined: Performance Overview → Process Flow → Dataset → Key Takeaways → Collaboration → Technical Details

**Impact**: Clearer methodology presentation, easier for recruiters to assess analytical/technical approach

---

## [1.3.0] - 2026-02-11

### Added

#### Differentiation Strategies Guide
- **Comprehensive differentiation section** in templates.md to address "too template-y" feedback
- **Project-specific emphasis** - Different strategies for performance/efficiency/insight projects
- **Section order flexibility** - Guidelines for reordering when emphasizing specific aspects
- **Writing style variety** - Formal/Casual/Technical style examples
- **Visual differentiation** - Different table/chart/emoji styles per project
- **Differentiation checklist** - 6-point check before uploading

**Rationale**: Critical recruiter feedback "all projects look identical" → need concrete strategies

#### Business Impact Quantification Guide
- **5 quantification formulas** - Time savings, efficiency, conversion, cost reduction, error reduction
- **ROI calculation templates** - Step-by-step examples with real numbers
- **Impact table templates** - 3 different table formats for different project types
- **Quantification checklist** - 7-point verification before claiming impact
- **Best practices** - How to estimate when data is unavailable, how to convert intangible to tangible value

**Rationale**: "Business context explained" was too vague → need concrete formulas and examples

#### Type 4 (Learning Project) Complete Redesign
- **Goal & Context section** - Why this learning matters for career/business
- **Learning Journey** - Timeline table with phases, focus, duration, milestones
- **Before & After comparison** - Quantitative skill level improvement
- **Structured Key Learnings** - What/How/Impact for each concept with code examples
- **Results & Achievements split** - Quantitative outcomes table + Qualitative achievements
- **Real-world Application** - Concrete plans with expected impact ($, %, timeline)
- **Key Takeaways enhanced** - Technical/Learning Process/Career Growth insights
- **Community Impact section** - Blog posts, open-source contributions, study groups

**Rationale**: Type 4 was v1.1.0 level while Type 1/2/3 at v1.2.0+ → bring to same quality standard

#### Example Projects (4 Gold Standard Examples)
- **Type 1 Example**: Delivery Time Prediction - XGBoost model, MAE -56%, $600K annual revenue
- **Type 2 Example**: Churn Analysis - 120K users, hypothesis testing, +8%p retention
- **Type 3 Example**: API Optimization - Response time -84%, $47K cost savings
- **Type 4 Example**: Kaggle Time Series - Top 8%, Bronze Medal, real-world application plan
- All examples demonstrate differentiation strategies, impact quantification, and v1.3.0 features

**Rationale**: Users requested concrete examples showing how to apply all guidelines → 4 complete, production-quality examples

#### Mermaid Diagram Guide (Comprehensive Visualization Guide)
- **6 Diagram Types with Examples**: Flowchart, Sequence, Graph, Gantt, State, ER diagrams
- **Project-Type Recommendations**: Type 1/2/3/4별 최적 다이어그램 조합 제안
- **Before/After Visualization**: 아키텍처 개선 시각화 기법 (색상, 레이블)
- **Best Practices**: DO/DON'T 예시, 실전 팁 4가지
- **Practical Tips**: "한 다이어그램 = 한 메시지", 성과 수치 포함, 복잡도 관리
- **Tools & Resources**: Mermaid Live Editor, VS Code Extension, 색상 팔레트
- **Checklist**: 7-point diagram quality checklist

**Rationale**: Visual storytelling is critical for portfolio impact → comprehensive guide for effective diagrams

#### Extra & Extra-Label Field Guide (Comprehensive Detail Section Guide)
- **15+ Extra-Label Templates**: A/B Test Design, Tech Spec, Hypothesis Testing, Data Details, Performance Optimization, Deployment Strategy, Learning Journey, Before/After Skills, Real-world Application, Experiment Design, etc.
- **4 Complete Examples**: One for each project type (Type 1/2/3/4) with full Extra content
- **Format Specification**: `**제목** — 설명` markdown structure with bold titles
- **Project-Type Recommendations**: Best Extra-Labels for each project type
- **Best Practices**: DO/DON'T examples, quantitative criteria, avoiding duplication with main content
- **Quality Checklist**: 7-point Extra/Extra-Label quality checklist

**Rationale**: Extra/Extra-Label fields allow project-specific details that don't fit standard templates → comprehensive guide ensures effective use

## [1.2.0] - 2026-02-11

### Added

#### Section Reordering (Type 1/2/3)
- Moved **Key Takeaways** earlier (after Dataset, before technical details)
- Moved **Collaboration** section earlier (after Key Takeaways)
- **Rationale**: Recruiters read top 50% → learning ability and teamwork visible earlier
- **Type 1**: Data & Metrics → Dataset → Key Takeaways → Collaboration → Problem & Solution → Technical → Deployment
- **Type 2**: Key Findings → Dataset → Key Takeaways → Collaboration → Statistical Validation → Analysis → Results
- **Type 3**: Project Goal → Dataset → Key Takeaways → Collaboration → Technical → Achievements → Deployment

#### Update/Modify Functionality
- **Update existing projects** - Fetch and modify existing Notion projects
- **Merge content** - Intelligently merge new content with existing content
- **Preserve data** - Keep existing data while updating specific sections
- **Triggers** - Added update/modify/edit/갱신 triggers for better UX

#### Collaboration & Impact Section (Type 1/2/3)
- **Stakeholders** - Document who you worked with (PM, marketing, engineering)
- **Communication** - How insights were shared with non-technical teams
- **Real-world Usage** - Actual usage stats, user feedback, business impact

#### Statistical Validation Section (Type 2)
- **Hypothesis** - H0 and H1 clearly stated
- **Statistical Test** - Test type, p-values, interpretation
- **Effect Size & CI** - Cohen's d, confidence intervals, practical significance

#### Deployment & Usage Section (Type 1/3)
- **Production Status** - Deployment environment, CI/CD, monitoring
- **Real Impact** - Work efficiency improvements, decision-making impact
- **Monitoring** - Performance tracking methods

#### Enhanced Content Requirements
- Business context requirement for all types - always explain "why this matters"
- Real-world usage examples - show actual usage, not just potential
- Personality differentiation - avoid generic template filling

### Changed

#### Code Block Improvements
- Increased limit from 10 lines to **15-20 lines**
- Allow meaningful pseudo-code or actual implementation
- Focus on core logic with proper comments

#### Type 2 Template Restructure
- **Removed** duplicate "데이터 특성" table from Key Findings section
- **Consolidated** data information into Dataset section only
- Clearer separation between findings and data description

#### Section Reordering (Type 1)
- Moved **Key Takeaways** earlier (after Dataset)
- Recruiters see learning ability in first 50% of page
- Better F-pattern readability

#### Mermaid Diagrams
- Increased flexibility: 5-7 steps allowed (up from 3-5)
- Focus on core flow, not oversimplification

#### Quality Checklist
- Added checks for Collaboration section
- Added checks for Statistical Validation (Type 2)
- Added checks for Deployment & Usage (Type 1/3)
- Added business context verification
- Added differentiation checks (avoid template-y content)

### Improved

#### Recruiter Readability
- **Teamwork Evidence** - Addresses "can this person work in a team?"
- **Statistical Rigor** - Shows analytical depth, not just chart generation
- **Real Impact** - Proves practical value, not just toy projects
- **Business Savvy** - Demonstrates understanding of "why" not just "how"

#### Expert Credibility
- Hypothesis testing reduces "did they just run random analyses?" suspicion
- Effect sizes and CIs show understanding of practical significance
- Preprocessing details demonstrate data quality awareness
- Deployment sections prove production-ready skills

### Fixed
- Removed redundant data description in Type 2
- Clarified when Dataset section is optional vs required
- Better guidance on hypothesis formulation

## [1.1.0] - 2026-02-11

### Added
- **Dataset Section** to Type 1, Type 2, and Type 3 templates
  - Type 1 (Business Impact): Dataset section after "Data & Metrics"
    - Data source and acquisition method
    - Data scale table (count, period, variables)
    - Variable composition
    - Data characteristics and preprocessing (optional)
  - Type 2 (Exploratory Analysis): Dataset section after "Key Findings"
    - Data source
    - Data scale (count, variables, collection period)
    - Variable composition
    - Preprocessing steps (missing values, outliers, derived variables)
  - Type 3 (Technical Implementation): Optional Dataset section after "Project Goal"
    - Data source and generation method
    - Data scale
    - Variable composition
    - Technical characteristics (real-time/batch, validation process)
  - Type 4 (Learning Project): No Dataset section (less relevant for learning projects)

### Changed
- Updated Quality Checklist to include Dataset section verification
  - "✅ Dataset section present (Type 1/2 required, Type 3 optional)"
- Enhanced template focus descriptions in Project Type Detection table
  - Type 1: Added "Dataset section"
  - Type 2: Added "Dataset section"
  - Type 3: Added "Dataset (optional)"
- Added Dataset section to Design Rules
- Updated version numbers in all configuration files
  - marketplace.json: 1.0.0 → 1.1.0
  - plugin.json: 1.0.0 → 1.1.0
  - SKILL.md: Added version badge "1.1.0"

### Improved
- **Portfolio Credibility**: Dataset transparency builds recruiter trust
- **Reproducibility**: Clear data provenance enables verification
- **Technical Depth**: Demonstrates data handling and preprocessing expertise
- **Professionalism**: Shows attention to detail and data governance awareness

## [1.0.0] - 2026-02-10

### Added
- Initial release of notion-project-upload skill
- 4 project type templates (Business Impact, Exploratory Analysis, Technical Implementation, Learning Project)
- Auto-detection of project type based on content analysis
- 14 property fields with automatic population
  - Core Analysis: Problem, Solution, Impact, Learning
  - Metadata: 프로젝트명, 상세제목, 한줄설명, 기술스택, 카테고리, 글로우색상
  - Extra Fields: Extra-Label, Extra
  - Auto-Generated: 업데이트 날짜
- Emoji + English section titles
- Minimal toggle block design
- Hybrid bullet formatting
- Tech stack tagging system
- Glow color selection (teal, amber, red, purple, pink)
- Quality checklist for pre-upload verification
- Recruiter-optimized templates (2-3 min scan time)
- F-Pattern visual hierarchy (성과 우선)

### Design Principles
- Before/After tables for Business Impact projects
- Code blocks limited to <=10 lines with comments
- Mermaid diagrams simplified to 3-5 steps
- Quantitative metrics always in **bold**
- Templates focused on recruiter readability

## Scoring Comparison

### v1.0.0 Score: 5.3/10
- Readability: 8/10
- Credibility: 6/10
- Design: 7/10
- **Differentiation: 4/10** ⚠️
- **Collaboration: 2/10** ⚠️
- Technical Depth: 5/10
- Business Context: 5/10

### v1.1.0 Score: 6.2/10
- Readability: 8/10
- **Credibility: 7/10** ✅ (Dataset added)
- Design: 7/10
- Differentiation: 4/10
- Collaboration: 2/10
- Technical Depth: 5/10
- Business Context: 5/10

### v1.2.0 Score: 7.8/10 (Target)
- Readability: 8.5/10
- **Credibility: 8/10** ✅ (Statistical validation)
- Design: 7.5/10
- **Differentiation: 7/10** ✅ (Business context, personality)
- **Collaboration: 7/10** ✅ (Stakeholders, communication)
- **Technical Depth: 7/10** ✅ (15-20 line code, deployment)
- **Business Context: 8/10** ✅ (Real impact, usage)

## Migration Guide

### From v1.1 to v1.2

#### New Required Sections
1. **Collaboration & Impact** (Type 1/2/3)
   - Add after Key Takeaways
   - Include stakeholders, communication, real usage

2. **Statistical Validation** (Type 2 only)
   - Add after Dataset section
   - Include hypothesis, test results, effect sizes

3. **Deployment & Usage** (Type 1/3 if applicable)
   - Add after Technical Deep Dive
   - Include production status, real metrics

#### Updated Guidelines
- Code blocks: Now 15-20 lines (was 10)
- Mermaid: Now 5-7 steps (was 3-5)
- Business context: Always explain "why" (new requirement)

#### Removed Duplicates
- Type 2: Delete "데이터 특성" table from Key Findings
- Keep only Dataset section

[1.2.0]: https://github.com/Taek-D/my-claude-skills/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/Taek-D/my-claude-skills/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Taek-D/my-claude-skills/releases/tag/v1.0.0
