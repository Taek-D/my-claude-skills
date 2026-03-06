# Type 1: Business Impact Template

> 프로젝트에 정량적 비즈니스 성과가 있을 때 사용

## Template Structure

```markdown
> 💡 **"핵심 성과 한 줄 (정량적 수치)"**
>
> 프로젝트 한줄 요약

---

## 🎯 Performance Overview

**30초 스캔용 - 핵심 성과**

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| 주요지표1 | 값 | 값 | **+X%** |
| 주요지표2 | 값 | 값 | **-X%** |
| 주요지표3 | 값 | 값 | **X배** |

**Impact Summary**: 무엇을 했고 → 어떤 결과가 나왔는지 → 비즈니스 임팩트

---
```

## 권장 섹션 (프로젝트에 맞게 2-3개 선택)

### Option A: Problem & Root Cause

```markdown
## 🔍 Problem & Root Cause

**Business Pain Point**

• 어떤 문제가 있었는지 구체적으로
• 이 문제로 인한 비즈니스 손실 (정량적)

**Root Cause Analysis**

| Challenge | Root Cause | Evidence |
|-----------|-----------|----------|
| 문제1 | 원인1 | 데이터 근거 |
| 문제2 | 원인2 | 데이터 근거 |
```

### Option B: Approach & Solution Design

```markdown
## 🛠️ Approach & Solution Design

**Why This Approach** ← Approach 필드 반영

• 왜 이 방법을 선택했는가 (데이터 근거, 대안 검토 결과)
• 검토했지만 선택하지 않은 방법과 이유

**Solution Options**

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| 방법 A | 장점 | 단점 | ❌ 기각 이유 |
| 방법 B | 장점 | 단점 | ✅ **선택** |

**A/B Test Design** (해당 시)

• Control vs Treatment 설계
• 샘플 크기 및 테스트 기간
• Primary/Secondary Metrics
```

### Option C: Technical Implementation

```markdown
## ⚙️ Technical Implementation

**Architecture**

(Mermaid 다이어그램 3-5단계 — mermaid-guide.md 참조)

**Core Implementation**

(핵심 로직 코드 10-15줄, 주석 포함)

**구현 포인트**: 기술적 선택 이유, 최적화 방법
```

### Option D: Collaboration & Impact

```markdown
## 🤝 Collaboration & Impact

**My Role**: 내가 직접 수행한 역할 구체적으로

**Teams Involved**

• Data (나): 구체적 역할
• Engineering/Product/Operations: 협업 내용

**Communication**: 비기술 팀원 대상 설명 방법, 의사결정 과정
```

### Option E: Deployment & Usage

```markdown
## 🚀 Deployment & Usage

**Rollout**: Canary → Gradual → Full 배포 과정
**Monitoring**: 핵심 지표 모니터링 방법
**Production Impact**: 운영 X개월 후 실제 성과
```

### Option F: A/B Test Results

```markdown
## 📊 A/B Test Results

| Metric | Control | Treatment | Lift | p-value |
|--------|---------|-----------|------|---------|
| Primary | 값 | 값 | **+X%** | p<0.05 |
| Secondary | 값 | 값 | **+X%** | p<0.05 |

**결론**: Treatment 승리/기각 이유, 후속 조치
```

## 필수 마무리 섹션

```markdown
---

## 💡 Key Takeaways

**"핵심 학습 한 줄"**

기술적 깨달음, 방법론 체득 2-3문장

**한계 및 개선 방향**

• **한계점**: 구체적 제약사항
• **Next Step**: 다음 개선안

---

## 🔗 Links

[GitHub](링크) | [Dashboard](링크)
```

## 구성 예시

포트폴리오 내 Type 1 프로젝트들이 서로 다르게 보이도록:

**프로젝트 A** (A/B 테스트 중심):
Overview → Problem → A/B Test Results → Collaboration → Takeaways

**프로젝트 B** (기술 구현 중심):
Overview → Solution Design → Technical Implementation → Deployment → Takeaways

**프로젝트 C** (비즈니스 분석 중심):
Overview → Problem & Root Cause → Collaboration → Takeaways

## Metric Scale Reference (Type 1)

| 프로젝트 성격 | 적절한 스케일 | 예시 |
|--------------|-------------|------|
| 개인 자동화 | 주 2-5시간 절약, 연 수십만 원 | 리포트 자동화 |
| 팀 대시보드 | 의사결정 속도 향상, 월 수시간 절약 | Tableau 대시보드 |
| 분석 프로젝트 | 전환율 +X%, 이탈률 -X% | A/B 테스트 |
| 비용 최적화 | 월 수만~수십만 원 절감 | 클라우드 비용 |

⚠️ ROI 500%+, 연 수억 원 임팩트는 시니어 전담팀 수준. 개인 프로젝트에 부적절.
