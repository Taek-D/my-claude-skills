# My Claude Skills

Custom Claude Code skills for personal productivity and automation.

## Skills

### notion-project-upload

**Version**: 1.5.0  
**Category**: Productivity

Upload projects to Notion with optimized portfolio templates and auto-captured screenshots. Automatically analyzes project type (business/exploratory/learning), applies recruiter-friendly templates, and captures portfolio-optimized screenshots.

**Features**:
- 🎯 Auto-detects project type (3 types)
- 🔄 Create new projects or update existing ones
- 📸 **Screenshot auto-capture** — smart capture based on project type & JD keywords (v1.5)
- 🖼️ **Notion File Upload API** — direct image upload, no external hosting (v1.5)
- 🎨 **Terminal renderer** — Catppuccin theme terminal output → image (v1.5)
- 🌐 **Web app auto-detection** — Streamlit/React/Flask auto-launch & capture (v1.5)
- ⚡ **Conditional file loading** — loads only relevant template (75% token savings) (v1.4)
- 📊 **Portfolio balance check** — type/stack/color distribution analysis (v1.4)
- 📝 **Update diff preview** — before/after comparison before committing (v1.4)
- 🎨 **Flexible section structure** — required + recommended + optional sections (v1.4)
- 📏 **Metric realism** — scale-appropriate numbers for 3-year DA level (v1.4)
- 🎨 Differentiation strategies to avoid template-y appearance (v1.3+)
- 👥 Collaboration & Impact section (v1.2+)
- 📊 Statistical Validation for analysis projects (v1.2+)
- 📁 Dataset section for data transparency (v1.1+)
- 📝 14 property fields auto-populated
- 🏷️ Tech stack tagging & glow color selection

**Templates**:
- Type 1: Business Impact (Before/After, ROI, metrics, collaboration, deployment)
- Type 2: Exploratory Analysis (EDA, findings, statistical validation, insights)
- Type 4: Learning Project (Kaggle, courses, practice, reflection)

**What's New in v1.4.0**:
- 📂 **File Structure Overhaul** — `templates.md` (2,390줄) → 6개 분리 파일 (타입별 템플릿 + 가이드)
- ⚡ **Conditional Loading** — 업로드 시 해당 타입 파일만 로딩 (토큰 75% 절감)
- 🔧 **Flexible Sections** — 필수+권장+선택 구조로 프로젝트별 차별화
- 📊 **Portfolio Balance Check** — 타입/스택/색상 분포 자동 분석
- 📝 **Update Diff Preview** — 변경사항 미리보기 후 확인
- 📏 **Metric Realism** — 3년차 DA 수준에 맞는 현실적 수치 가이드
- 🐛 **Bug Fixes** — Type 3 잔재, 중복 섹션, 코드블록 길이 모두 수정

**What's New in v1.3.2**:
- 🗑️ **Type 3 Removed** - Eliminated Technical Implementation type (backend/DevOps focused, not DA-appropriate)
- 🎯 **3-Type Structure** - Simplified portfolio to Type 1 (Business), Type 2 (Analysis), Type 4 (Learning)
- ✅ **Reduced Overlap** - Visualization & automation naturally integrated into all types
- 📊 **Clearer Categorization** - No more artificial separation of analysis vs technical aspects

**What's New in v1.3.1**:
- 📋 **Process Flow Integration** - 6-step frameworks for all project types showing clear methodology

**What's New in v1.3.0**:
- 🎨 **Differentiation Strategies Guide** - Concrete techniques to avoid cookie-cutter appearance
- 💰 **Business Impact Quantification** - ROI formulas, calculation templates, and real-world examples
- 🎓 **Type 4 Complete Redesign** - Learning projects now match Type 1/2 quality with Before/After, Journey, Real-world Application
- 📖 **Gold Standard Examples** - Complete example projects demonstrating all v1.3.0 features
- 📊 **Mermaid Diagram Guide** - 6 diagram types with project-specific recommendations and best practices
- 🎯 **Extra & Extra-Label Field Guide** - 15+ templates for project-specific details (A/B Test, Tech Spec, Hypothesis, etc.)
- 🔧 **Project-Specific Emphasis** - Different approaches for performance/efficiency/insight projects
- 📝 **Writing Style Variety** - Formal/Casual/Technical examples and guidelines
- 🎭 **Visual Differentiation** - Table/chart/emoji style variations
- ✅ **Comprehensive Checklists** - 6-point differentiation + 7-point impact + 7-point diagram + 7-point Extra quality

**What's New in v1.2**:
- ✨ **Section Reordering** - Key Takeaways & Collaboration moved earlier for better recruiter scanning (top 50%)
- ✨ **Collaboration & Impact** - Show teamwork, stakeholder management
- 📊 **Statistical Validation** - Hypothesis testing, p-values, effect sizes
- 🚀 **Deployment & Usage** - Production status, real-world impact
- 🔄 **Update Functionality** - Modify existing projects with new triggers (업데이트, 수정, edit, modify)
- 💻 **Better Code Blocks** - 15-20 lines (up from 10)
- 🎯 **Business Context** - Always explain "why this matters"

## Installation

### Via Claude Code Marketplace (Recommended)

```bash
# In Claude Code CLI
/install-skill https://github.com/Taek-D/my-claude-skills
```

### Manual Installation

```bash
# Clone repository
git clone https://github.com/Taek-D/my-claude-skills.git

# Copy to Claude Code skills directory
cp -r my-claude-skills/skills/* ~/.claude/skills/
```

---

## 📚 Examples

**실전 예시 프로젝트** - v1.3.0의 모든 기능을 완벽히 적용한 골드 스탠다드

각 예시는 다음을 포함합니다:
- ✅ Differentiation 전략 적용 (각 프로젝트마다 다른 강조점/스타일)
- ✅ Business Impact Quantification (ROI 계산 공식 적용)
- ✅ 정량적 Before/After 비교
- ✅ Statistical Validation (Type 2)
- ✅ 코드 블록 (15-20줄, 주석 포함)
- ✅ Mermaid 다이어그램
- ✅ Collaboration & Impact 섹션
- ✅ Deployment & Usage (Type 1/3)

### Type 1: Business Impact Project
**[배달 시간 예측 모델 개선으로 고객 만족도 향상](examples/type1-delivery-prediction.md)**
- XGBoost 기반 배달 시간 예측, MAE 15.2분→6.8분 (-55%)
- 월 환불 비용 ₩1.1M 절감, CSAT 3.8→4.3
- Redis 캐싱, Feature Engineering, A/B 테스트

### Type 2: Exploratory/Analysis Project
**[구독 서비스 이탈 패턴 분석으로 리텐션 전략 수립](examples/type2-churn-analysis.md)**
- 2만 사용자 코호트 분석, 3가지 핵심 이탈 요인 발견
- 30일 리텐션 62%→70% (+8%p), 연 ₩28.8M 수익 보전
- Hypothesis Testing, Kaplan-Meier, Logistic Regression

### Type 4: Learning Project
**[Kaggle Tabular Playground Series - Time Series Forecasting 학습](examples/type4-kaggle-learning.md)**
- Prophet, XGBoost, LSTM 앙상블, RMSE 0.237
- 3,200명 중 상위 12% (384등), Bronze Medal
- 87시간 투자, 실무 적용 계획 포함

---

## Usage

In any Claude conversation:

**Creating New Projects:**
```
"노션에 업로드해줘"
"Upload this project to Notion"
"프로젝트 포트폴리오 업로드"
```

**Updating Existing Projects:**
```
"CohortIQ 프로젝트 업데이트해줘"
"이 프로젝트 수정해서 노션에 올려줘"
"Update my chatbot project in Notion"
"프로젝트 리뉴얼해줘"
```

The skill will:
1. Analyze your project (or fetch existing one)
2. Select appropriate template
3. Generate optimized content
4. Upload/update in your Notion database

## Configuration

Set your Notion database ID in user memories or provide it when uploading:

```
Database ID: ce6722a9-00b2-4d0e-8eda-190f4ce97cb6
```

## Version History

### v1.2.0 (2026.02.11) - Major Improvements
- ✨ Added **Collaboration & Impact** section (Type 1/2/3)
  - Show stakeholder interaction
  - Communication methods
  - Real-world usage and feedback
- 📊 Added **Statistical Validation** section (Type 2)
  - Hypothesis testing (H0/H1)
  - p-values, effect sizes
  - Confidence intervals
- 🚀 Added **Deployment & Usage** section (Type 1/3)
  - Production status
  - Real usage metrics
  - User feedback
- 💻 Increased code block limit: 10 → 15-20 lines
- 🎯 Enhanced business context requirement
- 🔍 Removed duplicate "데이터 특성" in Type 2
- 📋 Updated Quality Checklist

**Why v1.2?** Based on feedback from recruiters and data professionals:
- Show teamwork ability (not just solo projects)
- Demonstrate statistical rigor (not just charts)
- Prove real-world impact (not just toy projects)
- Less template-y, more personality

### v1.1.0 (2026.02.11)
- ✨ Added Dataset section to Type 1/2/3 templates
- 📊 Improved portfolio credibility with data transparency
- 🔍 Quality checklist updated with Dataset verification
- 📝 Version info added to SKILL.md

### v1.0.0 (2026.02.10)
- 🎉 Initial release
- 4 project type templates
- 14 property auto-population
- Emoji + English sections
- Tech stack tagging
- Glow color selection

## Roadmap

**v1.3.0 (Planned)**
- [ ] Multi-language support (English templates)
- [ ] Custom template creation
- [ ] Batch upload support

## Contributing

Feel free to submit issues or pull requests!

## License

MIT
