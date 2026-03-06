# Extra & Extra-Label Field Guide

## 개요

**Extra-Label**: 프로젝트 고유 섹션 제목 (영어 대문자)
**Extra**: 상세 내용 (`**제목** — 설명` 형식)

## 타입별 추천 Extra-Label

### Type 1: Business Impact
| Extra-Label | 사용 시점 |
|-------------|----------|
| **A/B TEST DESIGN** | A/B 테스트 수행 시 (필수) |
| **APPROACH & DECISION** | 왜 이 분석 방법/모델을 선택했는가 (대안 비교) |
| **CHALLENGE & PIVOT** | 시행착오, A→B 피벗 상세 |
| **PERFORMANCE OPTIMIZATION** | 성능 개선 프로젝트 |
| **DEPLOYMENT STRATEGY** | 배포 전략이 복잡한 경우 |
| **COST ANALYSIS** | 비용 절감이 주요 성과 |

### Type 2: Exploratory/Analysis
| Extra-Label | 사용 시점 |
|-------------|----------|
| **HYPOTHESIS TESTING FRAMEWORK** | 가설 검증 프로젝트 |
| **APPROACH & DECISION** | 왜 이 분석 방법을 선택했는가 (대안 검토) |
| **CHALLENGE & PIVOT** | 데이터 품질 문제, 분석 방향 변경 등 시행착오 |
| **DATA DETAILS** | 데이터 규모/품질이 중요할 때 |
| **STATISTICAL VALIDATION** | 통계적 검증 강조 |
| **SEGMENTATION ANALYSIS** | 세그먼트별 분석 수행 시 |

### Type 3: Product Development
| Extra-Label | 사용 시점 |
|-------------|----------|
| **TECH STACK DECISIONS** | 기술 선택 이유가 중요할 때 |
| **APPROACH & DECISION** | 왜 이 스택/아키텍쳐를 선택했는가 |
| **CHALLENGE & PIVOT** | 구현 중 마주한 기술적 난관, 피벗 사례 |
| **FEATURE SPEC** | 핵심 기능 상세 스펙 |
| **USER FLOW** | 사용자 여정이 복잡할 때 |
| **PERFORMANCE METRICS** | Lighthouse, FCP, 번들 사이즈 등 |
| **DESIGN SYSTEM** | UI/UX 설계 원칙 설명 |

### Type 4: Learning Project
| Extra-Label | 사용 시점 |
|-------------|----------|
| **LEARNING JOURNEY** | 학습 과정 타임라인 |
| **APPROACH & DECISION** | 왜 이 강의/데이터셋을 선택했는가 |
| **CHALLENGE & PIVOT** | 학습 중 마주한 난관, 전략 변경 |
| **BEFORE/AFTER SKILLS** | 역량 변화 |
| **REAL-WORLD APPLICATION** | 실무 적용 계획 |
| **EXPERIMENT DESIGN** | 실험적 시도 |

### Type 5: Automation & Tools
| Extra-Label | 사용 시점 |
|-------------|----------|
| **WORKFLOW DESIGN** | 자동화 흐름이 핵심일 때 |
| **APPROACH & DECISION** | 왜 이 자동화 도구(Playwright/cron/n8n)를 선택했는가 |
| **CHALLENGE & PIVOT** | 크롤링 레이아웃 변경, 에러 패턴 등 시행착오 |
| **ERROR HANDLING STRATEGY** | 에러 처리가 복잡한 경우 |
| **SCHEDULING CONFIG** | 스케줄링 설계가 중요할 때 |
| **SYSTEM ARCHITECTURE** | 여러 컴포넌트 연동 시 |
| **EFFICIENCY REPORT** | 자동화 전후 비교 데이터 |

## 작성 예시

### A/B TEST DESIGN (Type 1)
```
**Control Group** — 기존 예측 알고리즘 (단순 거리 기반, 평균 오차 23분)
**Treatment Group** — XGBoost 모델 (14개 feature, 평균 오차 10분)
**Sample Size** — 각 그룹 5,000건 (총 10,000건, 2주간 수집)
**Primary Metric** — MAE, 목표: -30% 개선
**Statistical Power** — 95% 신뢰수준, 80% 검정력, p<0.05
```

### TECH STACK DECISIONS (Type 3)
```
**Frontend** — React + Vite (HMR 속도 우선, CRA 대비 10x 빌드 속도)
**Animation** — Canvas API (DOM 조작 대비 60fps 안정적 렌더링)
**State** — Context API (Redux 과도, 컴포넌트 6개 규모에 적합)
**Deploy** — Vercel (GitHub 자동 배포, Preview URL 지원)
**Sound** — Web Audio API (외부 의존성 0, 번들 사이즈 최소화)
```

### WORKFLOW DESIGN (Type 5)
```
**Trigger** — GitHub Actions cron (매일 09:00, 18:00 KST)
**Crawling** — Playwright headless (6개 사이트 병렬, timeout 30초)
**Processing** — 가격 비교 엔진 (최저가 판별 + 노이즈 필터링)
**Storage** — Google Sheets API (가격 추이 기록 + 자동 차트)
**Alert** — Discord Webhook (최저가 감지 시 임베드 알림)
**Error** — 3회 재시도 + exponential backoff + Discord 에러 알림
```

### HYPOTHESIS TESTING FRAMEWORK (Type 2)
```
**H1: 3일 내 미사용** — 가입 후 3일 내 미사용 시 이탈률 3배 증가 (Chi-square)
**H2: 프로필 완성도** — 프로필 <50% 사용자의 이탈률 유의하게 높음 (Logistic Reg)
**Test Method** — Chi-square (범주형), t-test (연속형)
**Significance Level** — α=0.05, Bonferroni correction
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
