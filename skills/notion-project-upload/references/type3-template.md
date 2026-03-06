# Type 3: Product Development Template

> 웹앱, 모바일앱, 게임, SaaS, 서비스 개발 프로젝트에 사용

## Template Structure

```markdown
> 💡 **"무엇을 만들었고, 누가 어떻게 쓰는가"**
>
> 핵심 기능과 사용자 가치를 한 줄로

---

## 🎯 Performance Overview

**30초 스캔용 - 프로덕트 성과**

| Metric | Value | Note |
|--------|-------|------|
| 핵심 기능 | N개 | 주요 기능 나열 |
| 기술 스택 | X, Y, Z | 프론트/백/인프라 |
| 사용자/배포 | X명/플랫폼 | MAU, 다운로드, 배포 상태 |
| 개발 기간 | X주 | 기획~배포 |

**Impact Summary**: 무엇을 만들었고 → 어떤 문제를 해결했으며 → 사용자에게 어떤 가치를 전달하는지

---
```

## 권장 섹션 (프로젝트에 맞게 2-3개 선택)

### Option A: Problem & Motivation + Approach

```markdown
## 🔍 Problem & Motivation

**Why I Built This**

• 어떤 문제를 해결하려고 만들었는지 (개인 페인포인트 or 시장 니즈)
• 기존 대안과 비교했을 때 부족한 점

**Why This Approach** ← Approach 필드 반영

• 왜 이 기술 스택/아키텍쳐를 선택했는가
• 검토했지만 선택하지 않은 대안 (e.g. Next.js vs Vite, Supabase vs Firebase)

**Target User**

| 페르소나 | 니즈 | 현재 해결 방법 | 한계 |
|----------|------|---------------|------|
| 사용자 A | 니즈 | 기존 방법 | 불편한 점 |

**Core Value Proposition**: 이 서비스만의 차별점 한 줄
```

### Option B: Feature Showcase

```markdown
## ✨ Feature Showcase

**Feature 1: [기능명]**

• **What**: 기능 설명
• **How**: 기술적 구현 방법
• **Impact**: 사용자 가치

**Feature 2: [기능명]**

• **What**: 기능 설명
• **How**: 구현 방법
• **Impact**: 사용자 가치

(핵심 기능 코드 10-15줄 — UI 로직이나 핵심 비즈니스 로직)
```

### Option C: Architecture & Tech Stack

```markdown
## 🏗️ Architecture & Tech Stack

**System Architecture**

(Mermaid 다이어그램 — Frontend → API → Backend → DB)

**Tech Decisions**

| Layer | Choice | Why | Alternatives Considered |
|-------|--------|-----|------------------------|
| Frontend | React/Next.js | 이유 | Vue, Svelte |
| Backend | FastAPI | 이유 | Express, Django |
| DB | PostgreSQL | 이유 | MongoDB, SQLite |
| Deploy | Vercel | 이유 | Netlify, AWS |

**Technical Challenges**: 가장 어려웠던 기술적 도전과 해결 과정
```

### Option D: User Experience & Metrics

```markdown
## 📱 User Experience & Metrics

**User Flow**

(Mermaid 다이어그램 — 핵심 사용자 여정)

**Usage Metrics** (해당 시)

| Metric | Value | Period |
|--------|-------|--------|
| 방문자/DAU | X명 | 기간 |
| 핵심 기능 사용률 | X% | 기간 |
| 평균 세션 시간 | X분 | 기간 |

**User Feedback**: 실제 피드백, 커뮤니티 반응, 개선 요청 사항
```

### Option E: Development Process

```markdown
## 🔄 Development Process

**Timeline**

| Phase | Period | Focus | Deliverable |
|-------|--------|-------|-------------|
| 기획 | Week 1 | 요구사항 정의 | PRD/와이어프레임 |
| MVP | Week 2-3 | 핵심 기능 구현 | v0.1 |
| 개선 | Week 4+ | 피드백 반영 | v1.0 |

**Iteration Highlights**: 피드백 → 개선 사이클 중 가장 의미있었던 변화
```

### Option F: Deployment & Operations

```markdown
## 🚀 Deployment & Operations

**Infrastructure**

• Hosting: Vercel/Netlify/AWS
• CI/CD: GitHub Actions
• Monitoring: 에러 트래킹 방법

**Performance**

| Metric | Target | Actual |
|--------|--------|--------|
| Lighthouse Score | 90+ | X |
| FCP | <1.5s | Xs |
| API Response | <200ms | Xms |
```

## 필수 마무리 섹션

```markdown
---

## 💡 Key Takeaways

**"핵심 학습 한 줄"**

풀스택 개발 경험, 프로덕트 사고, 사용자 중심 개발 등

**한계 및 개선 방향**

• **현재 한계**: 구체적 제약사항
• **Next Step**: v2 계획, 추가 기능

---

## 🔗 Links

[Live Demo](링크) | [GitHub](링크) | [App Store](링크)
```

## 구성 예시

**프로젝트 A** (웹앱/SaaS):
Overview → Problem → Feature Showcase → Architecture → User Metrics → Takeaways

**프로젝트 B** (모바일 게임):
Overview → Feature Showcase → Development Process → User Feedback → Takeaways

**프로젝트 C** (포트폴리오 사이트):
Overview → Architecture → Deployment → Takeaways

## Metric Scale Reference (Type 3)

| 프로젝트 성격 | 적절한 스케일 | 비현실적 |
|--------------|-------------|---------|
| 사이드 프로젝트 | DAU 10-100명, GitHub Stars 10-50 | DAU 10K+ |
| 인디 앱/게임 | 다운로드 100-1,000, 평점 4.0+ | 100K 다운로드 |
| 웹 서비스 | 방문자 100-1,000/월, 기능 5-15개 | 10K MAU+ |

⚠️ 사이드 프로젝트에서 MAU 10,000+, 매출 발생은 비현실적. "만든 과정"과 "기술적 의사결정"이 핵심.
