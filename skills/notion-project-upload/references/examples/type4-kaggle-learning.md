# Kaggle Tabular Playground Series - Time Series Forecasting 학습

> 💡 **"시계열 예측 기법을 Kaggle 경진대회로 마스터"**
>
> Prophet, XGBoost, LSTM 앙상블로 RMSE 0.237 달성, 3,200명 중 상위 8% (263등), 시계열 분석 역량 실무 적용 준비 완료

---

## 🎯 Goal & Context

**Why I Started This**

실무에서 재고 예측, 수요 예측 프로젝트를 진행하면서 시계열 데이터 특유의 트렌드, 계절성, 노이즈 처리에 어려움을 겪음. Pandas의 기본 rolling mean만 사용했고, ARIMA, Prophet 같은 전문 시계열 모델은 이론만 알고 실전 경험 부족.

Kaggle Tabular Playground Series (2024년 6월) 대회가 시계열 예측 주제로 진행되어, 실전 데이터로 다양한 기법을 체계적으로 학습할 기회로 판단.

**Learning Goals**

• **기술 목표**: 
  - ARIMA, SARIMA, Prophet 모델 구현 및 하이퍼파라미터 튜닝
  - LSTM/GRU 딥러닝 시계열 모델 학습
  - Feature Engineering for Time Series (Lag, Rolling, Fourier)
  - 앙상블 기법 (Stacking, Blending)

• **실무 목표**: 
  - 재고 예측 모델에 Prophet 적용 (목표: MAPE 12% → 8%)
  - 트렌드/계절성 분해 능력으로 비즈니스 인사이트 도출

• **성과 목표**: 
  - Kaggle 상위 10% 진입 (Bronze Medal)
  - 5개 이상 서로 다른 접근법 실험
  - 재사용 가능한 시계열 분석 파이프라인 구축

---

## 📊 Learning Journey

**Learning Path**

| Phase | Focus | Duration | Key Milestone |
|-------|-------|----------|---------------|
| Week 1-2 | 이론 학습 & EDA | 2주 | Coursera "Time Series" 수료, 데이터 분석 완료 |
| Week 3-4 | Classical Methods | 2주 | ARIMA/SARIMA 구현, Baseline RMSE 0.312 |
| Week 5-6 | ML & DL Models | 2주 | XGBoost 0.258, LSTM 0.271 달성 |
| Week 7-8 | Ensemble & Tuning | 2주 | 3모델 Stacking → RMSE 0.237, 상위 8% |
| **Total** | | **8주** | **263/3,200등, Bronze Medal** |

**Resources Used**

• **Primary**: 
  - Coursera "Practical Time Series Analysis" (Duke University)
  - Kaggle Learn "Time Series" 코스
  - "Forecasting: Principles and Practice" (Hyndman & Athanasopoulos)

• **Supplementary**: 
  - Prophet 공식 문서 + 튜토리얼 10개
  - LSTM for Time Series 논문 3편
  - Kaggle Discussion 및 Notebook 50+ 개 참고

• **Total Time**: 120시간 (주 15시간 × 8주)

---

## 💡 Key Learnings

### Before & After

**Before Learning**

• 시계열 지식: Pandas rolling mean, 단순 선형 회귀만 사용
• 계절성 처리: 월별 더미 변수로 무식하게 처리
• 검증 방법: Train/Test Split만 사용 (Time Series CV 모름)
• 딥러닝: LSTM이 뭔지는 알지만 구현 경험 전무

**After Learning**

• 시계열 전문 모델: Prophet, SARIMA, LSTM 모두 구현 가능
• Feature Engineering: 15가지 시계열 피처 (Lag, Rolling, Fourier, Holiday 등)
• 검증 전략: Time Series Cross-Validation + Walk-Forward 검증 숙달
• 앙상블: 3개 모델 Stacking으로 개별 모델 대비 **+8% 성능 향상**
• **정량적 성과**: Competition RMSE 0.312 (Baseline) → 0.237 (Final) **-24%**

---

### Core Concepts Mastered

**Concept 1: Time Series Feature Engineering**

**What I Learned**

시계열 데이터는 과거 관측값(Lag)과 통계량(Rolling)이 핵심 예측 변수. Fourier Transform으로 복잡한 계절성도 수학적으로 모델링 가능.

**How I Applied**

```python
import pandas as pd
import numpy as np

def create_time_features(df, date_col, target_col, lags=[1, 7, 14, 30]):
    """
    시계열 피처 엔지니어링 파이프라인
    """
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.sort_values(date_col)
    
    # 1. Lag Features
    for lag in lags:
        df[f'lag_{lag}'] = df[target_col].shift(lag)
    
    # 2. Rolling Statistics (7일, 30일)
    for window in [7, 30]:
        df[f'rolling_mean_{window}'] = df[target_col].rolling(window).mean()
        df[f'rolling_std_{window}'] = df[target_col].rolling(window).std()
        df[f'rolling_min_{window}'] = df[target_col].rolling(window).min()
        df[f'rolling_max_{window}'] = df[target_col].rolling(window).max()
    
    # 3. Time-based Features
    df['day_of_week'] = df[date_col].dt.dayofweek
    df['day_of_month'] = df[date_col].dt.day
    df['month'] = df[date_col].dt.month
    df['quarter'] = df[date_col].dt.quarter
    df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)
    
    # 4. Fourier Features for Seasonality (연주기)
    df['sin_day_of_year'] = np.sin(2 * np.pi * df[date_col].dt.dayofyear / 365.25)
    df['cos_day_of_year'] = np.cos(2 * np.pi * df[date_col].dt.dayofyear / 365.25)
    
    return df

# 적용 결과
df_featured = create_time_features(df, 'date', 'sales', lags=[1, 7, 14, 30])
print(f"Original features: 2, After engineering: {df_featured.shape[1]}")
# Output: Original features: 2, After engineering: 23

# Impact: XGBoost RMSE 0.298 → 0.258 (-13%)
```

**Impact**
• Feature 수: 2개 → 23개 생성
• XGBoost 성능: RMSE 0.298 → 0.258 (**-13%**)
• **Key Insight**: Lag 7일과 30일이 가장 중요한 피처 (Feature Importance 상위 2개)

---

**Concept 2: Facebook Prophet for Seasonality**

**What I Learned**

Prophet은 트렌드, 연/주/일 계절성, 휴일 효과를 자동으로 모델링. 가법 모델 (Additive) 구조로 직관적 해석 가능.

**How I Applied**

```python
from prophet import Prophet
import pandas as pd

def train_prophet_model(df, holidays=None):
    """
    Prophet 모델 학습 및 예측
    """
    # Prophet 요구 형식: ds (date), y (target)
    df_prophet = df[['date', 'sales']].rename(columns={'date': 'ds', 'sales': 'y'})
    
    # 모델 초기화 및 하이퍼파라미터
    model = Prophet(
        seasonality_mode='multiplicative',  # 계절성이 트렌드에 비례
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False,
        changepoint_prior_scale=0.05,  # 트렌드 변화 민감도
        holidays=holidays  # 공휴일 효과
    )
    
    # 커스텀 계절성 추가 (월별)
    model.add_seasonality(name='monthly', period=30.5, fourier_order=5)
    
    # 학습
    model.fit(df_prophet)
    
    # 미래 예측 (30일)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    
    return model, forecast

# 한국 공휴일 정보 추가
holidays = pd.DataFrame({
    'holiday': 'new_year',
    'ds': pd.to_datetime(['2024-01-01', '2024-02-09', '2024-02-10']),
    'lower_window': 0,
    'upper_window': 1,
})

model, forecast = train_prophet_model(train_df, holidays)

# 성능 평가
from sklearn.metrics import mean_squared_error
y_true = test_df['sales'].values
y_pred = forecast['yhat'][-len(test_df):].values
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
print(f"Prophet RMSE: {rmse:.3f}")
# Output: Prophet RMSE: 0.264
```

**Impact**
• 단독 모델 성능: RMSE 0.264 (ARIMA 0.312 대비 **-15%** 개선)
• 계절성 자동 감지: 주간 패턴 (주말 -18% 판매량) 발견
• **Key Insight**: 공휴일 정보 추가로 RMSE 추가 -3% 개선

---

**Concept 3: LSTM Neural Network for Sequences**

**What I Learned**

LSTM은 장기 의존성(Long-term Dependencies)을 학습 가능한 RNN 변형. 시계열의 순서 정보를 완전히 활용.

**How I Applied**

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def create_sequences(data, seq_length=30):
    """
    LSTM 입력용 시퀀스 생성
    seq_length: 과거 몇 일을 입력으로 사용할지
    """
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

# 데이터 정규화 (LSTM은 scaling 필수)
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(train_df[['sales']].values)

# 시퀀스 생성 (과거 30일 → 다음 1일 예측)
X_train, y_train = create_sequences(scaled_data, seq_length=30)

# LSTM 모델 구축
model = Sequential([
    LSTM(128, return_sequences=True, input_shape=(30, 1)),
    Dropout(0.2),
    LSTM(64, return_sequences=False),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# 학습
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    verbose=0
)

print(f"Best Val Loss: {min(history.history['val_loss']):.4f}")
# Output: Best Val Loss: 0.0023 (scaled)

# 예측 및 역정규화
X_test, y_test = create_sequences(scaled_test_data, seq_length=30)
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)

# 성능
rmse = np.sqrt(mean_squared_error(y_test_original, predictions))
print(f"LSTM RMSE: {rmse:.3f}")
# Output: LSTM RMSE: 0.271
```

**Impact**
• 단독 성능: RMSE 0.271 (Prophet보다 약간 낮음)
• 앙상블 효과: Prophet + XGBoost + LSTM 스태킹 시 **+8%** 추가 개선
• **Key Insight**: LSTM은 급격한 트렌드 변화 감지에 강함 (예: 프로모션 기간)

---

## 📈 Results & Achievements

### Quantitative Outcomes

| Metric | Target | Achieved | Status |
|--------|--------|----------|--------|
| Competition Rank | Top 20% (640등) | **Top 8% (263등)** | ✅ 초과달성 |
| RMSE Score | 0.280 이하 | **0.237** | ✅ 초과달성 |
| 모델 실험 수 | 5개 | **8개** | ✅ 초과달성 |
| 학습 완료율 | 100% | **100%** | ✅ 달성 |
| Notebook 공유 | 1개 | **3개** | ✅ 초과달성 |

### Qualitative Achievements

• **Medal**: Bronze Medal (상위 10% 이내 수상)
• **Community**: Kaggle Discussion 답변 5개 (Upvotes 총 89개)
• **Knowledge Sharing**: Medium 블로그 "시계열 Feature Engineering 완벽 가이드" (조회수 2,800+, 클랩 127개)
• **GitHub**: 시계열 분석 파이프라인 오픈소스 공개 (Stars 34개, Forks 8개)
• **Recognition**: Kaggle Notebooks Expert 등급 달성 (3개 Notebook 합산 Upvotes 200+)

---

## 🔄 Real-world Application

**실무 적용 계획**

**적용 1: 재고 예측 모델 개선**

**현재 상황**: 단순 이동 평균 기반 예측, MAPE 12.3%

**적용 계획**:
• Prophet으로 계절성 모델링 (연/월/주 패턴)
• 프로모션, 공휴일 정보를 외부 변수로 추가
• XGBoost로 날씨, 경쟁사 가격 등 추가 피처 반영

**기대 효과**:
• MAPE 12.3% → 8.5% 목표 (**-31% 개선**)
• 재고 부족 발생 -40% (현재 월 15건 → 9건)
• 과잉 재고 비용 월 $8K 절감

**Timeline**: 
• Week 1-2: 데이터 수집 및 정제
• Week 3-4: Prophet + XGBoost 모델 개발
• Week 5-6: A/B 테스트 (신규 모델 vs 기존 모델)
• Week 7+: 점진적 배포 및 모니터링

---

**적용 2: 수요 예측 대시보드 구축**

**현재 상황**: 엑셀 기반 수동 예측, 업데이트 주 1회

**적용 계획**:
• Streamlit으로 실시간 예측 대시보드 개발
• Prophet 모델 API화 (FastAPI)
• 일일 자동 재학습 파이프라인 (Airflow)

**기대 효과**:
• 예측 업데이트 주기: 주 1회 → 매일 (**7배 향상**)
• 담당자 작업 시간: 주 4시간 → 30분 (**-88%**)
• 예측 정확도 향상으로 매출 기회 손실 -15%

**Timeline**:
• Week 1-2: Streamlit 대시보드 프로토타입
• Week 3: FastAPI 모델 서빙 개발
• Week 4: Airflow 파이프라인 구축
• Week 5+: 운영 팀 교육 및 피드백 수집

---

**Immediate Next Steps**

✅ **Week 1**: 재고 데이터 6개월치 수집 및 EDA (완료)
⏳ **Week 2**: Prophet Baseline 모델 구축 (진행중)
📅 **Week 3-4**: XGBoost 피처 엔지니어링 및 앙상블
📅 **Month 2**: A/B 테스트 진행 및 결과 분석
📅 **Month 3**: 프로덕션 배포 및 모니터링 체계 구축

---

## 🧠 Key Takeaways

**Technical Insights**

• **Prophet의 강점**: 트렌드 + 계절성 자동 감지, 해석 가능성 높음 → 비즈니스 팀 설득 용이
• **XGBoost의 강점**: 외부 변수 (날씨, 프로모션) 통합 용이, Feature Importance로 인사이트 도출
• **LSTM의 강점**: 급격한 패턴 변화 감지 (예: 바이럴 이벤트) → 앙상블 시 보완 효과

**Learning Process Insights**

• **효과적이었던 방법**: 
  - "이론 1일 → 실습 2일" 비율로 빠른 피드백 루프
  - Kaggle Discussion에서 다른 참가자의 접근법 매일 30분 학습
  - 실험 로그를 Notion에 정리 (8주간 총 47개 실험 기록)

• **어려웠던 부분**: 
  - LSTM 하이퍼파라미터 튜닝 (Layer 수, Units, Dropout) → Grid Search로 해결
  - Time Series CV 구현 (미래 데이터 누출 방지) → Sklearn의 TimeSeriesSplit 활용

• **다음 학습 개선점**: 
  - 이론 학습 시간 줄이고 실전 문제부터 시작 (Project-based Learning)
  - 매주 1개씩 블로그 포스팅으로 학습 내용 정리 → Retention 향상

**Career Growth**

• **역량 향상**: Data Analyst → "시계열 전문" 역량 보유 (LinkedIn 프로필 업데이트)
• **협업 개선**: 재고 팀과 "예측 모델" 공통 언어로 소통 가능
• **Next Step**: GNN (Graph Neural Network) 학습 → 네트워크 효과 모델링

---

## 🤝 Community Impact

**학습 내용을 커뮤니티에 환원**

**Kaggle Contribution**
• **Discussion 답변**: 5개 포스팅 (Upvotes 총 89개)
  - "시계열 CV 실수 피하기" (34 Upvotes)
  - "Prophet vs ARIMA 선택 가이드" (28 Upvotes)
  - "LSTM 오버피팅 방지 팁" (27 Upvotes)

• **Notebook 공유**: 3개 Public Notebook
  - "Time Series Feature Engineering Toolkit" (Upvotes 67, Forks 23)
  - "Prophet + XGBoost Ensemble" (Upvotes 52, Forks 18)
  - "LSTM for Tabular Time Series" (Upvotes 41, Forks 12)

**Medium 블로그**
• "시계열 Feature Engineering 완벽 가이드" (조회수 2,800+, 클랩 127개)
• "Kaggle에서 배운 시계열 예측 실전 팁 10가지" (조회수 1,600+, 클랩 83개)

**GitHub 오픈소스**
• `timeseries-toolkit` 라이브러리 공개 (Stars 34, Forks 8)
  - Feature Engineering 자동화
  - Prophet/ARIMA/LSTM 통합 인터페이스
  - Time Series CV 헬퍼 함수

**사내 ML 스터디**
• "시계열 분석 입문" 세션 리드 (참여자 12명, 만족도 4.7/5.0)
• 학습 자료 및 코드 예제 공유 (Confluence 페이지 조회수 180+)

---

## 🔗 Links

[Kaggle Profile](https://www.kaggle.com/username) | [Competition Page](링크) | [GitHub Repo](https://github.com/username/timeseries-toolkit) | [Medium Blog](링크) | [Best Notebook](링크)
