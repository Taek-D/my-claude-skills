# notion-project-upload

> A Claude skill to upload and update projects in a Notion master record database — records all project facts in detail using the **PACRL framework**, job-role agnostic.

[![Version](https://img.shields.io/badge/version-2.3.0-blue)](https://github.com/Taek-D/my-claude-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Pro Required](https://img.shields.io/badge/Claude-Pro%20%2F%20Max%20%2F%20Team-blueviolet)](https://claude.ai)

---

## Concept: Notion as a Master Project Record DB

이 스킬의 핵심 철학은 하나다.

> **"직군 색 없이 팩트를 최대한 상세하게 기록한다."**
> 나중에 어떤 직무 포트폴리오를 만들어도 여기서 꺼내 쓸 수 있어야 한다.

Notion은 포트폴리오가 아니라 **원장(元帳)**이다. 포트폴리오 작성은 이 원장을 기반으로 별도로 진행한다.

---

## Features

- 🗂️ **Project record DB** — 직군 무관하게 프로젝트 팩트를 완전하게 보존
- 🔄 **Create or update** — 신규 업로드 + 기존 페이지 수정 (Diff 프리뷰 포함)
- 📋 **PACRL framework** — Problem / Approach / Solution / Challenge / Result / Learning
- 🔍 **5 project types** — 섹션 구성 최적화용 (Impact / Analysis / Product / Learning / Automation)
- 📊 **Portfolio balance check** — 타입 분포 + PACRL 완성도 자동 체크
- 📸 **Screenshot auto-capture** — 웹앱/터미널 캡처 → Notion 직접 업로드
- 📝 **16 property fields** — 자동 추출 및 작성
- 🏷️ **Broad tech stack tags** — DA / PA / PM / BA / 기획 전 직군 도구 포함

---

## PACRL Framework

모든 프로젝트는 6단계 서술 구조로 기록된다:

| 필드 | 핵심 질문 |
|------|----------|
| **Problem** | 왜 이게 문제였는가? 어떤 맥락에서? |
| **Approach** | 왜 이 방법인가? 검토했던 대안은? |
| **Solution** | 무엇을 어떻게 만들었는가? |
| **Challenge** | 어떤 어려움이 있었고 어떻게 넘겼는가? |
| **Result** | 수치로 무엇이 달라졌는가? (있는 수치 전부) |
| **Learning** | 이 경험에서 무엇을 배웠는가? |

> **Approach + Challenge가 핵심이다.**
> 대부분의 포트폴리오는 Problem → Solution → Result만 있다.
> 이 두 필드를 채울 때 어떤 직무 포트폴리오를 만들어도 강해진다.

---

## Prerequisites

- **Claude Pro, Max, Team, or Enterprise** plan
- **Code Execution enabled** in Claude settings
- **Notion MCP** connected in Claude settings
- A Notion database with the required properties (아래 참조)

---

## Installation

### Via Claude Code Marketplace (Recommended)

```bash
/plugin marketplace add Taek-D/my-claude-skills
/plugin install notion-project-upload@Taek-D/my-claude-skills
```

### Manual Installation

```bash
git clone https://github.com/Taek-D/my-claude-skills.git
cp -r my-claude-skills/skills/* ~/.claude/skills/
```

---

## Notion Database Setup

### Required Properties

| Property Name | Type | Notes |
|---------------|------|-------|
| `프로젝트명` | Title | Main project name |
| `Problem` | Text | Problem definition & context |
| `Approach` | Text | Why this method? Alternatives considered |
| `Solution` | Text | Implementation details |
| `Challenge` | Text | Obstacles, pivots, failures |
| `Result` | Text | All quantitative & qualitative outcomes |
| `Learning` | Text | Key insights & retrospective |
| `상세제목` | Text | Detailed subtitle |
| `한줄설명` | Text | One-line summary |
| `기술스택` | Multi-select | Tech stack tags |
| `카테고리` | Select | Project category |
| `글로우색상` | Select | teal / amber / red / purple / pink |
| `Extra-Label` | Text | e.g. "APPROACH & DECISION" |
| `Extra` | Text | Additional structured details |
| `업데이트 날짜` | Text | Format: YYYY.MM.DD |
| `진행기간` | Text | Format: YYYY.MM ~ YYYY.MM |

### Get your Database ID

```
https://www.notion.so/YOUR_WORKSPACE/[DATABASE_ID]?v=...
                                      ↑ this part
```

### Tell Claude your DB ID

```
"노션에 업로드해줘. DB ID는 [YOUR_DATABASE_ID]야"
```

---

## Usage

```
"노션에 업로드해줘"
"Upload this project to Notion"
"프로젝트 등록해줘"
```

업데이트:

```
"wishket-monitor 프로젝트 업데이트해줘"
"이 프로젝트 수정해서 노션에 올려줘"
```

---

## File Structure

```
skills/notion-project-upload/
├── SKILL.md                          ← Claude가 읽는 핵심 명세
├── CHANGELOG.md
├── README.md
└── references/
    ├── examples/
    │   └── project-record-example.md ← 원장 작성 예시 (직군 무관)
    ├── guides/
    │   ├── mermaid-guide.md
    │   └── screenshot-guide.md
    └── screenshot-capture/           ← 스크린샷 자동화 모듈
        ├── capture_manager.py
        ├── strategies.py
        ├── terminal_renderer.py
        └── notion_file_upload.py
```

---

## Version History

### v2.3.0 (2026.03.30) — Master Record DB

- 🗂️ **컨셉 전환**: 직군별 포트폴리오 → 직군 무관 프로젝트 원장 DB
- 🗑️ **제거**: 타입별 템플릿 파일(type1~5), 직군별 예시 9개, extra-label/differentiation 가이드
- ✅ **유지**: PACRL 프레임워크, 5가지 프로젝트 타입(섹션 구성용), 16개 속성
- 🆕 **신규**: 직군 무관 원장 예시 1개 (`project-record-example.md`)
- 🏷️ **확장**: Tech Stack Tags에 PA/PM/BA/기획 도구 추가
- 📉 **파일 수**: 20개+ → 4개 (SKILL.md + 예시 1개 + 가이드 2개)

### v2.1.0 (2026.03.06) — PACRL Framework

- Problem/Approach/Solution/Challenge/Result/Learning 구조 도입
- Approach, Challenge 필드 신규 추가 (Properties 14개 → 16개)

### v2.0.0 (2026.02.27) — 5-Type System

- Type 3 (Product Development), Type 5 (Automation & Tools) 추가
- SKILL.md 토큰 최적화 (393줄 → 197줄)

### v1.5.0 (2026.02.15) — Screenshot Automation

- 스크린샷 자동 캡처 + Notion File Upload API 연동

### v1.0.0 (2026.02.10) — Initial Release

- 4가지 프로젝트 타입, 14개 속성 자동 작성

---

## License

MIT © [Taek-D](https://github.com/Taek-D)
