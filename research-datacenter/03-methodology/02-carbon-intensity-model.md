# Sub-Model 2: Carbon Intensity Forecasting

---

## Problem Definition

The carbon intensity model predicts the carbon intensity of electricity generation (gCO2/kWh) for each Canadian province. For data center siting decisions, the relevant granularity is **monthly and seasonal averages with uncertainty bands**. The fundamental insight driving model design is that interprovincial differences are so large -- spanning a 200x range -- that seasonal averages capture most of the decision-relevant variation.

### Task Definition

- **Target variable:** Carbon intensity in gCO2/kWh per province per time period -- both average and marginal.
- **Prediction horizon:** Monthly and seasonal averages (MVP); hourly forecasts as a stretch goal for operational scheduling.
- **Output:** Point estimate plus 90% prediction interval for each province-month combination, for both average and marginal intensity.

---

## Provincial Carbon Intensity: The Core Insight

**Critical distinction: Average vs. Marginal Intensity.** The table below shows *average* grid intensity -- the standard accounting metric. However, Dandres et al. (2016, *Journal of Industrial Ecology*) demonstrate that the *marginal* electricity serving new data center loads in Canada is dominated by natural gas (47-55%) and coal (38-48%), producing 0.85-1.01 kg CO2-eq/kWh -- roughly 5-6x higher than the Canadian average of 0.16 kg CO2-eq/kWh. This is because new large loads don't build new hydro dams or nuclear plants; they are served by dispatchable fossil generation. Additionally, 60-70% of this marginal electricity comes from reduced electricity exports to the United States, triggering compensating fossil fuel generation south of the border.

**Design decision:** Our carbon intensity model forecasts *both* average and marginal intensity. Average intensity is useful for attributional accounting (reporting annual emissions). Marginal intensity is the methodologically appropriate metric for evaluating the consequential impact of *new* data center loads -- and is therefore the primary input to the composite SIS.

The table below illustrates why provincial variation dominates all other sources of variation in Canadian electricity carbon intensity (shown here as average intensity).

| Province | Approx. gCO2/kWh | Primary Generation Sources | Data Center Presence |
|---|---|---|---|
| Manitoba | ~1.4 | 97%+ hydroelectric | Low |
| Quebec | ~1.7 | 95%+ hydroelectric | High (Montreal) |
| British Columbia | ~15 | 90%+ hydroelectric | Medium (Vancouver) |
| Newfoundland & Labrador | ~18 | Hydro dominant | Low |
| Ontario | ~38 | Nuclear + hydro + natural gas | High (Toronto) |
| Yukon | ~70 | Hydro + diesel | Minimal |
| Northwest Territories | ~190 | Mixed generation | Minimal |
| New Brunswick | ~350 | Nuclear, hydro, gas, oil | Low |
| Prince Edward Island | ~350 | Imports + wind | Minimal |
| Alberta | ~490 | Natural gas dominant | High (Calgary) |
| Saskatchewan | ~670 | Coal + natural gas | Low |
| Nova Scotia | ~700 | Coal + natural gas dominant | Low |
| Nunavut | ~820 | Diesel generation | Minimal |

A 100 MW data center operating at PUE 1.3 in Alberta (~490 gCO2/kWh) produces approximately 560,000 tonnes of CO2 per year. The same facility in Quebec (~1.7 gCO2/kWh) produces approximately 1,900 tonnes -- a **295x difference**. This single factor often dominates the entire siting analysis.

---

## Model Selection

### Baseline: Prophet (Meta/Facebook)

Prophet is the recommended starting model for time-series carbon intensity forecasting.

```python
from prophet import Prophet
import pandas as pd

df = pd.DataFrame({'ds': timestamps, 'y': carbon_intensity_values})
model = Prophet(yearly_seasonality=True, weekly_seasonality=True)
model.fit(df)

future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)
# forecast contains yhat, yhat_lower, yhat_upper
```

**Advantages:**

- Built-in seasonality handling (daily, weekly, yearly) with automatic Fourier decomposition
- Holiday effects can be added with a few lines of code
- Produces uncertainty intervals out of the box -- critical for our Monte Carlo framework
- Handles missing data and outliers gracefully
- Minimal feature engineering required: just timestamps and target values
- 10 lines of code to get a working, publishable model

**Limitations:**

- Does not incorporate exogenous variables (weather, generation mix) without manual regressor addition
- Assumes additive or multiplicative seasonality -- may not capture structural grid transitions (e.g., coal plant retirement)

### Primary: XGBoost with Exogenous Features

For higher accuracy, XGBoost can incorporate external drivers of carbon intensity.

**Exogenous features:**

- Temperature and heating/cooling degree days
- Generation mix (share of gas, coal, hydro, nuclear, wind, solar)
- Import/export flows between provinces
- Time-of-day and seasonal indicators
- Planned outage schedules for nuclear and hydro facilities

Literature consistently shows that ensemble approaches combining XGBoost with temporal models outperform either approach alone.

---

## CarbonCast: Key Open-Source Reference

CarbonCast (Maji et al. 2022, ACM BuildSys) is the most relevant existing system for our work.

### Architecture

CarbonCast uses a two-tier forecasting approach:

1. **Tier 1:** Forecasts electricity production by generation source (solar, wind, gas, coal, hydro, nuclear) using source-specific models.
2. **Tier 2:** Combines Tier 1 production forecasts with weather data to produce carbon intensity forecasts.

Each tier uses a CNN-LSTM hybrid architecture that captures both spatial patterns (CNN) and temporal dependencies (LSTM).

### Performance

| Forecast Horizon | MAPE Range | Notes |
|---|---|---|
| 24-hour ahead | 4.80-8.20% | Best performance on stable grids |
| 48-hour ahead | 6.10-10.50% | Moderate degradation |
| 96-hour ahead | 8.30-13.93% | Acceptable for operational planning |

### Practical Advantages

- **Robust to noisy and missing inputs:** Important for Canadian data, where some provinces have gaps in hourly reporting.
- **Open source:** Code available at https://github.com/carbonfirst/CarbonCast
- **Adaptable:** Originally trained on US regions but architecture is transferable to Canadian provinces with retraining.

### Adaptation for This Project

- Replace US ISO data sources with IESO (Ontario), AESO (Alberta), and Hydro-Quebec APIs.
- Retrain Tier 1 models on Canadian generation mix data.
- Use ECCC (Environment and Climate Change Canada) published emission factors for calibration.

---

## Published Performance Benchmarks

| Model | Architecture | Metric | Value | Source |
|---|---|---|---|---|
| CarbonCast | CNN-LSTM two-tier | MAPE | 4.80-13.93% | Maji et al. 2022 |
| Ensemble (weighted) | XGBoost 51% + LSTM 28% + SARIMA 21% | R-squared | 0.96 | Jones 2025 |
| LSTM-GAT | LSTM + Graph Attention Network | Classification accuracy | 89.5% | Wu et al. 2024 |
| TFT | Temporal Fusion Transformer | State-of-the-art | Interpretable attention | Applied Soft Computing 2024 |

The ensemble approach (Jones 2025) is particularly relevant because it demonstrates that combining a tree-based model (XGBoost) with a sequence model (LSTM) and a statistical baseline (SARIMA) yields better results than any single architecture.

---

## Forecasting Horizon Relevance

Different forecasting horizons serve different purposes in the data center siting context.

| Horizon | Use Case | Relevance to Siting |
|---|---|---|
| Hourly | Operational workload scheduling (shift compute to low-carbon hours) | Stretch goal |
| Daily/Weekly | Seasonal pattern capture and validation | Model training |
| Monthly/Seasonal | Siting decisions -- captures fundamental provincial differences | **Primary target** |
| Annual | Long-term planning and policy analysis | Calibration |

**Recommendation for MVP:** Monthly and seasonal averages with uncertainty bands. This granularity captures the dominant provincial variation that drives siting decisions. Hourly forecasting adds complexity without changing the siting recommendation in most cases, since interprovincial differences dwarf intra-day variation.

---

## ElectricityMap Methodology

ElectricityMap is a widely-used open-source platform for real-time carbon intensity tracking that provides a useful reference implementation.

### Data Pipeline

1. **Raw production data** collected from official government and TSO sources (IESO, AESO, Hydro-Quebec, etc.).
2. **Flow-tracing algorithm** for consumption-based carbon accounting -- attributes imported electricity's carbon intensity to the consuming region.
3. **Life-cycle emission factors** that include construction, fuel extraction, operations, and decommissioning -- not just combustion emissions.

### Coverage

- Already covers Ontario (IESO zone) and Alberta (AESO zone).
- Open-source parsers available for Canadian zones.
- Historical data available from 2021 onward for most Canadian provinces.

### Relevance to This Project

ElectricityMap's historical data can serve as training data for our Prophet and XGBoost models. Their flow-tracing methodology is more sophisticated than simple average emission factors, accounting for cross-border electricity trade.

---

## MVP Implementation

### Data Pipeline

1. Download ElectricityMap historical data (2021-2024) for all available Canadian zones -- including both average and marginal intensity where available.
2. Supplement with IESO, AESO, and Hydro-Quebec hourly generation data.
3. Use ECCC published National Inventory Report emission factors as ground truth for annual calibration of average intensity.
4. Use Electricity Maps marginal intensity estimates (available for CA-ON, CA-AB) as training targets for marginal models.

### Model Training

1. Train Prophet on each province's time series independently (average intensity).
2. Train XGBoost with exogenous features on provinces with sufficient data (Ontario, Alberta, Quebec).
3. For Ontario and Alberta, train a parallel marginal intensity model using Electricity Maps marginal data as target.
4. For provinces without marginal data, apply a marginal multiplier derived from Dandres et al.: marginal intensity is approximately 2-5x average intensity in mixed-source grids (ON, QC, NB), and converges toward 1x in pure fossil grids (AB, SK) where average and marginal are already similar.
5. For data-scarce provinces, fall back to Prophet-only with wider uncertainty bands.
6. Temporal train/test split: train on 2021-2023, test on 2024.

### Output Specification

For each province and each month:

- Average carbon intensity estimate (gCO2/kWh) with 90% prediction interval
- Marginal carbon intensity estimate (gCO2/kWh) with 90% prediction interval (primary metric for SIS)
- Data quality flag (high/medium/low based on source data availability)
- Marginal data source flag (direct model / multiplier fallback)

### Evaluation Metrics

| Metric | Description |
|---|---|
| MAE | Mean absolute error (gCO2/kWh) -- primary metric |
| RMSE | Root mean squared error -- penalizes large deviations |
| Calibration | Fraction of actual values falling within predicted 90% interval (target: 0.90) |
| Coverage | Proportion of province-months with sufficient data to produce a forecast |

---

## Key References

- **Dandres, T. et al. 2016,** "Consequences of Future Data Center Deployment in Canada on Electricity Generation and Environmental Impacts," *Journal of Industrial Ecology* 20(5), 1312-1322. -- Foundational reference for marginal vs. average intensity in Canadian DC context. Established that marginal generation is 85-100% fossil-fueled with 60-70% from reduced US exports.
- Maji, S. et al. 2022, "CarbonCast: Multi-Day Forecasting of Grid Carbon Intensity," *ACM BuildSys*. https://github.com/carbonfirst/CarbonCast
- Jones, S. 2025, "Ensemble Methods for Regional Carbon Intensity Forecasting."
- Wu, H. et al. 2024, "Graph Attention Networks for Spatiotemporal Carbon Intensity Prediction."
- ElectricityMap methodology: https://www.electricitymaps.com/methodology
- ECCC National Inventory Report: https://www.canada.ca/en/environment-climate-change/services/climate-change/greenhouse-gas-emissions/inventory.html
