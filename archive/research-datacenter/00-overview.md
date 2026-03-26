# Societal Impact Modeling for AI Data Center Siting in Canada -- Research Overview

---

## Core Policy Question

> Given a proposed data center in Region R, is it environmentally and socially responsible to build there?

This project builds a composite **Societal Impact Score (SIS)** that quantifies the environmental and social cost of siting an AI data center in any Canadian region. The score integrates four sub-models -- grid stress, carbon intensity, cooling efficiency, and water intensity -- with Monte Carlo uncertainty quantification to produce a defensible, policy-ready assessment.

---

## Project Summary

Four sub-models feed into a single composite score:

| Sub-Model | What It Measures | Key Output |
|---|---|---|
| **Grid Stress** | Marginal load impact on provincial reserve margins, peak demand, and price volatility | Grid Stress Index (0-1) |
| **Carbon Intensity** | Lifecycle CO2 emissions per kWh of electricity consumed at the proposed site | gCO2/kWh (marginal) |
| **PUE / Cooling Efficiency** | Power Usage Effectiveness driven by local climate, humidity, and cooling technology | Annualized PUE estimate |
| **Water Intensity** | Evaporative cooling water consumption and local watershed stress | L/kWh + watershed risk score |

The four sub-model outputs are combined into a weighted **Societal Impact Score** using configurable policy weights. Monte Carlo simulation propagates uncertainty from each sub-model through the composite, yielding confidence intervals rather than point estimates.

---

## Why Canada

Canada's federated electricity system creates a natural experiment that no other country offers with comparable data quality.

- **200x variation in provincial carbon intensity:** Quebec emits approximately 2 gCO2/kWh (almost entirely hydroelectric), while Saskatchewan emits approximately 670 gCO2/kWh (dominated by fossil generation). This range is wider than the variation across most entire continents.
- **Provincial control over generation mix:** Each province independently manages its electricity grid, creating distinct regulatory and emissions profiles within a single national data ecosystem.
- **High-quality open data:** Statistics Canada, the Canada Energy Regulator (CER), Environment and Climate Change Canada (ECCC), and provincial utilities all publish granular, machine-readable data under open licenses.
- **Active policy window:** Ontario's Bill 40 (December 2025) introduced the first Canadian legislation explicitly requiring ministerial approval for data center grid connections, signaling that governments are seeking analytical tools to evaluate proposals.
- **Concentrated geography:** 93% of Canadian data center IT load sits in three metropolitan hubs (Toronto, Montreal, Calgary), making the siting problem tractable -- a small number of regions cover the vast majority of decisions.

### Comparison to Other Jurisdictions

No other country offers the same combination of features for this research:

- **United States:** Individual states vary in carbon intensity, but lack Canada's extreme range (200x). Grid data is fragmented across ISOs/RTOs with inconsistent formats.
- **European Union:** EU-wide carbon targets exist, but electricity markets are interconnected across borders, making attribution of marginal generation to a specific site harder to model.
- **Nordics:** Low-carbon grids (hydro/nuclear) but limited variation across regions -- less interesting as a natural experiment.

Canada uniquely combines extreme variation, high data quality, and an active regulatory moment.

### Canada's Data Center Footprint

| Metric | Value | Source |
|---|---|---|
| Total IT capacity | 10.3 GW (Q2 2025) | DC Byte |
| Development pipeline | ~9-10 GW | DC Byte |
| Total tracked facilities | ~337 | DataCenters.com (Oct 2025) |
| Market value (projected 2029) | $9.04 billion | ENCOR Advisors |
| CAGR (2023-2029) | 10.26% | Mordor Intelligence |

Three hubs account for **93% of total IT load:**

1. **Toronto** -- 72 facilities / 42 operators, >370 MW existing capacity (~40% of national)
2. **Montreal** -- 54 facilities / 18 operators, near-zero carbon grid from hydropower
3. **Calgary/Alberta** -- Fastest-growing market, >25% of upcoming capacity (~2 GW pipeline)

---

## Why Now

- **Explosive growth:** 9 GW of pipeline capacity represents near-doubling of Canada's installed base, concentrated in a 3-5 year window.
- **Regulatory inflection:** Ontario Bill 40 (Royal Assent December 11, 2025) requires Minister of Energy and Mines approval for data center grid connections -- the first such law in Canada. Other provinces are watching.
- **Net-Zero 2050 target:** Siting decisions made today lock in 20-30 years of emissions. A 100 MW facility in Alberta vs. Quebec represents a ~430,000 tonne/year difference in CO2 output.
- **Water stress visibility:** CBC investigations (2024) and municipal water permit filings have brought data center water consumption into public discourse for the first time in Canada.
- **No existing multi-dimensional tool:** Current assessments address single dimensions (carbon OR water OR efficiency). No publicly available tool combines all dimensions into a single uncertainty-aware score.

---

## Sub-Model Descriptions

### 1. Grid Stress Model

Estimates the marginal impact of adding a data center's baseload demand to a provincial grid. Inputs include current reserve margins, hourly load profiles, planned generation additions, and transmission constraints. Outputs a Grid Stress Index (0-1 scale) reflecting how close the grid is to capacity limits after the proposed facility is added.

**Key inputs:** IESO/AESO/Hydro-Quebec hourly demand data, installed and planned generation capacity by fuel type, transmission topology constraints, historical outage rates.

**Why marginal, not average:** A data center added to a grid with 20% reserve margin has a different impact than one added to a grid at 5% reserve. The model captures this by evaluating the marginal change in reserve adequacy.

### 2. Carbon Intensity Model

Calculates marginal (not average) carbon intensity at the proposed site, accounting for the generation mix that would actually serve the incremental load. Incorporates time-of-day variation and seasonal shifts in renewable availability.

**Key inputs:** Provincial generation mix (hourly where available), fuel-specific emission factors, import/export flows between provinces, planned generation retirements and additions.

**Why marginal, not average:** When a data center is added to Ontario's grid, the incremental generation is likely natural gas peaking -- not the nuclear/hydro baseload that drives the low average intensity. Marginal intensity is typically 2-5x higher than average in mixed grids.

### 3. PUE / Cooling Efficiency Model

Predicts annualized Power Usage Effectiveness based on local climate data (dry-bulb temperature, wet-bulb temperature, humidity), facility design parameters, and cooling technology choice (air-side economization, evaporative, liquid cooling).

**Key inputs:** ECCC historical weather station data (hourly temperature, humidity, precipitation), facility design specifications (IT load, cooling technology, redundancy level), industry PUE benchmarks by climate zone.

**Output range:** Modern hyperscale facilities achieve PUE 1.1-1.2 in cold climates with free-air cooling. Older or less efficient facilities in warm climates may see PUE 1.4-1.8. The model estimates where a proposed facility would fall given its location and design.

### 4. Water Intensity Model

Estimates water consumption from evaporative cooling systems and cross-references against local watershed health indicators. Accounts for municipal water supply constraints and competing demands.

**Key inputs:** Cooling technology type and capacity, local water availability (watershed health indices, municipal supply data), historical drought frequency, competing demands from agriculture, residential, and industrial users.

**Output:** Litres per kWh of IT energy consumed, plus a watershed risk score indicating whether the local water supply can sustain the additional draw without adverse effects on other users.

### Composite Societal Impact Score

The SIS aggregates all four sub-models using configurable policy weights. Default weights reflect equal concern for all dimensions, but policymakers can adjust to prioritize carbon, water, or grid stability depending on regional context.

**Monte Carlo uncertainty quantification:** Each sub-model produces not a single point estimate but a distribution reflecting input data uncertainty, model parameter uncertainty, and scenario variability. The composite SIS is computed across 10,000+ Monte Carlo draws, yielding a distribution with confidence intervals (e.g., 5th/50th/95th percentile scores). This allows decision-makers to understand not just the expected impact but the range of plausible outcomes.

---

## Intended Audience and Use Cases

The Societal Impact Score is designed to serve multiple stakeholders:

- **Provincial energy regulators** (e.g., Ontario Ministry of Energy and Mines under Bill 40): Evaluate whether a proposed data center meets environmental and social thresholds for grid connection approval.
- **Municipal planners:** Assess water, noise, and community impacts of proposed facilities during zoning and permitting.
- **Data center operators:** Identify sites that minimize environmental footprint and regulatory risk, supporting ESG commitments.
- **Federal policymakers:** Inform national strategy on data center development within Net-Zero 2050 framework.
- **Researchers and advocacy organizations:** Provide transparent, reproducible methodology for environmental impact assessment.

---

## Repository Structure

| Path | Contents |
|---|---|
| `01-problem/` | Background on data center growth (global and Canadian), environmental impact dimensions |
| `02-datasets/` | Data sources for each sub-model, access methods, and quality assessment |
| `03-methodology/` | ML approaches, model architectures, Monte Carlo framework |
| `04-feasibility/` | Timeline, scope, team requirements, risk assessment |
| `05-literature/` | Annotated bibliography of key papers and reports |
| `06-proposal-alignment.md` | Mapping to RBC Borealis Let's SOLVE It evaluation criteria |

---

## Key Sources

- IEA, "Energy and AI," January 2025
- LBNL, "United States Data Center Energy Usage Report," December 2024
- Xiao & You, "Powering AI data centers sustainably," Nature Sustainability, November 2025
- DC Byte, Canada Data Center Market, Q2 2025
- CER, "Market Snapshot: Data Centres in Canada," October 2024
- Ontario Bill 40, Protect Ontario by Securing Affordable Energy for Generations Act, 2025
