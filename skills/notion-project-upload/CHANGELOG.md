# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.3.0] - 2026-03-30

### Changed

#### 컨셉 전환: 직군별 포트폴리오 → 프로젝트 원장 DB

**핵심 변경**: Notion을 "직군별 포트폴리오"가 아닌 "프로젝트 원장 DB"로 재정의.
직군 색 없이 팩트를 최대한 상세하게 기록하고, 포트폴리오 작성은 별도로 진행한다.

**이유**:
- DA/PA/BA/PM/PO/기획 등 여러 직군에 동시 지원하는 상황
- 동일 프로젝트를 직군마다 다르게 서술해야 하므로, 원본 팩트가 먼저 필요
- 직군 특화 서술은 Claude 프로젝트 내에서 Notion 원장을 읽어 생성하는 방식으로 분리

### Removed

- **타입별 템플릿 파일 5개 제거**: `type1~5-template.md` → SKILL.md에 섹션 힌트 표로 축약
- **직군별 예시 9개 제거**: DA 5개 (type1~5) + PA/PM/BA/기획 4개 → 모두 직군 특화 서술이었으므로 제거
- **가이드 2개 제거**: `extra-label-guide.md`, `differentiation-guide.md` → 직군 특화 내용 위주였음

### Added

- **원장 예시 1개 신규**: `references/examples/project-record-example.md`
  - 직군 색 없이 팩트만 상세하게 기록한 예시
  - 쿠팡윙 가격 모니터링 자동화 프로젝트 기준
  - Problem/Approach/Solution/Challenge/Result/Learning 전 필드 완성
- **Tech Stack Tags 확장**: PA (Amplitude, GA4, Mixpanel), PM/PO (Jira, Confluence), BA (Power Automate, Excel), 기획 (Figma, Miro) 추가
- **Result 필드 원칙 명시**: "있는 수치 전부 기록, 직군 필터 없이"
- **Quality Checklist 항목 추가**: "Result: 있는 수치 전부 기록했는가? (직군 필터 없이)"

### Impact

- 파일 수: 20개+ → **4개** (SKILL.md + 예시 1개 + 가이드 2개)
- SKILL.md: 직군 감지 섹션 제거로 단일 목적에 집중
- Step 1: 외부 템플릿 파일 참조 → SKILL.md 인라인 섹션 힌트 표로 축약

---

## [2.1.0] - 2026-03-06

### Changed

#### 포트폴리오 서술 구조 개선 (PACRL 프레임워크)
- **Problem → Approach → Solution → Challenge → Result → Learning** 구조로 개편
- 채용담당자가 가장 보고 싶어하는 "왜 이 방법?"과 "시행착오"를 필드로 명시화
- `Impact` 필드 → `Result` 로 이름 변경 (노션 DB 반영 완료)
- `Approach` 필드 신규 추가: 왜 이 방법을 선택했는가 (근거, 대안 검토)
- `Challenge` 필드 신규 추가: 시행착오, A→B 피벗, 실패 케이스
- Properties 수: 14개 → 16개
- Quality Checklist에 Approach/Challenge 검증 항목 추가

---

## [2.0.0] - 2026-02-27

### Added

#### Type 3: Product Development Template (NEW)
- **웹앱/모바일앱/게임/SaaS 프로젝트** 전용 템플릿
- 글로우 색상: pink (시각화/프로덕트)

#### Type 5: Automation & Tools Template (NEW)
- **봇/파이프라인/크롤러/CLI 도구/모니터링** 전용 템플릿
- 글로우 색상: amber (자동화)

#### Screenshot Guide (분리)
- SKILL.md에 인라인되어 있던 스크린샷 가이드를 `references/guides/screenshot-guide.md`로 분리

### Changed

#### SKILL.md 전면 리팩토링
- **393줄 → 197줄** (50% 감소, 토큰 최적화)
- 5타입 체계: 3타입(1/2/4) → 5타입(1/2/3/4/5) 확장

---

## [1.5.0] - 2026-02-15

### Added

#### Screenshot Auto-Capture
- 프로젝트 유형별 자동 캡처 전략 엔진
- Notion File Upload API 직접 연동 (외부 호스팅 불필요)
- Playwright 웹앱 자동 실행 + 캡처
- Pillow 기반 Catppuccin 테마 터미널 렌더러

---

## [1.4.0] - 2026-02-14

### Changed

#### File Structure Overhaul (Token Optimization)
- `templates.md` (2,390줄) → 타입별 분리 파일 (~170줄씩)
- 토큰 75% 절감 (업로드 시 해당 타입 파일만 로딩)

### Added
- Portfolio Balance Check (Pre-upload)
- Update Diff Preview
- Language Rules Standardization

---

## [1.3.2] - 2026-02-11

### Removed
- Type 3 (Technical Implementation) 제거 — DA 포트폴리오에 부적합

---

## [1.2.0] - 2026-02-11

### Added
- Collaboration & Impact 섹션
- Statistical Validation 섹션 (Type 2)
- Deployment & Usage 섹션
- Update/Modify 기능

---

## [1.1.0] - 2026-02-11

### Added
- Dataset Section (Type 1/2/3)

---

## [1.0.0] - 2026-02-10

### Added
- Initial release
- 4 project type templates
- 14 property fields auto-population
- Tech stack tagging, Glow color selection

[2.3.0]: https://github.com/Taek-D/my-claude-skills/compare/v2.1.0...v2.3.0
[2.1.0]: https://github.com/Taek-D/my-claude-skills/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/Taek-D/my-claude-skills/compare/v1.5.0...v2.0.0
[1.5.0]: https://github.com/Taek-D/my-claude-skills/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/Taek-D/my-claude-skills/compare/v1.3.2...v1.4.0
[1.3.2]: https://github.com/Taek-D/my-claude-skills/compare/v1.2.0...v1.3.2
[1.2.0]: https://github.com/Taek-D/my-claude-skills/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/Taek-D/my-claude-skills/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Taek-D/my-claude-skills/releases/tag/v1.0.0
