# Focus Valley — Pomodoro Timer Web App

> 💡 **"식물이 자라는 포모도로 타이머 — React + Canvas API로 몰입형 집중 경험 구현"**
>
> 게이미피케이션과 시각적 피드백으로 집중 시간을 눈에 보이는 성장으로 전환

---

## 🎯 Performance Overview

**30초 스캔용 - 프로덕트 성과**

| Metric | Value | Note |
|--------|-------|------|
| 핵심 기능 | 5개 | 타이머, 식물 성장, 통계, 사운드, 다크모드 |
| 기술 스택 | React, Canvas API, Vercel | SPA + 클라이언트 사이드 렌더링 |
| 배포 | Vercel (라이브) | 반응형 웹 (모바일 대응) |
| 개발 기간 | 3주 | 기획 1주 + 개발 2주 |

**Impact Summary**: 기존 포모도로 앱의 "타이머만 돌아가는" 단조로움 → 집중할수록 식물이 성장하는 시각적 보상 → 사용자가 집중 과정을 즐기는 경험 설계

---

## ✨ Feature Showcase

**Feature 1: 실시간 식물 성장 애니메이션**

• **What**: 25분 집중 세션 동안 Canvas API로 식물이 단계별로 성장
• **How**: requestAnimationFrame + 타이머 진행률 연동, 5단계 성장 스프라이트
• **Impact**: 집중 시간이 눈에 보이는 결과물로 전환 → 지속 동기 부여

**Feature 2: 집중 통계 대시보드**

• **What**: 일별/주별 집중 시간, 완료 세션 수, 연속 달성 기록
• **How**: localStorage 기반 데이터 저장 + Chart.js 시각화
• **Impact**: 자기 성장 추적 가능, 습관 형성 지원

```jsx
// Canvas 식물 성장 렌더링 핵심 로직
const drawPlant = (ctx, progress) => {
  const stage = Math.floor(progress * 5); // 0~4단계
  const height = BASE_HEIGHT + (MAX_HEIGHT - BASE_HEIGHT) * progress;
  
  // 줄기 → 잎 → 꽃 순서로 렌더링
  drawStem(ctx, height, COLORS[stage]);
  if (stage >= 2) drawLeaves(ctx, height, stage - 1);
  if (stage >= 4) drawFlower(ctx, height);
};
```

---

## 🏗️ Architecture & Tech Stack

**Tech Decisions**

| Layer | Choice | Why |
|-------|--------|-----|
| Framework | React (Vite) | 빠른 HMR, 가벼운 번들 사이즈 |
| Animation | Canvas API | DOM 조작 대비 60fps 부드러운 렌더링 |
| State | Context API | Redux 과도, 컴포넌트 5-6개 규모에 적합 |
| Deploy | Vercel | GitHub 연동 자동 배포, 무료 |
| Sound | Web Audio API | 외부 라이브러리 없이 알림음 구현 |

**Technical Challenge: Canvas 성능 최적화**

초기 구현에서 Canvas 리렌더링이 CPU 15%까지 차지. requestAnimationFrame 조건부 호출 + 오프스크린 캔버스 캐싱으로 CPU 사용률 **3% 이하**로 최적화.

---

## 💡 Key Takeaways

**"Canvas API와 React의 조합에서 성능과 UX를 동시에 잡는 법을 배웠다"**

React의 선언적 UI와 Canvas의 명령형 렌더링이 충돌하는 지점에서, useRef로 Canvas 인스턴스를 관리하고 useEffect로 애니메이션 루프를 제어하는 패턴을 체득. 게이미피케이션 요소가 단순한 도구의 재사용률을 크게 높인다는 프로덕트 인사이트도 얻음.

**한계 및 개선 방향**

• **현재 한계**: localStorage 한계로 디바이스 간 동기화 불가
• **Next Step**: Supabase 연동으로 클라우드 동기화, PWA 변환으로 오프라인 지원

---

## 🔗 Links

[Live Demo](https://focus-valley.vercel.app) | [GitHub](https://github.com/Taek-D/focus-valley)
