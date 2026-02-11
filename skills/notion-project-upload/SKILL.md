---
name: notion-project-upload
description: Upload projects to Notion with optimized portfolio templates. Automatically analyzes project type (business/exploratory/technical/learning) and applies the appropriate template with emoji+English sections, minimal toggles, and hybrid bullet formatting. Handles 14 property fields including Problem/Solution/Impact/Learning, tech stack tagging, glow colors, and auto-updated dates. Use when user asks to upload a project to Notion, update a Notion portfolio entry, or create a recruiter-friendly project page. Triggers include "노션에 업로드", "노션 업로드", "포트폴리오 업로드", "프로젝트 업로드", "notion upload", "portfolio upload", "리뉴얼", "renewal".
---

# Notion Project Upload

Upload projects to Notion portfolio database with optimized, recruiter-friendly templates.

**Version**: 1.2.0

## Database Configuration

- **Data Source ID**: `ce6722a9-00b2-4d0e-8eda-190f4ce97cb6`
- **Database URL**: https://www.notion.so/3249e5d70c6c4fbebe400ee3d8d2d4c7

## Workflow

1. **Analyze** project content and detect type
2. **Select** template from [references/templates.md](references/templates.md)
3. **Generate** markdown content following template
4. **Populate** all 14 properties
5. **Quality check** before upload
6. **Upload** to Notion DB

## Project Type Detection

Analyze content and classify into one type:

| Type | Triggers | Template Focus |
|------|----------|---------------|
| **1. Business Impact** | 매출, ROI, KPI, conversion, A/B 테스트 | Before/After tables, metrics in **bold**, Dataset, Collaboration & Deployment |
| **2. Exploratory Analysis** | 분석, EDA, 인사이트, 상관관계, 패턴 | Finding-oriented, Dataset, Statistical Validation, charts/tables |
| **3. Technical Implementation** | 챗봇, 크롤러, 자동화, API, 시스템, 개발 | Code blocks (15-20 lines), Mermaid diagrams, Deployment |
| **4. Learning Project** | Kaggle, 학습, 연습, 튜토리얼, 강의 | Learning-focused, ranking/score, reflection |

**Default**: If no clear match, check for quantitative metrics -> Type 1, otherwise -> Type 3.

For full templates, read [references/templates.md](references/templates.md).

## Design Rules

- **Section titles**: Emoji + English (e.g., `🎯 Project Goal`)
- **Toggle blocks**: Minimize. Show goals/achievements/core code. Toggle only for 100+ line code or supplementary content
- **Bullets**: Hybrid -- bullets for lists/goals/metrics, paragraphs for background/reflection, tables for numbers/comparisons (preferred)
- **Emojis**: Section headings only, minimize in body
- **Code blocks**: Core logic, 15-20 lines with comments (increased from 10 lines)
- **Mermaid diagrams**: 5-7 steps OK, focus on core flow
- **Quantitative metrics**: Always **bold**
- **Dataset section**: Include for data-based projects (Type 1/2 required, Type 3 optional)
- **Collaboration**: Show stakeholder interaction, communication methods (Type 1/2/3)
- **Statistical rigor**: Include hypothesis, p-values, effect size (Type 2)
- **Business context**: Always explain "why this matters" (All types)

## Properties (14 Fields)

### Core Analysis
| Property | Description |
|----------|-------------|
| **Problem** | 문제 정의 (2-3문장, 비즈니스 맥락 포함) |
| **Solution** | 해결 방법 (번호 매기기) |
| **Impact** | 성과 (정량/정성) |
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
| **Extra-Label** | 섹션 제목 (e.g., "A/B TEST DESIGN", "TECH SPEC", "STATISTICAL TEST") |
| **Extra** | **제목** -- 설명 형식 (마크다운 볼드) |

### Auto-Generated
| Property | Format |
|----------|--------|
| **업데이트 날짜** | YYYY.MM.DD (오늘 날짜 자동) |

## Tech Stack Tags

Python, Pandas, NumPy, Matplotlib, Seaborn, Tableau, Power BI, SQL, PostgreSQL, LangChain, OpenAI API, FAISS, RAG, Streamlit, Flask, FastAPI, Playwright, Selenium, JavaScript, React, Node.js, Google Sheets, Discord API, GitHub Actions, Vercel

## Quality Checklist

Before uploading, verify:

**Structure & Design**
- ✅ Section titles are emoji + English
- ✅ Toggle blocks minimized
- ✅ Code blocks 15-20 lines (not 10)
- ✅ Quantitative metrics in **bold**
- ✅ Mermaid diagrams clear (5-7 steps OK)

**Content Completeness**
- ✅ Before/After table present (Type 1 only)
- ✅ Dataset section present (Type 1/2 required, Type 3 optional)
- ✅ Statistical Validation present (Type 2 only: hypothesis, p-value, effect size)
- ✅ Collaboration & Impact section (Type 1/2/3)
- ✅ Deployment & Usage section (Type 1/3 if applicable)
- ✅ Business context explained ("why this matters")

**Properties**
- ✅ All 14 properties filled
- ✅ Date in YYYY.MM.DD format
- ✅ Problem includes business context
- ✅ Impact is quantitative + qualitative
- ✅ Learning is specific and actionable

**Differentiation**
- ✅ Not generic template content
- ✅ Project personality visible
- ✅ Real-world usage/feedback included (if applicable)

## Version History

- **v1.2.0** (2026.02.11): Major improvements based on recruiter & expert feedback
  - Added Collaboration & Impact section (Type 1/2/3)
  - Added Statistical Validation section (Type 2)
  - Added Deployment & Usage section (Type 1/3)
  - Removed duplicate "데이터 특성" in Type 2
  - Increased code block limit: 10 → 15-20 lines
  - Enhanced business context requirement
  - Updated Quality Checklist
- **v1.1.0** (2026.02.11): Added Dataset section to Type 1/2/3 templates for improved portfolio credibility
- **v1.0.0** (2026.02.10): Initial release

## Notes

- Templates optimized for **recruiter readability** (2-3 min scan time)
- Follow **F-Pattern** visual hierarchy (성과 우선, Scannable)
- **Dataset transparency** builds trust with recruiters (v1.1+)
- **Collaboration evidence** shows teamwork ability (v1.2+)
- **Statistical rigor** demonstrates analytical depth (v1.2+)
- Don't force fit -- if metrics don't exist, use alternatives
- Be honest -- 없는 걸 억지로 만들지 않기
- Show personality -- not just template filling
