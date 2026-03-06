# Type 5: Automation & Tools Template

> 봇, 파이프라인, 크롤러, CLI 도구, 스케줄러, 모니터링 시스템에 사용

## Template Structure

```markdown
> 💡 **"무엇을 자동화했고, 얼마나 효율적인가"**
>
> 수작업 X시간 → 자동화 후 Y분, 핵심 워크플로우 한 줄 요약

---

## 🎯 Performance Overview

**30초 스캔용 - 자동화 성과**

| Metric | Before (수작업) | After (자동화) | Improvement |
|--------|---------------|---------------|-------------|
| 소요 시간 | X시간 | Y분 | **-Z%** |
| 처리량 | 건/일 | 건/일 | **+X배** |
| 에러율 | X% | Y% | **-Z%** |
| 빈도 | 수동 (비정기) | 자동 (매일/시간) | **상시 운영** |

**Impact Summary**: 수작업 프로세스 분석 → 핵심 워크플로우 자동화 → 시간 절약 + 정확도 향상 + 운영 안정화

---
```

## 권장 섹션 (프로젝트에 맞게 2-3개 선택)

### Option A: Problem & Manual Process + Approach

```markdown
## 🔍 Problem & Manual Process

**Pain Point**

• 수작업으로 X를 해야 했고, 매번 Y시간 소요
• 실수 발생 빈도 / 반복 작업의 비효율

**Why This Automation Approach** ← Approach 필드 반영

• 왜 이 방법(Playwright/cron/n8n 등)을 선택했는가
• 검토했지만 선택하지 않은 대안과 이유

**기존 수작업 프로세스**

| Step | 작업 내용 | 소요 시간 | 실수 위험 |
|------|----------|----------|----------|
| 1 | 데이터 수집 | X분 | 높음 |
| 2 | 변환/처리 | X분 | 중간 |
| 3 | 결과 전달 | X분 | 낮음 |

**Total**: 주 X시간, 월 Y시간 낭비
```

### Option B: Workflow Design

```markdown
## ⚙️ Workflow Design

**자동화 워크플로우**

(Mermaid 다이어그램 — Trigger → Collect → Process → Notify)

**핵심 설계 결정**

| 결정 포인트 | 선택 | 이유 |
|------------|------|------|
| 스케줄링 | cron/GitHub Actions | 이유 |
| 데이터 수집 | API/크롤링 | 이유 |
| 알림 | Discord/Slack/Email | 이유 |
| 에러 처리 | Retry + Alert | 이유 |
```

### Option C: System Architecture

```markdown
## 🏗️ System Architecture

**Architecture**

(Mermaid 다이어그램 — 시스템 구성도)

**Tech Stack**

| Component | Tool | Role |
|-----------|------|------|
| Scheduler | cron/Airflow/n8n | 실행 트리거 |
| Collector | Playwright/requests | 데이터 수집 |
| Processor | Python/pandas | 데이터 가공 |
| Storage | DB/Google Sheets | 결과 저장 |
| Notifier | Discord API/Slack | 알림 발송 |

**Core Logic** (핵심 자동화 코드 10-15줄)
```

### Option D: Efficiency Gains

```markdown
## 📊 Efficiency Gains

**시간 절약 분석**

| 작업 | Before | After | 절약 |
|------|--------|-------|------|
| 데이터 수집 | 30분/회 | 0분 (자동) | **-100%** |
| 데이터 처리 | 20분/회 | 2분 | **-90%** |
| 리포트 작성 | 1시간/회 | 5분 | **-92%** |

**월간 효과**: 주 X시간 → Y분, **월 Z시간 절약**

**정확도 향상**: 수작업 에러율 X% → 자동화 후 Y%
```

### Option E: Error Handling & Reliability

```markdown
## 🛡️ Error Handling & Reliability

**에러 처리 전략**

| 에러 유형 | 처리 방법 | Fallback |
|----------|----------|----------|
| 네트워크 타임아웃 | 3회 재시도 (exponential backoff) | 수동 알림 |
| 데이터 형식 변경 | 스키마 검증 + 경고 | 이전 포맷 유지 |
| 인증 만료 | 자동 갱신 | Discord 알림 |

**Monitoring**: 실행 로그 기록, 실패 시 즉시 알림, 주간 요약 리포트

**Uptime**: 운영 X개월, 성공률 Y%
```

### Option F: Scheduling & Operations

```markdown
## ⏰ Scheduling & Operations

**실행 스케줄**

| Job | Schedule | Duration | Status |
|-----|----------|----------|--------|
| 데이터 수집 | 매일 09:00 | ~2분 | ✅ 운영 중 |
| 리포트 생성 | 매주 월요일 | ~5분 | ✅ 운영 중 |
| DB 정리 | 매월 1일 | ~1분 | ✅ 운영 중 |

**운영 현황**: X개월째 안정 운영, 총 Y회 실행, 성공률 Z%
```

## 필수 마무리 섹션

```markdown
---

## 💡 Key Takeaways

**"핵심 학습 한 줄"**

자동화 설계 패턴, 에러 핸들링, 운영 안정성 확보 등

**한계 및 개선 방향**

• **현재 한계**: 구체적 제약사항
• **Next Step**: 확장 계획, 추가 자동화

---

## 🔗 Links

[GitHub](링크) | [실행 대시보드](링크) | [Discord Bot](링크)
```

## 구성 예시

**프로젝트 A** (가격 모니터링 봇):
Overview → Problem & Manual Process → Workflow Design → Efficiency Gains → Takeaways

**프로젝트 B** (데이터 파이프라인):
Overview → System Architecture → Error Handling → Scheduling → Takeaways

**프로젝트 C** (Discord/Slack 봇):
Overview → Feature Showcase(Type3에서 차용) → Workflow Design → Operations → Takeaways

## Metric Scale Reference (Type 5)

| 프로젝트 성격 | 적절한 스케일 | 비현실적 |
|--------------|-------------|---------|
| 개인 자동화 | 주 2-5시간 절약, 일 수십 건 처리 | 월 1,000시간 절약 |
| 봇/크롤러 | 일 100-1,000건, 에러율 <5% | 일 100만 건 처리 |
| 파이프라인 | 수분 내 완료, 월 수백 회 실행 | 실시간 스트리밍 처리 |

⚠️ "완전 자동화"보다 "적절한 자동화 + 사람의 판단"이 더 현실적이고 설득력 있음.
