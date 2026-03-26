# Sub-Model 3: PUE / Cooling Overhead Regression

---

## Problem Definition

The PUE model predicts **Power Usage Effectiveness** for a data center at a given location based on local climate conditions and facility design parameters.

### PUE Definition

```
PUE = Total Facility Energy / IT Equipment Energy
```

- A PUE of **1.0** is the theoretical minimum: all energy goes to computing, with zero overhead.
- Higher values indicate more energy lost to cooling, lighting, power distribution, and other non-IT loads.
- Cooling is the dominant overhead component, typically accounting for 30-50% of non-IT energy in traditional facilities.

### Typical PUE Ranges

| Configuration | Typical PUE Range |
|---|---|
| State-of-the-art hyperscale (cold climate) | 1.05 - 1.15 |
| Modern hyperscale (moderate climate) | 1.10 - 1.25 |
| Enterprise (cold climate, economizer) | 1.20 - 1.40 |
| Enterprise (hot climate, chiller) | 1.40 - 1.80 |
| Legacy facility (no economizer) | 1.80 - 2.50 |
| Global industry average (2024, Uptime Institute) | ~1.55 - 1.60 |

For a 100 MW IT load, the difference between PUE 1.10 and PUE 1.60 represents 50 MW of additional power consumption -- enough to power approximately 40,000 Canadian homes.

---

## Physics Basis

The relationship between PUE and climate is grounded in thermodynamics, not learned from data alone.

### Core Equation

```
PUE = 1.0 + (cooling_overhead + other_overhead) / IT_load
```

Where:

- `cooling_overhead` = energy consumed by cooling systems (chillers, fans, pumps, cooling towers)
- `other_overhead` = power distribution losses, lighting, security, UPS inefficiency (~0.05-0.10 PUE)
- `IT_load` = total power delivered to servers, storage, and networking equipment

### Free Cooling Threshold

The critical variable is whether the outdoor air temperature is below the **economizer switchover point** (typically 18-22 degrees C, depending on facility design and humidity tolerance).

- **Below threshold (free cooling):** Outside air (or a heat exchanger using outside air) directly cools the data hall. Energy cost is limited to fan power. Cooling overhead is minimal.
- **Above threshold (mechanical cooling):** Compressor-based chillers must actively remove heat. Energy cost increases sharply -- typically 0.3-0.5 kW of cooling energy per kW of IT load.

This creates a **piecewise-linear** relationship between temperature and PUE: approximately flat below the economizer threshold, then linearly increasing above it.

### Canadian Climate Advantage

Canada's cold climate provides a structural advantage for data center cooling efficiency.

- **5,500+ free-cooling hours per year** across most of Canada (approximately 60% of annual hours)
- Cities like Montreal, Toronto, and Calgary all benefit from extended winter economizer operation
- Even summer peaks in most Canadian cities are milder than US data center hubs (e.g., Dallas, Phoenix)
- Average cooling energy savings of approximately 80% where economizers are feasible compared to mechanical-only cooling

---

## Key Features

Features are ranked by their influence on PUE, based on Sobol sensitivity analysis from the literature.

| Rank | Feature | Description | Influence |
|---|---|---|---|
| 1 | Outdoor dry-bulb temperature | Primary driver of cooling load | Highest |
| 2 | Outdoor wet-bulb temperature | Determines evaporative cooling potential | High |
| 3 | Relative humidity | Affects cooling tower performance and air-side economizer limits | High |
| 4 | Cooling system type | Air-cooled, evaporative, hybrid, or liquid | High |
| 5 | IT load factor | Partial load operation increases PUE (fixed overhead / variable IT) | Medium |
| 6 | Design PUE baseline | Varies by facility age, design generation, and engineering quality | Medium |

The dominance of temperature-related features means that climate data is the single most important input. Facility design parameters modulate the baseline but do not change the fundamental climate-driven relationship.

---

## Model Selection

### Primary: Random Forest Regression

- **Rationale:** PUE is driven by a small number of well-understood physical variables. The relationship between temperature and cooling energy is approximately linear in the free-cooling regime and piecewise-linear at the economizer switchover point. A Random Forest with 5-8 features captures this structure with high accuracy and full interpretability.
- **Alternative:** Linear regression with explicit breakpoints at the economizer threshold. Simpler, equally valid, and more transparent.
- **Not recommended:** Deep learning. The Google DeepMind approach (see below) used thousands of sensor features from proprietary telemetry. For our project, which uses publicly available climate data and published PUE benchmarks, a simple model is both more appropriate and more defensible.

### Feature Importance Validation

```python
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# After training
rf = RandomForestRegressor(n_estimators=200, max_depth=8, random_state=42)
rf.fit(X_train, y_train)

# Feature importance
importances = rf.feature_importances_
for name, imp in sorted(zip(feature_names, importances), key=lambda x: -x[1]):
    print(f"{name}: {imp:.3f}")
```

Expected output should confirm that temperature-related features dominate, consistent with the physics.

---

## Google DeepMind Reference

Google DeepMind's data center cooling optimization is the most prominent ML application in this domain.

### Approach

- Neural network ensemble trained on 2 years of monitoring data from Google data centers
- 5 hidden layers, 50 nodes each
- Input: thousands of sensor readings (temperatures, power, pump speeds, setpoints, valve positions)
- Output: recommended cooling setpoints

### Results

- **40% reduction in cooling energy consumption**
- **15% reduction in overall PUE**
- Deployed in production across multiple Google facilities

### Why This Is Not Reproducible for Our Project

- Requires proprietary real-time telemetry from thousands of sensors per facility
- Training data is not publicly available
- The model optimizes **operational control** (adjusting setpoints in real time), not **siting prediction** (estimating PUE for a proposed location)
- Our task is fundamentally different: predict PUE from climate data, not optimize PUE from sensor data

The DeepMind work demonstrates that ML can reduce PUE, but the approach is orthogonal to our siting-oriented model.

---

## Semi-Synthetic Approach for MVP

Since no public dataset of measured PUE values across Canadian cities exists, we use a physics-informed semi-synthetic approach.

### Step 1: Obtain Climate Data

Download TMY (Typical Meteorological Year) or CWEC (Canadian Weather for Energy Calculations) data for target cities. These datasets provide hourly temperature, humidity, and solar radiation values for a statistically representative year.

**Target cities:** Toronto, Montreal, Calgary, Vancouver, Winnipeg, Halifax, Edmonton, Ottawa, Quebec City, Saskatoon.

### Step 2: Compute Free-Cooling Hours

Using ASHRAE psychrometric bin analysis:

```python
def free_cooling_hours(tmy_data, threshold_temp=20.0):
    """Count hours where outdoor temperature allows economizer operation."""
    below_threshold = tmy_data['dry_bulb_temp'] <= threshold_temp
    return below_threshold.sum()

def pue_estimate(dry_bulb_temp, supply_temp_setpoint=22.0, design_pue_base=1.10):
    """Estimate hourly PUE from outdoor temperature."""
    if dry_bulb_temp <= supply_temp_setpoint:
        # Free cooling regime: minimal overhead (fans only)
        cooling_overhead = 0.02 + 0.001 * max(0, dry_bulb_temp)
    else:
        # Mechanical cooling regime: overhead scales with temperature delta
        delta_t = dry_bulb_temp - supply_temp_setpoint
        cooling_overhead = 0.02 + 0.015 * delta_t
    return design_pue_base + cooling_overhead
```

### Step 3: Validate Against Published Benchmarks

Compare estimated annual PUE values against published ranges from Uptime Institute and LBNL. Adjust the model coefficients if estimates fall outside expected ranges for a given climate zone and facility class.

### Step 4: Generate Output

For each city and each month:

- Predicted mean PUE
- 90% confidence interval (propagated from weather data variability)
- Free-cooling hours count
- Estimated annual cooling energy (kWh per MW of IT load)

---

## ASHRAE Free Cooling Analysis

The ASHRAE psychrometric bin analysis is the industry-standard method for estimating economizer performance.

### Methodology

1. Bin hourly weather data by dry-bulb temperature and humidity ratio.
2. For each bin, determine whether free cooling, partial free cooling, or mechanical cooling is required.
3. Sum hours and energy consumption across all bins for the year.

### Canadian Results (Selected Cities)

| City | Free-Cooling Hours/Year | % of Year | Estimated Annual PUE |
|---|---|---|---|
| Winnipeg | ~6,200 | 71% | 1.12 - 1.18 |
| Montreal | ~5,800 | 66% | 1.14 - 1.22 |
| Calgary | ~6,000 | 68% | 1.12 - 1.20 |
| Toronto | ~5,400 | 62% | 1.16 - 1.25 |
| Vancouver | ~6,500 | 74% | 1.10 - 1.18 |
| Halifax | ~5,600 | 64% | 1.14 - 1.22 |

These estimates assume a modern facility with air-side economizer. Legacy facilities without economizer capability would see PUE values 0.3-0.5 higher.

### Reference

- NREL/DOE, "Psychrometric Bin Analysis and Alternative Cooling Strategies for Data Centers." https://www1.eere.energy.gov/buildings/publications/pdfs/rsf/psychrometric_bin_analysis_alternative_cooling_strategies_data_centers.pdf

---

## Key References

- Google DeepMind, "DeepMind AI Reduces Google Data Centre Cooling Bill by 40%." https://deepmind.google/discover/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-by-40/
- Lei, N. et al. 2024, "Impact of Economizer Types on PUE Across Climate Zones," *MDPI Buildings* 14(1), 299. https://www.mdpi.com/2075-5309/14/1/299
- Tao, Z. et al. 2022, "Prediction of Overall Energy Consumption of Data Centers," *MDPI Sensors* 22(10), 3704. https://www.mdpi.com/1424-8220/22/10/3704
- Uptime Institute, "Global Data Center Survey," 2024.
- ASHRAE TC 9.9, "Data Center Networking Equipment -- Issues and Best Practices."
