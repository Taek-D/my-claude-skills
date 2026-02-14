# Extra & Extra-Label Field Guide

## 개요

**Extra-Label**: 프로젝트 고유 섹션 제목 (영어 대문자)
**Extra**: 상세 내용 (`**제목** — 설명` 형식)

## 타입별 추천 Extra-Label

### Type 1: Business Impact
| Extra-Label | 사용 시점 |
|-------------|----------|
| **A/B TEST DESIGN** | A/B 테스트 수행 시 (필수) |
| **PERFORMANCE OPTIMIZATION** | 성능 개선 프로젝트 |
| **DEPLOYMENT STRATEGY** | 배포 전략이 복잡한 경우 |
| **COST ANALYSIS** | 비용 절감이 주요 성과 |

### Type 2: Exploratory/Analysis
| Extra-Label | 사용 시점 |
|-------------|----------|
| **HYPOTHESIS TESTING FRAMEWORK** | 가설 검증 프로젝트 |
| **DATA DETAILS** | 데이터 규모/품질이 중요할 때 |
| **STATISTICAL VALIDATION** | 통계적 검증 강조 |
| **SEGMENTATION ANALYSIS** | 세그먼트별 분석 수행 시 |

### Type 4: Learning Project
| Extra-Label | 사용 시점 |
|-------------|----------|
| **LEARNING JOURNEY** | 학습 과정 타임라인 |
| **BEFORE/AFTER SKILLS** | 역량 변화 |
| **REAL-WORLD APPLICATION** | 실무 적용 계획 |
| **EXPERIMENT DESIGN** | 실험적 시도 |

## 작성 예시

### A/B TEST DESIGN (Type 1)
```
**Control Group** — 기존 예측 알고리즘 (단순 거리 기반, 평균 오차 23분)
**Treatment Group** — XGBoost 모델 (14개 feature, 평균 오차 10분)
**Sample Size** — 각 그룹 5,000건 (총 10,000건, 2주간 수집)
**Primary Metric** — MAE, 목표: -30% 개선
**Statistical Power** — 95% 신뢰수준, 80% 검정력, p<0.05
```

### HYPOTHESIS TESTING FRAMEWORK (Type 2)
```
**H1: 3일 내 미사용** — 가입 후 3일 내 미사용 시 이탈률 3배 증가 (Chi-square)
**H2: 프로필 완성도** — 프로필 <50% 사용자의 이탈률 유의하게 높음 (Logistic Reg)
**Test Method** — Chi-square (범주형), t-test (연속형)
**Significance Level** — α=0.05, Bonferroni correction
```

### DATA DETAILS (Type 2)
```
**Data Source** — PostgreSQL (user_events), S3 (clickstream logs)
**Time Range** — 2024.01 ~ 2024.12 (12개월)
**Sample Size** — 15,000명 (신규 가입자)
**Data Quality** — Missing <2%, IQR 이상치 제거
**Feature Engineering** — 20개 features (demographic 6, behavioral 9, temporal 5)
```

### LEARNING JOURNEY (Type 4)
```
**Week 1-2: 이론** — 핵심 개념 학습 (강의, 문서, 영상)
**Week 3-4: 실습** — Kaggle 커널 복제, Feature engineering 실험
**Week 5-6: 경진대회** — 모델 앙상블, 하이퍼파라미터 튜닝
**Week 7-8: 정리** — 코드 정리, 블로그 포스팅, GitHub 공개
**Total** — 87시간 투자
```

## 규칙

**✅ DO**:
- 5-8개 항목 (최대 10개)
- 정량적 수치 포함 (%, 숫자, 금액)
- 본문에 없는 추가 디테일만
- `**제목** — 설명` 형식 준수

**❌ DON'T**:
- 추상적 내용 ("좋은 전략을 사용했습니다")
- 본문과 중복되는 내용
- 약어 남발 (K8S, CICD → Kubernetes, CI/CD Pipeline)
- 정량 수치 없이 작성
