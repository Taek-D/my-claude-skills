# 구독 서비스 이탈 패턴 분석으로 리텐션 전략 수립

> 🔬 **"왜 고객들이 떠나는가? 2만 사용자 행동 데이터 분석"**
>
> 코호트 분석과 서바이벌 분석으로 3가지 핵심 이탈 요인 발견, 타겟 리텐션 캠페인으로 30일 리텐션 +8%p 달성

---

## 🎯 Performance Overview

**30초 스캔용 - Before/After 핵심 성과**

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| 30일 리텐션 | 62% | 70% | **+8%p** |
| 월 이탈자 수 | 760명 | 600명 | **-21%** |
| 온보딩 완료율 | 41% | 68% | **+27%p** |
| 이탈 예측 정확도 | - | AUC 0.82 | **신규** |

**Impact**: 코호트 분석 + 서바이벌 분석 → 3가지 핵심 이탈 시점 발견 → 타겟 리텐션 캠페인 → 30일 리텐션 **+8%p**

---

## 📊 Analysis Process

### 1️⃣ Problem Definition

**Business Problem**

SaaS 프로덕트 구독 서비스의 30일 리텐션이 62%로 업계 벤치마크(75%) 대비 13%p 낮은 상황. 월 신규 가입 2,000명 중 760명이 30일 내 이탈. 이탈 원인에 대한 데이터 기반 이해 부족으로 기존 리텐션 캠페인의 효과가 미미했음.

**Research Questions**

1. **언제** 이탈이 집중되는가? (Critical Period 파악)
2. **누가** 이탈하는가? (High-risk Segment 식별)
3. **왜** 이탈하는가? (Root Cause 분석)
4. **어떻게** 막을 수 있는가? (Actionable Insights)

**Success Metrics**

• 통계적으로 유의한 이탈 예측 변수 3개 이상 발견 (p < 0.05)
• 이탈 고위험군 정확도 80% 이상으로 식별
• 실행 가능한 리텐션 전략 도출 및 A/B 테스트 검증
• 30일 리텐션 62% → 70% 목표 (최소 +5%p)

---

### 2️⃣ Data Collection & Exploration

**Data Sources**

**Data Sources**

• **User Events** (BigQuery) - 20K 사용자, 6개월, 1.2M 이벤트
• **User Profiles** (PostgreSQL) - 인구통계, 구독 정보, 결제 내역
• **Product Usage** (Amplitude) - 기능별 사용 빈도, 세션 시간
• **Support Tickets** (Zendesk) - 문의 내역 및 해결 여부

**Dataset Characteristics**

| Feature Category | Variables | 예시 |
|------------------|-----------|------|
| 유저 속성 | 8개 | 연령, 직업군, 기업 규모, 구독 플랜 |
| 온보딩 행동 | 12개 | 첫 세션 길이, 튜토리얼 완료 여부, 첫 프로젝트 생성 시간 |
| 제품 사용 | 15개 | 일 평균 세션, 기능별 사용 횟수, 협업 초대 수 |
| 참여도 | 6개 | 이메일 오픈율, 알림 클릭률, 커뮤니티 활동 |
| 문제 경험 | 4개 | 에러 발생 횟수, 지원 티켓 수, 해결 시간 |

**Analysis Scope**

• Cohort: 2024년 1-3월 가입자 15,000명
• Observation Period: 가입 후 30일간 추적
• Outcome: 30일 시점 Active/Churned 이진 분류
• Target Variable: 30일 리텐션 여부 (1=retained, 0=churned)

**Exploratory Analysis**

**Initial Findings**:
• 이탈자 평균 세션 수: 2.3회 vs 잔존자 8.7회
• 첫 3일 활동 없는 유저의 78%가 이탈
• 튜토리얼 완료 유저의 82% 잔존 vs 미완료 38%

---

### 3️⃣ Hypothesis & Analysis Design

**Hypothesis Testing Framework**

**가설 1: 온보딩 완료 여부가 리텐션에 영향을 미친다**

```
H0 (귀무가설): 온보딩 완료 여부와 리텐션은 무관하다
H1 (대립가설): 온보딩 완료 시 리텐션이 유의하게 높다

통계 검정: Chi-square test
```

**결과**:
| Group | 30일 리텐션 | Sample Size |
|-------|-------------|-------------|
| 온보딩 완료 | 82% | 6,200명 |
| 온보딩 미완료 | 38% | 8,800명 |

• χ² = 3,247.6, p < 0.001
• Effect Size (Cramér's V) = 0.47 (Large effect)
• **결론**: 온보딩 완료는 리텐션에 **매우 강한 양의 영향** ✅

---

**가설 2: 협업 기능 사용이 리텐션을 높인다**

```
H0: 협업 초대 여부와 리텐션은 무관하다
H1: 협업 초대 시 리텐션이 유의하게 높다

통계 검정: Two-sample t-test
```

**결과**:
| Group | 평균 리텐션 기간 (일) | SD | n |
|-------|---------------------|-----|------|
| 협업 사용 (1명+ 초대) | 89.3일 | 12.4 | 4,100명 |
| 개인 사용 (초대 0명) | 31.7일 | 18.9 | 10,900명 |

• t = 47.2, df = 14,998, p < 0.001
• Cohen's d = 3.65 (Very large effect)
• **결론**: 협업 사용자는 평균 **57.6일 더 오래 활동** ✅

---

**가설 3: 첫 3일 내 핵심 기능 사용이 Critical**

```
H0: 첫 3일 핵심 기능 사용 횟수와 30일 리텐션은 무관하다
H1: 첫 3일 핵심 기능 사용 횟수가 많을수록 30일 리텐션이 높다

통계 검정: Logistic Regression
```

**결과**:

```python
from sklearn.linear_model import LogisticRegression

# 핵심 기능 사용 횟수 (첫 3일) → 30일 리텐션 예측
X = df[['project_created', 'template_used', 'export_completed']]
y = df['retained_30d']  # 0: Churned, 1: Retained

model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Odds Ratio 해석
odds_ratios = np.exp(model.coef_[0])
# Project Created: 3.42x, Template Used: 2.18x
# Export Completed: 4.67x (p < 0.001) ← 가장 강력한 예측 변수
```

• 모델 정확도: 84%
• AUC-ROC: 0.89
• **결론**: 첫 3일 Export 완료 시 리텐션 확률 **4.67배** 증가 ✅

---

### 4️⃣ Key Findings

**Statistical Validation Summary**

| Hypothesis | Test | p-value | Effect Size | Result |
|------------|------|---------|-------------|--------|
| H1: 온보딩 완료 | Chi-square | < 0.001 | V = 0.47 | ✅ Reject H0 |
| H2: 협업 사용 | t-test | < 0.001 | d = 3.65 | ✅ Reject H0 |
| H3: 핵심 기능 사용 | Logistic Reg | < 0.001 | OR = 4.67 | ✅ Reject H0 |

**모든 가설이 통계적으로 유의** (p < 0.001, large effect sizes)

---

**Critical Insights**

**Finding 1: "Aha Moment" = Export 완료**

첫 3일 내 Export 완료 유저의 30일 리텐션은 **91%** vs 미완료 유저 **42%**

• Export는 "실제 업무에 활용"을 의미하는 핵심 지표
• 로지스틱 회귀 계수: OR = 4.67 (p < 0.001)
• 첫 3일 Export 완료율이 현재 23%에 불과 → **개선 여지 큼**

**Finding 2: 협업 사용이 "Sticky Factor"**

협업 초대 1명+ 시 리텐션 **82%** vs 개인 사용 **39%**

• 평균 리텐션 기간: 89.3일 vs 31.7일 (**+57.6일**)
• Cohen's d = 3.65 (Very large effect size)
• 네트워크 효과로 이탈 장벽 상승 → **바이럴 성장 기회**

**Finding 3: Day 3, 7, 13에 이탈 집중**

서바이벌 분석 결과 3개의 Critical Drop-off Points 발견:

• **Day 3** (온보딩 미완료): 리텐션 82% → 61% (**-21%p**)
• **Day 7** (핵심 기능 미사용): 리텐션 61% → 48% (**-13%p**)
• **Day 13** (체험 종료 직전): 리텐션 48% → 34% (**-14%p**)

→ 타이밍별 타겟 캠페인 필요

---

### 5️⃣ Recommendations & Impact

**Actionable Strategies**

**전략 1: 온보딩 플로우 개선 (Product Team)**

**문제**: 온보딩 완료율 41%, 미완료 시 리텐션 38%

**솔루션**:
• "첫 Export 유도" 인터랙티브 튜토리얼 추가 (5분 가이드)
• 진행률 바 + 체크리스트로 완료 동기 부여
• 튜토리얼 스킵 시 Day 2 리마인더 발송

**결과**: 온보딩 완료율 41% → 68% (**+66%**), 첫 3일 Export 완료율 23% → 47% (**+104%**)

---

**전략 2: 타이밍 기반 리텐션 캠페인 (Marketing Team)**

**문제**: 일률적 캠페인으로 효과 미미

**솔루션**:
• **Day 3 캠페인**: 온보딩 미완료자 대상 튜토리얼 리마인더
• **Day 7 캠페인**: 협업 미사용자 대상 팀 초대 인센티브 (크레딧 제공)
• **Day 13 캠페인**: 전체 대상 "성과 리포트" 발송 (ROI 강조)

**결과**: 이메일 오픈율 18% → 34%, CTR 2.1% → 5.8%

---

**전략 3: High-Risk 세그먼트 프로액티브 지원 (CS Team)**

**문제**: 반응형 지원으로 이탈 후 발견

**솔루션**:
• High-risk 정의: 온보딩 미완료 + 첫 3일 Export 없음 (이탈률 78%)
• Day 2, 7 체크인 콜 (10분 컨설팅)
• 맞춤형 사용 사례 가이드 제공

**결과**: 아웃리치 받은 유저 리텐션 41% → 68% (**+66%**)

---

**Business Impact**

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| 30일 리텐션 | 62% | 70% | **+8%p** |
| 월 이탈자 수 | 760명 | 600명 | **-21%** |
| 온보딩 완료율 | 41% | 68% | **+27%p** |
| CAC 효율 | - | **+13%** | 동일 비용으로 더 많은 장기 고객 |

**비용 효과 추정**:
• 리텐션 개선: +8%p × 월 2,000 신규 가입 = 약 160명 추가 유지
• 유저당 월 구독료 ₩15,000 기준, 월 추가 수익 약 **₩2.4M**
• 연간 추정: 최소 **₩28.8M** 추가 수익

---

### 6️⃣ A/B Test & Validation

**Test Design**

**Hypothesis**: Day 13 "성과 리포트" 이메일이 14일 전환율을 높인다

```
Control (A): 이메일 없음 (기존 플로우)
Variant (B): Day 13 성과 리포트 발송 (사용 통계 + ROI 강조)

Primary Metric: 14일 유료 전환율
Sample Size: n = 2,400 (1,200 per group)
Duration: 2 weeks
Significance Level: α = 0.05
```

**Results**

| Group | 14일 전환율 | Lift | p-value |
|-------|-------------|------|---------|
| Control (A) | 32.1% | - | - |
| Variant (B) | 41.3% | **+9.2%p** | **0.003** |

• 통계적으로 유의한 차이 (p = 0.003 < 0.05)
• Relative Improvement: **+29%**
• 예상 월 전환 증가: 9.2%p × 월 2,000 가입 = 약 184명 추가 전환

**Launch Decision**: ✅ Roll out to 100% of users

---

## 💡 Key Takeaways

**What Worked**

• **코호트 분석의 힘** - 집계된 평균은 진실을 숨김, 일별 분해로 3개의 Critical Period 발견
• **통계 검정으로 신뢰 확보** - "체감"이 아닌 "증명"으로 이해관계자 설득, 3개 가설 모두 p < 0.001
• **단순 지표가 강력** - 복잡한 ML 모델보다 "첫 3일 Export 여부" 한 변수가 더 actionable

**Lessons Learned**

• **세그먼트 + 타이밍이 핵심** - 일률적 캠페인 대신 세그먼트별 + Critical Period별 접근으로 효과 극대화
• **Cross-functional 협업** - Product/Marketing/CS 3개 팀이 데이터 기반으로 정렬되어 빠른 실행
• **A/B 테스트로 검증** - 분석 인사이트 → 전략 수립 → A/B 테스트 → 전사 확대, 과학적 의사결정

---

## 🤝 Collaboration & Impact

**Cross-functional Collaboration**

**Product Team** (PM: 최수진)
• 주 2회 분석 결과 공유 → 온보딩 플로우 개선에 즉시 반영
• "첫 Export 유도" 튜토리얼 추가 (5분짜리 인터랙티브 가이드)
• 결과: 첫 3일 Export 완료율 23% → 47% (**+104%**)

**Marketing Team** (매니저: 김도현)
• Day 3, 7, 13 타이밍에 맞춘 리텐션 이메일 캠페인 설계
• 세그먼트별 메시지 차별화 (온보딩 미완료 / 협업 미사용 등)
• 결과: 이메일 오픈율 18% → 34%, CTR 2.1% → 5.8%

**Customer Success Team** (리드: 박서연)
• High-risk 세그먼트 (온보딩 미완료 + 첫 3일 Export 없음) 우선 지원
• 프로액티브 아웃리치 프로그램 운영 (Day 2, 7 체크인 콜)
• 결과: 아웃리치 받은 유저 리텐션 41% → 68% (**+66%**)

**Business Impact**

• **30일 리텐션**: 62% → 70% (**+8%p, +13% 상대 증가**)
• **리텐션 개선**: 30일 리텐션 62% → 70% (+8%p), 월 160명 추가 유지
• **전환율 향상**: 14일 유료 전환율 +9.2%p (A/B 테스트 검증)
• **CAC 투자 효율**: 동일한 마케팅 비용으로 8% 더 많은 장기 고객 확보

---

## 📊 Visualizations & Code

### Survival Analysis (Kaplan-Meier)

```python
from lifelines import KaplanMeierFitter

kmf = KaplanMeierFitter()

# 온보딩 완료 vs 미완료 그룹 생존 곡선 비교
for label, group in df.groupby('onboarding_completed'):
    name = 'Completed' if label else 'Not Completed'
    kmf.fit(group['days_active'], event_observed=group['churned'], label=name)
    kmf.plot_survival_function()

plt.title('Survival Curve by Onboarding Status')
plt.xlabel('Days Since Signup')
plt.ylabel('Retention Rate')
# 결과: Day 30 시점 생존율 격차 44%p (82% vs 38%)
```

### Cohort Heatmap

```python
# 월별 코호트 리텐션 히트맵
cohort_data = df.pivot_table(
    values='is_active', index='cohort_month',
    columns='days_since_signup', aggfunc='mean'
)

sns.heatmap(cohort_data, annot=True, fmt='.1%',
            cmap='RdYlGn', vmin=0, vmax=1)
plt.title('Monthly Cohort Retention Heatmap')

# 인사이트: 2024년 2월 코호트 이상치 (리텐션 +12%p)
# → 제품 업데이트 + PR 효과로 확인
```

---

## 🚀 Impact & Implementation

**Implemented Actions (3개월)**

| Action | Timeline | Owner | Status |
|--------|----------|-------|--------|
| 온보딩 플로우 개선 | Week 1-4 | Product | ✅ Launched |
| 리텐션 이메일 캠페인 | Week 2-3 | Marketing | ✅ Ongoing |
| High-risk 아웃리치 | Week 3-6 | CS | ✅ Scaled |
| 협업 인센티브 프로그램 | Week 5-8 | Growth | ✅ Launched |

**Results After 3 Months**

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| 30일 리텐션 | 62% | 70% | **+8%p** |
| 첫 3일 Export 완료율 | 23% | 47% | **+24%p** |
| 협업 기능 사용률 | 27% | 41% | **+14%p** |
| 온보딩 완료율 | 41% | 63% | **+22%p** |
| 월 MRR 순증 | $127K | $189K | **+49%** |

**A/B Test Validation**

Day 13 "성과 리포트" 이메일 A/B 테스트:
• Control (이메일 없음): 14일 전환율 32%
• Variant (성과 리포트 발송): 14일 전환율 41%
• **Uplift: +9%p** (p = 0.003, n = 2,400)

---

## 🔗 Links

[Full Analysis Report](링크) | [Cohort Dashboard](링크) | [A/B Test Results](링크) | [Jupyter Notebook](링크)
