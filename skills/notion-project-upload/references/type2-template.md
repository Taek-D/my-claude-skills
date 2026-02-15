# Type 2: Exploratory Analysis Template

> 데이터 분석, EDA, 인사이트 발견, 가설 검증 프로젝트에 사용

## Template Structure

```markdown
> 💡 **"핵심 발견(Discovery)을 한 줄로"**
>
> 어떤 데이터를 분석해서 무엇을 발견했는지

---

## 🎯 Performance Overview

**30초 스캔용 - 주요 발견**

| 발견 | 분석 결과 | Insight |
|------|----------|---------|
| 핵심 발견1 | 수치/통계 | **비즈니스 의미** |
| 핵심 발견2 | 수치/통계 | **비즈니스 의미** |
| 핵심 발견3 | 수치/통계 | **비즈니스 의미** |

**Impact Summary**: 데이터 분석으로 발견한 것 → 비즈니스 액션 → 기대 효과

---
```

## 권장 섹션 (프로젝트에 맞게 2-3개 선택)

### Option A: Problem Definition

```markdown
## 🔍 Problem Definition

**Business Context**

• 어떤 비즈니스 문제를 해결하려고 했는지
• 왜 이 분석이 필요했는지

**Analysis Goals**

• 명확한 분석 목표 (3-5개)
• 성공 기준 (어떤 인사이트를 찾으면 성공인지)
```

### Option B: Data & Methodology

```markdown
## 📊 Data & Methodology

**Data Sources**

| Source | Type | Records | Period |
|--------|------|---------|--------|
| 소스1 | DB/파일 | X건 | 기간 |
| 소스2 | DB/파일 | X건 | 기간 |

**Data Quality**: 결측치 X%, 이상치 처리 방법, 전처리 과정

**Analysis Methods**

| Step | Method | Tool | Purpose |
|------|--------|------|---------|
| 1. 탐색 | EDA, 분포 확인 | Pandas, Seaborn | 패턴 발견 |
| 2. 검정 | t-test, Chi-square | Scipy | 통계적 유의성 |
| 3. 모델링 | Regression/Classification | scikit-learn | 예측/분류 |
```

### Option C: Key Findings

```markdown
## 📈 Key Findings

**Finding 1: [핵심 발견 제목]**

• **분석 결과**: 구체적 수치와 통계적 근거
• **비즈니스 의미**: 이 발견이 의미하는 것
• **제안 액션**: 어떤 조치가 가능한지

**Finding 2: [핵심 발견 제목]**

• **분석 결과**: 수치
• **비즈니스 의미**: 해석
• **제안 액션**: 조치

(핵심 분석 코드 10-15줄 — 가장 인사이트가 있는 부분만)
```

### Option D: Statistical Validation

```markdown
## 📐 Statistical Validation

**Hypothesis Testing**

| 가설 | 검정방법 | 결과 | 해석 |
|------|---------|------|------|
| H1: 가설 | Chi-square | χ²=X, p<0.05 | **검증됨** |
| H2: 가설 | t-test | t=X, p>0.05 | 기각됨 |

**Effect Sizes**: Cohen's d, Odds Ratio 등 효과 크기 보고
**Multiple Testing**: Bonferroni correction 적용 여부
```

### Option E: Recommendations

```markdown
## 💼 Recommendations

| Recommendation | Data Evidence | Expected Impact | Priority |
|----------------|--------------|-----------------|----------|
| 제안1 | 근거 데이터 | 기대 효과 | P0 |
| 제안2 | 근거 데이터 | 기대 효과 | P1 |
| 제안3 | 근거 데이터 | 기대 효과 | P2 |
```

### Option F: Collaboration & Impact

```markdown
## 🤝 Collaboration & Impact

**My Role**: 분석 전 과정 수행

**Communication**: 분석 결과 공유 방법 (리포트, 대시보드, 발표)

**Business Impact**: 분석 결과가 의사결정에 어떻게 기여했는지
```

## 필수 마무리 섹션

```markdown
---

## 💡 Key Takeaways

**"배운 점"**

통계적 방법론, 데이터 전처리 기법, 분석 설계 등 구체적으로

**한계 및 후속 분석**

• **한계점**: 데이터/분석 한계
• **Next Step**: 추가 실험, 필요한 데이터

---

## 🔗 Links

[Analysis Notebook](링크) | [Dashboard](링크) | [Report](링크)
```

## 구성 예시

**프로젝트 A** (가설 검증형):
Overview → Problem → Statistical Validation → Recommendations → Takeaways

**프로젝트 B** (패턴 발견형):
Overview → Data & Methodology → Key Findings → Collaboration → Takeaways

**프로젝트 C** (비즈니스 분석형):
Overview → Problem → Key Findings → Recommendations → Takeaways

## Metric Scale Reference (Type 2)

| 프로젝트 성격 | 적절한 스케일 | 예시 |
|--------------|-------------|------|
| 개인 EDA | 수백~수천 건, 인사이트 발견 | Kaggle 데이터셋 분석 |
| 팀 분석 | 수천~수만 건, 개선 제안 | 이탈 분석, 세그먼트 분석 |
| 부서 프로젝트 | 수만 건, 의사결정 기여 | A/B 테스트 분석 |

⚠️ 12만+ 유저 데이터, 연 수억 원 LTV는 대기업 전담팀 규모. 데이터 출처를 반드시 명시할 것.
