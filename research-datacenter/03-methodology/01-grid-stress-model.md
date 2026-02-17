# Sub-Model 1: Grid Stress Prediction

---

## Problem Definition

The grid stress model addresses a binary classification task: predict whether a given provincial grid region will be in a **high-stress** or **normal** state during a given hour. The model outputs a probability of high stress, which is then used to assess the marginal impact of adding data center load to the grid.

### Label Definition

- **Binary target:** 1 if high-stress, 0 otherwise.
- A grid hour is labeled high-stress if **any** of the following conditions hold:
  - Demand-to-available-capacity ratio exceeds a threshold (e.g., > 0.90)
  - Reserve margin falls below a minimum threshold (e.g., < 5%)
  - A price spike event occurs (e.g., price > 3x rolling 30-day average)
  - An emergency alert or capacity warning is issued by the ISO
  - Carbon intensity spikes above a seasonal threshold (indicating reliance on peaker plants)

These conditions capture both reliability risk (low reserves, high demand) and economic/environmental stress (price spikes, dirty peaker dispatch).

---

## Data Sources

### IESO (Ontario)

- Hourly demand, generation mix, reserve information, and market signals
- Historical depth: 2010 to present
- Access: Free CSV/XML downloads, no API key required
- Covers the Toronto corridor (~40% of Canadian data center capacity)

### AESO (Alberta)

- Hourly generation metered volumes, pool price, aggregate internal load
- Historical depth: 2001 to present
- Access: Free standard datasets; custom extracts available at $100/hr
- Covers the Calgary corridor (~25% of pipeline capacity)

### Programmatic Access

The `gridstatus` Python library provides a unified interface to both ISOs:

```python
import gridstatus

# Ontario
ieso = gridstatus.IESO()
fuel_mix = ieso.get_fuel_mix(start="2023-01-01", end="2024-01-01")
load = ieso.get_load(start="2023-01-01", end="2024-01-01")

# Alberta
aeso = gridstatus.AESO()
lmp = aeso.get_lmp(start="2023-01-01", end="2024-01-01")
```

Installation: `pip install gridstatus` (MIT license, open source).

---

## Feature Engineering

Features are organized into five categories. All features are computed at hourly granularity.

### Temporal Features

| Feature | Description |
|---|---|
| `hour_of_day` | 0-23, cyclically encoded (sin/cos) |
| `day_of_week` | 0-6, cyclically encoded |
| `month` | 1-12, cyclically encoded |
| `season` | Categorical: winter, spring, summer, fall |
| `is_holiday` | Binary flag for statutory holidays |
| `is_weekend` | Binary flag for Saturday/Sunday |

### Demand Features

| Feature | Description |
|---|---|
| `demand_current` | Current hour system demand (MW) |
| `demand_rolling_24h` | Rolling 24-hour average demand |
| `demand_rolling_7d` | Rolling 7-day average demand |
| `demand_lag_1h` | Demand 1 hour ago |
| `demand_lag_24h` | Demand 24 hours ago |
| `demand_lag_168h` | Demand 1 week ago |
| `demand_delta_1h` | Hour-over-hour demand change |

### Supply Features

| Feature | Description |
|---|---|
| `reserve_margin` | (Available capacity - demand) / available capacity |
| `total_available_capacity` | Total dispatchable generation (MW) |
| `nuclear_share` | Nuclear generation as fraction of total |
| `hydro_share` | Hydro generation as fraction of total |
| `gas_share` | Natural gas generation as fraction of total |
| `renewable_share` | Wind + solar as fraction of total |

### Weather Features

| Feature | Description |
|---|---|
| `temperature` | Outdoor dry-bulb temperature (degrees C) |
| `hdd` | Heating degree days (base 18C) |
| `cdd` | Cooling degree days (base 18C) |

### Market Features

| Feature | Description |
|---|---|
| `price_current` | Current electricity price ($/MWh) |
| `price_lag_1h` | Price 1 hour ago |
| `price_lag_24h` | Price 24 hours ago |
| `price_volatility_24h` | Standard deviation of price over trailing 24 hours |

---

## Model Selection

### Primary: XGBoost (Gradient Boosted Trees)

- **Rationale:** Grid stress prediction is a tabular classification task with structured, well-defined features. XGBoost consistently achieves state-of-the-art performance on tabular data, offers native feature importance, and trains in minutes on datasets of this size.
- **Hyperparameter tuning:** Bayesian optimization over max_depth, learning_rate, n_estimators, min_child_weight, subsample, colsample_bytree.
- **Class imbalance handling:** High-stress hours are rare events (~5-15% of hours). Use SMOTE or class weighting to address imbalance.

### Alternative: LightGBM

- Faster training for large datasets, similar performance profile.
- Categorical feature handling without one-hot encoding.

### Why Not Deep Learning

LSTM and Transformer architectures have been applied to load forecasting, but for this binary classification task on tabular features:

- XGBoost matches or exceeds LSTM performance on structured tabular data (Grinsztajn et al., 2022).
- Interpretability is critical for a policy tool -- SHAP values from tree ensembles are more actionable than attention weights.
- Training and inference are orders of magnitude faster.
- Deep learning adds complexity without commensurate benefit for this problem structure.

---

## Published Performance Benchmarks

| Model | Task | Metric | Value | Source |
|---|---|---|---|---|
| Hybrid LSTM-XGBoost | Load forecasting | MAPE | 1.18% | Jang et al. 2024 |
| Hybrid LSTM-XGBoost | Load forecasting | R-squared | 0.994 | Jang et al. 2024 |
| Optimized XGBoost | Short-term load forecasting | MAPE | 2.61% | Scientific Reports 2022 |
| XGBoost ensemble | Day-ahead load forecasting | RMSE | <3% | Frontiers 2024 |
| Binary stress classification | Grid stress detection | F1 | 0.85-0.92 | Literature aggregate |

These benchmarks indicate that well-tuned XGBoost models achieve high accuracy on grid-related prediction tasks. The binary stress classification F1 range of 0.85-0.92 represents a realistic target for our model.

---

## Connection to Data Centers

The grid stress model does not operate in isolation. Its primary use is to quantify the **marginal impact** of adding data center load to an existing grid.

### Simulation Approach

1. Train the grid stress model on historical data (demand, supply, weather, price).
2. For a proposed data center of size X MW, add X to the demand feature for each hour.
3. Re-run the model with the augmented demand to obtain a new stress probability.
4. Compute the **marginal impact score**: difference between baseline stress probability and augmented stress probability.

### Load Scenarios

| Scenario | Added Load | Typical Facility |
|---|---|---|
| Small colocation | 10-25 MW | Single building |
| Medium enterprise | 50 MW | Campus |
| Large hyperscale | 100 MW | Regional hub |
| Mega campus | 200+ MW | Multi-building hyperscale |

The marginal impact is non-linear: adding 50 MW to a grid with 20% reserve margin has negligible effect, but adding 50 MW to a grid at 5% reserve margin could be catastrophic.

---

## MVP Implementation

### Scope

- Focus on Ontario (IESO) and Alberta (AESO) as the two provinces with the best hourly data availability and the largest data center markets.
- Extrapolate for other provinces using annual capacity-to-demand ratios from Statistics Canada and CER datasets.

### Train/Test Split

- **Temporal split:** Train on 2018-2022, test on 2023-2024.
- Strictly chronological -- no shuffled cross-validation, which would cause data leakage in time-series data.
- Validation set: final 6 months of training period for hyperparameter tuning.

### Evaluation Metrics

| Metric | Purpose |
|---|---|
| F1 Score | Primary metric, balances precision and recall for imbalanced classes |
| Precision | Proportion of predicted high-stress hours that are truly high-stress |
| Recall | Proportion of actual high-stress hours correctly identified |
| AUC-ROC | Discrimination ability across all thresholds |
| Confusion Matrix | Detailed breakdown of true/false positives and negatives |

### Deliverables

- Trained XGBoost model serialized via `joblib`
- SHAP feature importance plots
- Marginal impact curves: stress probability vs. added MW for each province
- Calibration plot: predicted probability vs. observed frequency

---

## Key References

- Jang et al. 2024, "Comparative Analysis of Deep Learning and Traditional ML Models for Short-Term Electrical Load Forecasting," *International Journal of Energy Research*. https://onlinelibrary.wiley.com/doi/full/10.1155/2024/5587728
- Nature Scientific Reports 2022, "Optimised XGBoost Model for Short-term Electric Load Forecasting." https://www.nature.com/articles/s41598-022-22024-3
- Frontiers in Energy Research 2024, "Evaluation of Electrical Load Demand Forecasting Using Various Machine Learning Approaches." https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2024.1408119/full
- Grinsztajn et al. 2022, "Why do tree-based models still outperform deep learning on tabular data?" *NeurIPS 2022*.
