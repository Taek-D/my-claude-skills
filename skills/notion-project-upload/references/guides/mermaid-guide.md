# Mermaid Diagram Guide

## Diagram Types & When to Use

| Type | When | Example Use |
|------|------|-------------|
| **Flowchart** | 프로세스, 의사결정 | 데이터 파이프라인, 분석 흐름 |
| **Sequence** | API/시스템 상호작용 | 캐싱 레이어, API 호출 흐름 |
| **Graph** | 아키텍처, 데이터 흐름 | Before/After 비교 |
| **Gantt** | 타임라인, 일정 | 프로젝트 일정, 학습 로드맵 |
| **State** | 상태 전환 | 주문 상태, 사용자 여정 |
| **ER** | 데이터 모델 | DB 스키마, 테이블 관계 |

## 프로젝트별 추천

| Type | 추천 다이어그램 |
|------|---------------|
| Type 1 | Graph (Before/After), Flowchart (파이프라인), Sequence (API) |
| Type 2 | Flowchart (분석 프로세스), Graph (데이터 소스), State (사용자 여정) |
| Type 3 | Sequence (API 흐름), Graph (시스템 아키텍처), State (유저 플로우) |
| Type 4 | Flowchart (학습 프로세스), Graph (모델 구조), Gantt (학습 타임라인) |
| Type 5 | Flowchart (자동화 워크플로우), Sequence (시스템 연동), Graph (아키텍처) |

## 핵심 문법

### Flowchart (Type 1, 2, 5에 추천)
```mermaid
graph TB
    A[Raw Data] --> B{Null 존재?}
    B -->|Yes| C[Null 처리]
    B -->|No| D[Feature Engineering]
    C --> D
    D --> E[모델 학습]
```

방향: `TB`(위→아래), `LR`(왼→오른), 노드: `[]`사각, `{}`마름모(조건)

### Sequence Diagram (Type 3, 5에 추천)
```mermaid
sequenceDiagram
    Client->>API: Request
    API->>Cache: Check
    alt Cache Hit
        Cache-->>API: Result
    else Cache Miss
        API->>DB: Query
        DB-->>API: Data
    end
    API-->>Client: Response
```

### Graph - System Architecture (Type 3에 추천)
```mermaid
graph LR
    A[React Frontend] -->|API Call| B[FastAPI Backend]
    B -->|Query| C[(PostgreSQL)]
    B -->|Cache| D[(Redis)]
    A -->|Deploy| E[Vercel]
    B -->|Deploy| F[Railway]
```

### Graph - Automation Workflow (Type 5에 추천)
```mermaid
graph TB
    A[⏰ Cron Trigger] --> B[🔍 Data Collection]
    B --> C{Data Changed?}
    C -->|Yes| D[📊 Processing]
    C -->|No| E[📝 Log]
    D --> F[🔔 Alert]
    D --> G[💾 Storage]
```

### Graph - Before/After (Type 1에 추천)
```mermaid
graph TB
    A[Client] -->|8.2초| B[Old System]
    style B fill:#ff6b6b

    C[Client] -->|1.3초| D[New System]
    style D fill:#51cf66
```

### State Diagram (Type 3 유저 플로우에 추천)
```mermaid
stateDiagram-v2
    [*] --> Landing
    Landing --> SignUp: 회원가입
    Landing --> Browse: 둘러보기
    SignUp --> Onboarding
    Onboarding --> Dashboard
    Browse --> SignUp: 관심 발생
    Dashboard --> Feature: 기능 사용
    Feature --> Dashboard: 완료
```

### Gantt (Type 4에 추천)
```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    section 분석
    성능 분석 :done, a1, 2024-01-01, 5d
    section 개발
    구현 :done, dev1, after a1, 7d
    section 배포
    테스트 :active, t1, after dev1, 4d
```

## Best Practices

**✅ DO**:
- Before/After는 색상으로 구분 (빨강: 문제 `#ff6b6b`, 초록: 개선 `#51cf66`)
- 노드에 성과 수치 포함 (`-->|1.3초|`)
- 한 다이어그램 = 한 메시지
- 노드 15개 이하
- Type 5는 이모지로 단계 구분 (⏰🔍📊🔔💾)

**❌ DON'T**:
- 모든 노드에 색상 → 3가지만 (빨강/초록/파랑)
- 노드 30개+ → 여러 다이어그램으로 분리
- 약어만 사용 → 풀네임 사용 (USR → User)
