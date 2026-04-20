# Environmental and Societal Impact Dimensions

---

## Overview

Data center siting decisions carry consequences across multiple environmental and social dimensions simultaneously. This document outlines the four primary impact dimensions -- carbon emissions, water consumption, grid stress, and community/equity effects -- and explains why a multi-dimensional assessment framework is necessary.

---

## 1. Carbon Emissions

### The Fundamental Equation

```
CO2 (tonnes/year) = IT_energy (MWh) x PUE x grid_carbon_intensity (tCO2/MWh)
```

Three variables determine a data center's carbon footprint: how much IT power it draws, how efficiently it converts total power into useful IT work (PUE), and how carbon-intensive the electricity grid is at the point of consumption.

### Provincial Carbon Intensity Variation

| Province | Approx. Grid Intensity (gCO2/kWh) | Primary Generation |
|---|---|---|
| Quebec | ~1.7 | Hydroelectric (94-99%) |
| British Columbia | ~11 | Hydroelectric (87-93%) |
| Manitoba | ~3 | Hydroelectric (>95%) |
| Ontario | ~30-80 | Nuclear + hydro + gas peaking |
| New Brunswick | ~290 | Nuclear + fossil |
| Nova Scotia | ~540 | Coal + gas + wind |
| Alberta | ~490 | Gas + coal + growing wind/solar |
| Saskatchewan | ~670 | Coal + gas |

**The 200x variation between Quebec (~2 gCO2/kWh) and Saskatchewan (~670 gCO2/kWh) is the single most important variable in Canadian data center carbon accounting.**

### Worked Example: 100 MW Facility

Assume PUE of 1.3 (industry average for modern facilities) and 8,760 hours/year operation:

| Location | Grid Intensity | Annual CO2 |
|---|---|---|
| Alberta (~490 gCO2/kWh) | 490 | ~556,000 tonnes |
| Saskatchewan (~670 gCO2/kWh) | 670 | ~760,000 tonnes |
| Ontario (~50 gCO2/kWh average) | 50 | ~57,000 tonnes |
| Quebec (~1.7 gCO2/kWh) | 1.7 | ~1,930 tonnes |

Using the simpler approximation from the project overview (IT energy x PUE x intensity with slight rounding): a 100 MW facility in Alberta emits approximately **430,000 tonnes CO2/year**, while the same facility in Quebec emits approximately **1,500 tonnes** -- a **286x difference**.

### Lock-In Effect

Data center infrastructure has a 20-30 year operational lifespan. A siting decision made in 2026 locks in emissions through 2046-2056. Even if Alberta's grid decarbonizes significantly, a facility built today will have accumulated millions of tonnes of CO2 before the grid reaches near-zero intensity.

### Net-Zero 2050 Alignment

Canada's legally binding Net-Zero by 2050 target means that high-carbon data center siting decisions are not merely environmentally suboptimal -- they are directly counterproductive to national climate commitments. Each high-carbon facility makes the remaining decarbonization pathway steeper for all other sectors.

---

## 2. Water Consumption

### Cooling and Water Use

Evaporative cooling is the dominant cooling method for large-scale data centers. It works by evaporating water to reject heat, consuming large volumes in the process. This accounts for the majority of data center water use.

**Industry benchmark:** Average Water Usage Effectiveness (WUE) is approximately **1.8 L/kWh** (Equinix reported figure).

### Canadian Examples

| Facility / Operator | Location | Water Figure | Source |
|---|---|---|---|
| Microsoft (planned complex) | Vaughan, ON | 730 million L/year expected | Municipal filings |
| Data center (approved) | Etobicoke, ON | 39.75 L/s for cooling | Municipal approval |
| QScale Q01 | Levis, QC | ~100 MW waste heat redirected to household heating | QScale |

The QScale example is notable as a positive case: rather than simply consuming water and rejecting heat, the facility captures waste heat and distributes it to nearby homes, partially offsetting the environmental cost.

### Global Context

| Operator | Annual Water Consumption | Year | Source |
|---|---|---|---|
| Google | 8.1 billion gallons (~30.7 billion litres) | 2024 | Google Environmental Report |
| Microsoft | 7.8 billion gallons (~29.5 billion litres) | 2024 | Microsoft Sustainability Report |

These figures have been increasing year-over-year as AI workloads grow.

### Canadian Water Discourse

A CBC investigation in 2024 noted: *"Canada is poised to join the data centre boom, but there is little debate here about what this will mean for the country's water."* The investigation highlighted that:

- Canadian municipalities have limited experience evaluating data center water permit applications
- Water consumption data for Canadian data centers is not systematically collected or published
- Public awareness of data center water use is minimal compared to energy use
- Municipal water infrastructure was not designed for single consumers drawing tens of millions of litres per year

### Water Stress Is Regional

Canada is often perceived as water-abundant, but water stress is highly localized:

- Southern Ontario watersheds face seasonal stress, particularly during summer peak cooling demand
- Prairie provinces experience periodic drought conditions
- Aquifer recharge rates vary significantly by sub-region
- Municipal water systems in growing suburbs (where hyperscale facilities are being sited) may already be near capacity

A data center in Quebec may have minimal carbon impact but could face water stress in specific sub-regions. Water assessment must be site-specific, not province-level.

---

## 3. Grid Stress

### Baseload Demand Characteristics

Data centers represent **continuous, non-interruptible baseload demand**. Unlike residential or commercial loads that fluctuate with time of day and season, data center power draw is essentially flat 24/7/365. This has specific grid implications:

- **Peak demand contribution:** Data centers add to peak demand without offering the natural load-shedding that occurs when residential and commercial consumers reduce usage
- **Reserve margin erosion:** Continuous high load reduces the buffer between available generation and peak demand, increasing the risk of supply shortfalls
- **Price volatility:** In deregulated markets (Alberta), large baseload additions can trigger price spikes during periods of constrained supply
- **Transmission loading:** Data centers concentrate demand at specific grid nodes, potentially overloading local transmission infrastructure

### Provincial Grid Concerns

**Ontario:**
- Grid is already facing a tightening supply-demand balance as the Pickering Nuclear Generating Station approaches end of life
- IESO (Independent Electricity System Operator) has flagged emerging capacity adequacy risks
- Bill 40 was motivated in part by concern that uncontrolled data center connections could exacerbate grid stress
- Natural gas peaking plants may need to run more frequently, increasing carbon intensity during peak hours

**Alberta:**
- Fossil-heavy grid means additional data center load may extend the economic viability of fossil generation plants that would otherwise be retired
- Deregulated market means price signals, rather than central planning, determine generation dispatch
- Renewable energy growth (wind + solar) is strong but intermittent, creating a mismatch with data center baseload requirements

**Quebec:**
- Hydro-Quebec has historically had surplus capacity, but new large industrial loads (including data centers and cryptocurrency mining) are consuming that surplus
- Export contracts to New England and New York compete with domestic data center demand
- Reservoir levels and seasonal hydrology introduce supply variability that continuous data center demand does not accommodate

---

## 4. Community and Equity Impacts

### Rural Grid Reliability

New data center load sited near capacity-constrained transmission infrastructure can jeopardize electricity service reliability for existing communities. Rural areas with limited grid redundancy are particularly vulnerable -- a large data center can consume a significant fraction of local substation capacity, leaving less headroom for residential and agricultural consumers during peak demand events.

### Indigenous Consultation

Many proposed data center sites are located near or on traditional territories of Indigenous communities. Responsible siting requires:

- Meaningful consultation under the duty to consult framework
- Assessment of impacts on water sources, land use, and cultural sites
- Consideration of benefit-sharing arrangements (employment, revenue sharing, infrastructure)
- Alignment with Indigenous data sovereignty principles where applicable

### Urban Impacts

- **Heat island effects:** Large facilities reject significant waste heat, contributing to urban heat island effects in already-warm metropolitan areas
- **Noise:** Cooling systems (fans, chillers) generate continuous noise that can affect nearby residential areas
- **Traffic:** Construction and ongoing operations generate truck and vehicle traffic
- **Visual impact:** Hyperscale facilities are large, utilitarian structures that can alter neighbourhood character

### Economic Tradeoffs

Data centers bring economic benefits -- construction jobs, permanent operations employment, property tax revenue, and attraction of technology sector investment. However:

- Permanent employment per MW is low relative to other industrial facilities (a 100 MW data center may employ only 50-100 people)
- Tax incentive packages sometimes reduce the net fiscal benefit to the host municipality
- Environmental costs (water consumption, carbon emissions, grid stress) are externalities borne by the broader community
- **Transparent tradeoff analysis is needed** to determine whether the economic benefits justify the environmental and social costs in a given location

---

## 5. Why Multi-Dimensional Assessment Matters

### Limitations of Single-Dimension Tools

Existing assessment tools and frameworks typically address **one dimension at a time**:

- Carbon calculators estimate emissions but ignore water and grid impacts
- PUE benchmarks measure efficiency but do not account for the carbon intensity of the energy being used (a PUE of 1.1 in Alberta still produces far more carbon than a PUE of 1.4 in Quebec)
- Water assessments rarely incorporate grid carbon or community equity dimensions
- Economic impact analyses typically omit environmental externalities

### Interaction Effects

The dimensions interact in ways that single-dimension tools cannot capture:

| Scenario | Carbon | Water | Grid | Equity | Single-Dimension Assessment | Multi-Dimensional Assessment |
|---|---|---|---|---|---|---|
| 100 MW in Quebec | Minimal | Possible sub-regional stress | Surplus eroding | Indigenous consultation needed | "Green" (carbon-only) | Moderate concern (water + equity) |
| 100 MW in Alberta with solar PPA | Reduced but not zero | Low (dry cooling feasible) | May extend fossil backup | Jobs in transition economy | "High carbon" (grid-average) | Mixed -- benefits and costs |
| 100 MW in rural Ontario | Moderate | Watershed-dependent | High stress risk | Rural reliability threatened | Varies by dimension | High concern (grid + equity) |

No single metric can capture these tradeoffs. A composite score with transparent sub-component weights allows policymakers to see the full picture and adjust priorities based on regional context.

### The Gap This Project Fills

There is currently **no publicly available tool** that:

1. Combines carbon, water, grid stress, and equity dimensions into a single assessment
2. Provides uncertainty quantification (confidence intervals rather than point estimates)
3. Is calibrated to Canadian provincial grid data
4. Accounts for marginal (not average) carbon intensity
5. Incorporates site-specific watershed and community data

This project aims to build that tool.

---

## Key Sources

- CER, Provincial and Territorial Energy Profiles, 2024
- CBC, "Canada is poised to join the data centre boom," 2024
- Google Environmental Report, 2024
- Microsoft Sustainability Report, 2024
- Equinix Sustainability Report (WUE benchmarks), 2024
- IESO, Annual Planning Outlook, 2024
- Alberta Electric System Operator (AESO), Long-term Outlook, 2024
- Hydro-Quebec Annual Report, 2024
- Xiao, D. & You, F., "Powering AI data centers sustainably," Nature Sustainability, November 2025
- AWS Sustainability Report, 2024
