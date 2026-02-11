# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2026-02-11

### Added

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
