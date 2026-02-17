# Composite Societal Impact Score

---

## Overview

The Societal Impact Score (SIS) aggregates the four sub-model outputs into a single, interpretable metric for comparing candidate data center locations. The score is designed to be transparent, configurable, and uncertainty-aware. Lower scores indicate more responsible siting.

---

## Score Definition

```
SIS = w_carbon * S_carbon + w_water * S_water + w_grid * S_grid + w_uncertainty * S_uncertainty
```

Where:

- Each `S` component is normalized to the range [0, 1].
- Each `w` weight is non-negative and all weights sum to 1.0.
- **Lower SIS = more responsible siting choice.**

---

## Component Definitions

### S_carbon: Normalized Carbon Emissions

```
Raw_carbon = Total_energy * PUE * marginal_carbon_intensity
S_carbon = normalize(Raw_carbon)
```

Total annual CO2 emissions from the facility, incorporating both the grid's carbon intensity (from Sub-Model 2) and the facility's energy overhead (from Sub-Model 3). **By default, S_carbon uses marginal carbon intensity** -- the emission rate of the generation that actually responds to new load -- rather than average grid intensity. Dandres et al. (2016) established that marginal intensity in Canada is 2-5x higher than average in mixed-source provinces, making this the methodologically appropriate metric for evaluating new data center loads. Average intensity is also computed and available for comparison.

**Cross-border impact flag:** For provinces with significant US electricity export relationships (Quebec, Ontario, British Columbia), the tool flags that S_carbon may underestimate the full consequential carbon impact due to export displacement effects -- where new Canadian load reduces exports, triggering compensating fossil generation in the US. Full consequential LCA with cross-border trade modeling is identified as future work.

### S_water: Normalized Water Harm

```
Raw_water = WUE * Total_energy * water_stress_multiplier
S_water = normalize(Raw_water)
```

Total annual water consumption weighted by local water stress (from Sub-Model 4). A facility consuming large volumes of water in a water-abundant region scores lower than one consuming moderate volumes in a water-stressed region.

### S_grid: Normalized Grid Stress

```
Raw_grid = stress_probability_with_dc - stress_probability_baseline
S_grid = normalize(Raw_grid)
```

The marginal increase in grid stress probability caused by adding the data center's load (from Sub-Model 1). This captures the risk that a new facility pushes an already-strained grid closer to reliability limits.

### S_uncertainty: Data Scarcity Penalty

```
S_uncertainty = normalized_prediction_variance
```

A penalty term for regions where sub-model predictions have high variance due to limited training data. This prevents the score from favoring a data-scarce region simply because the model has not seen enough data to identify risks. Provinces with sparse hourly data (e.g., Saskatchewan, territories) receive higher uncertainty penalties.

---

## Normalization

All component scores are normalized using min-max scaling across all candidate regions evaluated in a single analysis run.

```python
def normalize(values):
    """Min-max normalization to [0, 1] range."""
    min_val = min(values)
    max_val = max(values)
    if max_val == min_val:
        return [0.5] * len(values)  # All equal: assign midpoint
    return [(v - min_val) / (max_val - min_val) for v in values]
```

### Properties

- Normalization is **relative** to the set of candidates being compared. Adding or removing a candidate city can shift all scores.
- For absolute thresholds (e.g., "any SIS below 0.3 is acceptable"), use fixed reference points derived from best-case (Quebec hydropower, air-cooled, low water stress) and worst-case (Saskatchewan coal grid, evaporative cooling, high water stress) configurations.

---

## Weighting Strategies

The choice of weights reflects policy priorities. Four strategies are considered.

| Strategy | Description | Pros | Cons |
|---|---|---|---|
| Equal weights (0.25 each) | All dimensions weighted equally | No bias, easy to explain, transparent | Ignores relative importance of dimensions |
| AHP (Analytic Hierarchy Process) | Pairwise comparison matrix | Principled, widely cited in MCDA literature | Requires expert input, sensitivity to inconsistency |
| Stakeholder-defined | Weights derived from surveys | Democratic, reflects actual values | Requires actual stakeholder engagement |
| Entropy-based | Weights derived from data variance | Objective, fully reproducible | May not reflect policy priorities |

### Recommended Approach for MVP

**Default: Equal weights (0.25 each)** with an interactive slider in the dashboard allowing users to adjust weights in real time.

This approach avoids the need for expert elicitation while still enabling exploration of different policy priorities.

### Scenarios for Report and Presentation

For the final report, run and present **three weight scenarios** to demonstrate sensitivity:

| Scenario | w_carbon | w_water | w_grid | w_uncertainty | Rationale |
|---|---|---|---|---|---|
| Climate-first | 0.40 | 0.30 | 0.20 | 0.10 | Prioritizes emissions reduction, consistent with Net-Zero 2050 targets |
| Grid-reliability-first | 0.20 | 0.20 | 0.40 | 0.20 | Prioritizes grid stability, relevant post-Ontario Bill 40 |
| Equal | 0.25 | 0.25 | 0.25 | 0.25 | Baseline for comparison |

Showing how city rankings change under different weight assumptions is itself a strong analytical contribution. If Quebec ranks first under all three scenarios, the recommendation is robust. If rankings shift, the analysis reveals which trade-offs are at stake.

---

## Uncertainty Quantification: Monte Carlo Simulation

Point estimates without confidence intervals are insufficient for policy decisions. The SIS framework propagates uncertainty from each sub-model through the composite score using Monte Carlo simulation.

### Step 1: Characterize Sub-Model Uncertainty

Each sub-model produces not just a point estimate but a distribution of plausible values.

| Sub-Model | Uncertainty Source | Distribution Method |
|---|---|---|
| Grid Stress (XGBoost) | Model prediction variance | Quantile regression or bootstrap resampling |
| Carbon Intensity (Prophet) | Time-series forecast uncertainty + marginal multiplier range | Prophet native prediction intervals; for marginal estimates using multiplier fallback, sample from Uniform(2x, 5x) for mixed grids, Uniform(1x, 1.5x) for fossil-dominant grids (based on Dandres et al. 2016 range) |
| PUE (Random Forest) | Weather data variability | Propagate TMY data variance through model |
| Water Intensity (Lookup) | Cooling type range | Low/mid/high WUE scenarios from benchmarks |

### Step 2: Sample and Compute SIS for Each Draw

```python
def monte_carlo_sis(carbon_dist, water_dist, grid_dist, weights, n=1000):
    """
    Compute SIS distribution via Monte Carlo sampling.

    Parameters:
        carbon_dist: dict with 'mean' and 'std' for normalized carbon score
        water_dist: dict with 'mean' and 'std' for normalized water score
        grid_dist: dict with 'mean' and 'std' for normalized grid score
        weights: dict with 'carbon', 'water', 'grid', 'uncertainty' keys
        n: number of Monte Carlo samples

    Returns:
        dict with mean SIS and 90% confidence interval bounds
    """
    carbon_samples = np.random.normal(carbon_dist['mean'], carbon_dist['std'], n)
    water_samples = np.random.normal(water_dist['mean'], water_dist['std'], n)
    grid_samples = np.random.normal(grid_dist['mean'], grid_dist['std'], n)

    # Clip to [0, 1] after sampling (scores are bounded)
    carbon_samples = np.clip(carbon_samples, 0, 1)
    water_samples = np.clip(water_samples, 0, 1)
    grid_samples = np.clip(grid_samples, 0, 1)

    # Uncertainty component derived from variance of other components
    uncertainty_samples = np.sqrt(
        np.var(carbon_samples) + np.var(water_samples) + np.var(grid_samples)
    ) * np.ones(n)

    sis_samples = (
        weights['carbon'] * carbon_samples +
        weights['water'] * water_samples +
        weights['grid'] * grid_samples +
        weights['uncertainty'] * uncertainty_samples
    )

    return {
        'mean': float(np.mean(sis_samples)),
        'ci_low': float(np.percentile(sis_samples, 5)),
        'ci_high': float(np.percentile(sis_samples, 95)),
        'std': float(np.std(sis_samples))
    }
```

### Step 4: Report Results

For each candidate city, report:

- **Mean SIS** (point estimate for ranking)
- **90% confidence interval** (5th and 95th percentiles)
- **Probability of being best** (fraction of Monte Carlo draws where this city has the lowest SIS)

---

## Why Monte Carlo Uncertainty Matters

Most DC siting tools present point estimates with no uncertainty quantification. Without CIs, two cities scoring 0.42 and 0.45 appear different — but overlapping 90% CIs of [0.30, 0.55] and [0.38, 0.52] reveal no meaningful distinction. Monte Carlo provides:

- **Honest assessment:** "Quebec 0.12 [0.08, 0.18] vs Alberta 0.71 [0.62, 0.80] — robust difference" vs "Toronto 0.35 [0.22, 0.51] vs Montreal 0.28 [0.19, 0.40] — overlapping CIs"
- **Risk-aware recommendations:** Decision-makers can prefer tighter CI over lower mean
- **Academic differentiator:** Genuine UQ is rare in DC sustainability literature

---

## Visualization

### Choropleth Map

Folium-based map of Canada, color-coded by SIS score (green=low/responsible, red=high/risky). Each city marker shows a popup with mean SIS, 90% CI, and sub-score breakdown.

### Dashboard (Stretch Goal)

Streamlit dashboard with weight sliders (constrained to sum to 1.0), real-time score recalculation, side-by-side city comparison, CI visualization (error bars or violin plots), and scenario toggle.

### Presentation Figures

1. **Bar chart:** SIS scores for 8 cities with 90% CI error bars
2. **Tornado chart:** Sub-score contributions for a representative city
3. **Rank stability heatmap:** How rankings change across weight scenarios

---

## MCDA Methodological Grounding

The composite scoring approach is grounded in Multi-Criteria Decision Analysis (MCDA), a well-established field in operations research and sustainability assessment.

### Relevant MCDA Methods

| Method | Description | Applicability |
|---|---|---|
| Weighted Sum Model (WSM) | Linear aggregation with weights -- our primary approach | High: simple, transparent, widely understood |
| TOPSIS | Rank by distance to ideal and anti-ideal solutions | Medium: useful for sensitivity analysis |
| PROMETHEE | Outranking method based on pairwise preference | Low: adds complexity without clear benefit for our use case |
| AHP | Hierarchical pairwise comparison for weight derivation | Medium: applicable if expert weights are needed |

The Weighted Sum Model is the most commonly used MCDA method in environmental assessment and is appropriate for this project's scope.

---

## End-to-End Pipeline Summary

```
Input: City + facility size (MW) + cooling type
  → Sub-Model 1 (Grid Stress) → S_grid
  → Sub-Model 2 (Carbon) + Sub-Model 3 (PUE) → S_carbon = energy × PUE × gCO₂/kWh
  → Sub-Model 4 (Water) → S_water = WUE × energy × stress
  → Normalize all S to [0,1] → Weighted sum → Monte Carlo (N=1000)
Output: Ranked cities with SIS mean, 90% CI, sub-score breakdowns
```

---

## Key References

- **Dandres, T. et al. 2016,** "Consequences of Future Data Center Deployment in Canada on Electricity Generation and Environmental Impacts," *Journal of Industrial Ecology* 20(5), 1312-1322. -- Establishes marginal intensity range (0.85-1.01 kg CO2-eq/kWh) used for Monte Carlo uncertainty propagation and cross-border impact flagging.
- Pohekar, S.D. & Ramachandran, M. 2004, "Application of Multi-Criteria Decision Making to Sustainable Energy Planning -- A Review," *Renewable and Sustainable Energy Reviews* 8(4), 365-381. https://www.sciencedirect.com/science/article/pii/S1470160X14002647
- Wieckowski, J. et al. 2023, "Recent Advances in Multi-Criteria Decision Analysis: A Comprehensive Review of Applications and Trends," *International Journal of Knowledge Engineering and Soft Data Paradigms*. https://journals.sagepub.com/doi/10.3233/KES-230487
- Saaty, T.L. 1980, "The Analytic Hierarchy Process." McGraw-Hill.
- Hwang, C.L. & Yoon, K. 1981, "Multiple Attribute Decision Making: Methods and Applications." Springer-Verlag.
