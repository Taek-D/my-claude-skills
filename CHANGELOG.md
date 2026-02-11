# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

[1.1.0]: https://github.com/Taek-D/my-claude-skills/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Taek-D/my-claude-skills/releases/tag/v1.0.0
