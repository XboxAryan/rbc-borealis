# Sub-Model 4: Water Intensity Estimation

---

## Problem Definition

The water intensity model estimates **liters of water consumed per kWh of IT energy** for a data center at a given location, based on the cooling system type and local climate conditions. Unlike the other sub-models, this component does **not** require machine learning. A physics-based estimation grounded in published benchmarks and geospatial water stress data is more defensible and more transparent than a trained model.

### Why Water Matters

Evaporative cooling -- the most common data center cooling method -- consumes large volumes of water. A single 100 MW hyperscale data center with typical evaporative cooling can consume 1-3 million liters of water per day, comparable to the daily water use of a small city. In water-stressed regions, this consumption competes directly with agricultural, industrial, and residential demand.

---

## Water Usage Effectiveness (WUE) Benchmarks

WUE is the standard industry metric for data center water consumption, defined as liters of water consumed per kWh of IT energy.

| Cooling Type | WUE (L/kWh) | Notes |
|---|---|---|
| Air-cooled only (no water) | ~0 | No water use, but higher energy consumption and PUE |
| Best-in-class evaporative (e.g., AWS) | 0.19 | AWS global average, 2024 sustainability report |
| Typical evaporative | 1.8 | Industry average, Equinix reporting |
| Inefficient evaporative (hot/humid climate) | 2.5 - 9.0 | Upper bound is climate-dependent |
| Hybrid (air + evaporative) | 0.5 - 1.5 | Partial water use, switchover based on temperature |
| Microsoft zero-water design (2024+) | ~0 | Chip-level liquid cooling loop, no evaporative tower |

The range spans two orders of magnitude, making cooling type selection a first-order decision for water impact.

---

## Estimation Formula

The water intensity for a given location and cooling configuration is computed as follows:

```
WUE_estimated = base_WUE(cooling_type) * climate_adjustment(wet_bulb_temp)
Water_consumption = WUE_estimated * Total_energy
Water_harm = Water_consumption * water_stress_multiplier(region)
```

### Component Definitions

**Base WUE** is a lookup from the benchmarks table above, selected by cooling system type.

**Climate adjustment** accounts for the fact that evaporative cooling water consumption scales with:

- Enthalpy difference between outdoor air and supply air setpoint
- Number of hours per year requiring evaporative cooling (vs. free cooling, where no water is consumed)
- Cooling tower efficiency, characterized by cycles of concentration (ratio of dissolved solids in blowdown water to makeup water)

```python
def climate_adjusted_wue(base_wue, wet_bulb_temps, threshold=15.0):
    """Adjust base WUE for local climate using wet-bulb temperature profile."""
    evap_hours = sum(1 for t in wet_bulb_temps if t > threshold)
    total_hours = len(wet_bulb_temps)
    evap_fraction = evap_hours / total_hours

    # Water is only consumed during evaporative cooling hours
    adjusted_wue = base_wue * evap_fraction
    return adjusted_wue
```

**Water stress multiplier** transforms raw water consumption into a harm metric by weighting against local water availability. A liter consumed in a water-abundant region (e.g., Great Lakes) has less societal impact than a liter consumed in a water-stressed region (e.g., southern Alberta during drought).

---

## Water Stress Data: WRI Aqueduct 4.0

The World Resources Institute Aqueduct Water Risk Atlas (version 4.0) provides the geospatial water stress layer.

### Available Indicators

| Indicator | Description |
|---|---|
| Baseline water stress | Ratio of total water withdrawals to available renewable surface and groundwater |
| Baseline water depletion | Ratio of total water consumption to available renewable water |
| Interannual variability | Year-to-year variation in available water supply |
| Seasonal variability | Within-year variation in water supply |
| Groundwater table decline | Rate of groundwater level decline |
| Drought risk | Probability-weighted drought severity |

Aqueduct 4.0 provides 13 indicators total, with monthly snapshots available for temporal analysis.

### Access

- Direct download: https://www.wri.org/data/aqueduct-water-risk-atlas
- Google Earth Engine integration for programmatic access
- Spatial resolution: HydroBASINS level 6 (sub-basin scale)

---

## Regional Water Stress Context for Canada

Water stress is not uniform across Canada. The following regional patterns are relevant to data center siting.

| Region | Water Stress Level | Key Factors |
|---|---|---|
| Prairie provinces (Alberta, Saskatchewan) | Moderate to High | Seasonal variability, agricultural demand, drought risk |
| BC interior | Moderate (seasonal) | Summer drought conditions, competing agricultural use |
| Ontario Great Lakes region | Low | Abundant supply from Great Lakes basin |
| Quebec | Very Low | Extensive freshwater resources, low competing demand |
| Atlantic provinces | Low to Moderate | Generally adequate, some seasonal constraints |
| Northern territories | Low (supply) / High (infrastructure) | Water available but treatment and distribution infrastructure is limited |

This regional variation creates a meaningful differentiator when combined with carbon intensity. For example:

- **Alberta** has both high carbon intensity (~490 gCO2/kWh) and moderate-to-high water stress -- double penalty for data center siting.
- **Quebec** has near-zero carbon intensity (~1.7 gCO2/kWh) and very low water stress -- both dimensions favor siting.
- **British Columbia** has low carbon intensity (~15 gCO2/kWh) but seasonal water stress in interior regions -- a mixed signal that the composite score can capture.

---

## MVP Implementation

The water intensity sub-model does not require model training. It is implemented as a deterministic lookup and calculation pipeline.

### Step 1: Build Lookup Table

Construct a lookup table mapping cooling system type and climate zone to WUE estimate:

```python
WUE_TABLE = {
    ('air_cooled', 'any'):          0.0,
    ('evaporative', 'cold'):        0.8,
    ('evaporative', 'moderate'):    1.8,
    ('evaporative', 'hot_humid'):   4.5,
    ('hybrid', 'cold'):             0.3,
    ('hybrid', 'moderate'):         0.8,
    ('hybrid', 'hot_humid'):        1.5,
    ('liquid_cooled', 'any'):       0.0,
}
```

### Step 2: Apply Water Stress Multiplier

Download WRI Aqueduct 4.0 baseline water stress raster for Canada. For each candidate city, extract the local water stress index (0-5 scale) and multiply:

```python
def water_harm_score(wue, total_energy_kwh, water_stress_index):
    """Compute water harm score for a candidate location."""
    water_consumption = wue * total_energy_kwh  # liters
    harm = water_consumption * (water_stress_index / 5.0)  # normalized
    return harm
```

### Step 3: Output

For each candidate city:

- Estimated WUE (L/kWh) for each cooling type scenario
- Estimated annual water consumption (liters)
- Local water stress index (from Aqueduct 4.0)
- **Water harm score** = WUE * projected annual energy * local stress index

### Uncertainty

Water intensity uncertainty is dominated by cooling system type selection (which is a design choice, not a prediction). For the composite score, we propagate uncertainty by considering a range of WUE values for each cooling type (low, mid, high from the benchmarks table).

---

## Key Sources

- EESI, "Data Centers and Water Consumption." https://www.eesi.org/articles/view/data-centers-and-water-consumption
- Equinix, "What is Water Usage Effectiveness (WUE) in Data Centers?" https://blog.equinix.com/blog/2024/11/13/what-is-water-usage-effectiveness-wue-in-data-centers/
- Dgtl Infra, "Data Center Water Usage." https://dgtlinfra.com/data-center-water-usage/
- DOE, "Cooling Water Efficiency Opportunities for Federal Data Centers." https://www.energy.gov/femp/cooling-water-efficiency-opportunities-federal-data-centers
- Microsoft, "Sustainable by Design: Next-Generation Datacenters Consume Zero Water for Cooling." https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/
- WRI Aqueduct 4.0, "Aqueduct Water Risk Atlas." https://www.wri.org/data/aqueduct-water-risk-atlas
