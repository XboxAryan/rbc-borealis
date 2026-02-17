# Global AI Data Center Growth

---

## Overview

Data centers are the fastest-growing segment of global electricity demand. Driven primarily by AI training and inference workloads, the sector's power consumption is projected to more than double by 2030. This document summarizes the key figures, growth drivers, and environmental projections that frame the urgency of the siting problem.

---

## Current Electricity Consumption

### Global

| Metric | Value | Year | Source |
|---|---|---|---|
| Total DC electricity consumption | ~415 TWh | 2024 | IEA |
| Share of global electricity | ~1.5% | 2024 | IEA |
| Projected DC consumption | ~945 TWh | 2030 | IEA |
| Projected share of global electricity | ~3.4% | 2030 | IEA |

For context, 945 TWh exceeds the total electricity consumption of Japan (approximately 900 TWh/year).

### United States

| Metric | Value | Year | Source |
|---|---|---|---|
| Total DC electricity consumption | 176 TWh | 2023 | LBNL |
| Historical baseline | 58 TWh | 2014 | LBNL |
| Projected consumption (low) | 325 TWh | 2028 | LBNL |
| Projected consumption (high) | 580 TWh | 2028 | LBNL |
| Share of US electricity | ~4.4% | 2023 | LBNL |

US data center electricity consumption tripled from 2014 to 2023. The projected range for 2028 reflects uncertainty in AI workload scaling, with the high estimate implying a further tripling in just five years.

---

## Growth Rates

- **Data center sector:** ~15% annual electricity demand growth
- **All other sectors combined:** ~4% annual growth
- **AI-accelerated servers specifically:** ~30% annual growth rate in deployed compute capacity

The gap between data center growth and general electricity demand growth is widening. Traditional efficiency gains (server consolidation, improved PUE) that previously offset demand increases are being overwhelmed by the scale of AI workloads.

### Global Market Size

| Metric | Value | Source |
|---|---|---|
| Global DC market size (2024) | ~$250 billion | Various industry estimates |
| Projected market size (2030) | ~$550-620 billion | Mordor Intelligence, Statista |
| CAGR (2024-2030) | ~13-15% | Various |
| Hyperscale facilities worldwide | ~1,000+ | Synergy Research Group |

---

## AI as the Primary Growth Driver

AI workloads are qualitatively different from traditional data center loads:

- **Training runs** consume massive power for weeks or months continuously (e.g., training a frontier LLM can consume 50-100 GWh in a single run)
- **Inference at scale** requires sustained GPU/TPU utilization with high power density per rack (30-50+ kW/rack vs. 5-10 kW/rack for traditional workloads)
- **No natural plateau** -- each generation of foundation models demands 3-10x the compute of its predecessor
- **Geographic concentration** -- AI training clusters require low-latency interconnects, limiting distribution across multiple sites

The result is a class of demand that is simultaneously massive, continuous, geographically concentrated, and growing exponentially.

---

## Environmental Projections: Carbon

### Cornell / Nature Sustainability Study (Xiao & You, November 2025)

This is the most comprehensive peer-reviewed assessment of US AI data center environmental impact to date.

**Key findings:**

| Metric | Value (2030 Projection) |
|---|---|
| CO2 emissions from AI data centers | 24-44 MtCO2/year |
| Equivalent internal combustion vehicles | 14+ million |
| Share of US electricity-related emissions | ~2-4% |

**Mitigation potential** (the central finding):

| Strategy | CO2 Reduction | Water Reduction |
|---|---|---|
| Smart siting alone | -- | 52% |
| Grid decarbonization + operations | -- | 86% (total) |
| Energy/water-efficient technology | 7% additional | 29% |
| **All coordinated strategies combined** | **73%** | **86%** |

The study's critical insight is that **where** you build matters as much as **how** you build. Siting is the single most impactful lever for water consumption (52% reduction) and a major lever for carbon. This directly motivates our project's focus on a siting-oriented assessment tool.

**Optimal US locations identified:**

- Texas (wind + solar, low water stress in certain regions)
- Montana, Nebraska, South Dakota (wind corridor)
- New York (nuclear + hydro baseload)
- Pacific Northwest (hydro)

The study did not include Canada, which is precisely the gap this project fills.

### Water Projections

| Metric | Value (2030 Projection) | Source |
|---|---|---|
| AI DC water consumption (US) | Equivalent to household usage for 6-10 million Americans | Xiao & You, 2025 |
| Google global water consumption | 8.1 billion gallons | Google Sustainability Report 2024 |
| Microsoft global water consumption | 7.8 billion gallons | Microsoft Sustainability Report 2024 |

Water consumption is growing faster than energy consumption because evaporative cooling scales with heat rejection, and AI workloads produce significantly more heat per unit of compute.

---

## Historical and Projected Trajectory

```
Year    Global DC TWh    US DC TWh    Key Event
----    -------------    ---------    ---------
2014         --              58       LBNL baseline
2018        205              --       Pre-AI-boom baseline
2022        340              --       ChatGPT launch (Nov 2022)
2023        370             176       AI training boom begins
2024        415              --       IEA estimate
2025        --               --       Ontario Bill 40
2028        --           325-580      LBNL projection range
2030        945              --       IEA projection
```

The trajectory shows a clear inflection point around 2022-2023 when large language models and generative AI shifted data center planning from incremental growth to exponential buildout.

---

## Supply-Side Constraints

The scale of projected data center growth is creating unprecedented challenges on the supply side:

- **Grid interconnection queues:** Average wait time for new generation projects to connect to US grids exceeds 5 years. Data centers are competing with renewable energy projects for grid access.
- **Transformer shortages:** Lead times for large power transformers have extended to 2-4 years globally.
- **Skilled labor:** Electricians, power engineers, and data center technicians are in short supply across North America.
- **Water rights:** In water-stressed regions, new evaporative cooling permits face increasing opposition and regulatory scrutiny.
- **Land and permitting:** Hyperscale facilities require 50-200+ acres with specific power, fiber, and water access characteristics.

These constraints mean that siting decisions are not freely optimizable -- practical considerations narrow the feasible set, making it all the more important to evaluate the environmental impact of the sites that are actually available.

---

## Implications for This Project

1. **Scale demands systematic assessment.** The 9 GW Canadian pipeline cannot be evaluated facility-by-facility through ad hoc review. An automated scoring tool is needed.
2. **Siting is the highest-leverage intervention.** The Nature Sustainability study demonstrates 52-73% reduction potential from coordinated siting and grid decarbonization.
3. **AI workloads are qualitatively different.** Traditional data center efficiency benchmarks underestimate the environmental burden of AI-heavy facilities.
4. **Canada is unaddressed.** The most rigorous studies (LBNL, Xiao & You) focus exclusively on the US. Canada's unique grid structure and provincial carbon variation require a dedicated analysis.

---

## Key Sources

- IEA, "Energy and AI," January 2025
- LBNL, "United States Data Center Energy Usage Report," December 2024
- Xiao, D. & You, F., "Powering AI data centers sustainably," Nature Sustainability, November 2025
- Synergy Research Group, Hyperscale Data Center Tracker, 2024
- Google Environmental Report, 2024
- Microsoft Sustainability Report, 2024
