# Industry Benchmarks and Reference Data

This document catalogs the major benchmark reports, sustainability disclosures, and standards frameworks that provide reference values for data center energy efficiency, water usage, and carbon emissions. These benchmarks are essential for calibrating model assumptions and contextualizing Canadian data center performance.

---

## 1. LBNL 2024 US Data Center Energy Usage Report

- **Organization:** Lawrence Berkeley National Laboratory (DOE-funded)
- **URL:** https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf
- **Publication Date:** December 2024

### Key Findings

| Metric | Value |
|---|---|
| US DC energy consumption (2014) | 58 TWh |
| US DC energy consumption (2023) | 176 TWh |
| Projected US DC energy (2028, low) | 325 TWh |
| Projected US DC energy (2028, high) | 580 TWh |
| Growth rate (2014--2023) | ~13% CAGR |

### PUE Ranges by Data Center Type

The report provides PUE distributions segmented by facility type (hyperscale, colocation, enterprise) and cooling system (air-cooled, evaporative, liquid). These ranges are critical for parameterizing energy models.

### WUE Ranges by Data Center Type

Site-level Water Usage Effectiveness values are reported by cooling technology:

- Air-cooled (no evaporative component): WUE near 0 L/kWh
- Direct evaporative cooling: WUE 1.0--2.5 L/kWh
- Cooling towers: WUE 0.5--2.0 L/kWh
- Hybrid systems: WUE varies significantly by climate and operational mode

### Methodology

The report includes detailed flow charts for modeling PUE and WUE as functions of climate, cooling system type, IT load, and partial load conditions. These methodology diagrams are directly applicable to building a Canadian equivalent model.

### Relevance

Very High. This is the gold standard reference for data center energy and water efficiency parameters. While US-focused, the methodology and benchmark ranges are directly applicable to Canadian facilities operating similar equipment in comparable (or colder) climates.

---

## 2. DOE Best Practices Guide for Energy-Efficient Data Center Design

- **Organization:** US Department of Energy
- **URL:** https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design_0.pdf
- **Publication Date:** July 2024

### Key Metrics Defined

| Metric | Definition | Formula |
|---|---|---|
| PUE | Power Usage Effectiveness | Total Facility Energy / IT Equipment Energy |
| ERE | Energy Reuse Effectiveness | (Total Energy - Reused Energy) / IT Equipment Energy |
| WUE | Water Usage Effectiveness | Annual Site Water Usage / IT Equipment Energy (L/kWh) |
| CUE | Carbon Usage Effectiveness | Total CO2 Emissions / IT Equipment Energy (kgCO2/kWh) |

### Best Practice Recommendations

- Raise cold aisle temperature to ASHRAE recommended range (18--27C)
- Implement hot aisle/cold aisle containment
- Use economizer cooling (air-side or water-side) whenever outdoor conditions permit
- Deploy variable-speed fans and pumps
- Monitor PUE at the rack level, not just the facility level

### Relevance

High for metric definitions and establishing a common vocabulary. The best practice recommendations provide a framework for evaluating whether Canadian facilities are operating at or below industry standards.

---

## 3. Uptime Institute Global Data Center Survey 2024

- **Organization:** Uptime Institute
- **URL:** https://uptimeinstitute.com/resources/research-and-reports/uptime-institute-global-data-center-survey-results-2024

### Key Findings

| Metric | Value |
|---|---|
| Global average PUE (2024) | 1.56 |
| Trend | Flat for 5th consecutive year |
| New builds typical PUE | 1.3 or better |
| Survey respondents | 879 |
| Surveyed DCs older than 11 years | ~50% |

### Interpretation

The stagnation of global average PUE at 1.56 reflects the large installed base of older, less efficient facilities. New builds consistently achieve PUE 1.3 or better, and hyperscale facilities routinely report PUE below 1.2. The gap between new and existing facilities suggests that fleet-wide efficiency improvements depend more on replacing aging infrastructure than on incremental optimization.

### Relevance

High for calibrating PUE assumptions. A Canadian model should distinguish between new-build (PUE 1.2--1.3) and legacy (PUE 1.5--1.8) facilities when estimating aggregate energy consumption.

---

## 4. IEA Energy and AI / Electricity 2025

- **Organization:** International Energy Agency
- **URLs:**
  - https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
  - https://www.iea.org/reports/electricity-2025/demand

### Key Findings

| Metric | Value |
|---|---|
| Global DC electricity consumption (2024) | ~415 TWh |
| Share of global electricity | ~1.5% |
| Projected DC electricity (2030) | ~945 TWh |
| DC sector growth rate | ~15%/year |
| All other sectors growth rate | ~4%/year |

### IEA 4E EDNA Report

The IEA's Energy-Efficient End-use Equipment (4E) programme published a critical review of data center energy modeling approaches through its Electronic Devices and Networks Annex (EDNA). This report evaluates the assumptions and limitations of existing bottom-up and top-down DC energy models.

### Relevance

High for framing the global context. The IEA's projection that data center electricity demand will more than double by 2030, growing nearly four times faster than other sectors, establishes the urgency of the research question.

---

## 5. Big Tech Sustainability Reports

Major hyperscale operators publish annual sustainability reports with facility-level or aggregate efficiency metrics. None break out Canada-specific data; all figures are global aggregates.

### Google Environmental Report 2024/2025

- **URL:** https://sustainability.google/google-2025-environmental-report/

| Metric | Value |
|---|---|
| DC electricity growth | 27% year-over-year |
| Water consumed (2024) | 8.1 billion gallons |
| PUE data | By facility, in supplementary tables |
| WUE data | By facility, in supplementary tables |

Google provides the most granular public disclosure of PUE and WUE by individual facility, making it a useful reference for hyperscale benchmarks.

### Microsoft Environmental Sustainability Report 2025

- **URL:** https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2025-Microsoft-Environmental-Sustainability-Report-PDF.pdf

| Metric | Value |
|---|---|
| Electricity consumption (2024) | 29.8 million MWh |
| Electricity consumption (2020) | 10.8 million MWh |
| Water consumption (2024) | ~6 billion liters |
| Water consumption (2023) | ~8 billion liters |
| New renewable energy contracted | 19 GW across 16 countries |

Microsoft's water consumption dropped from approximately 8 billion liters in 2023 to approximately 6 billion liters in 2024, attributed to a shift toward air-cooled and liquid-cooled systems in newer facilities.

### AWS Sustainability

- **URL:** https://aws.amazon.com/sustainability/data-centers/

| Metric | Value |
|---|---|
| Global PUE (2024) | 1.15 |
| Global WUE (2024) | 0.15 L/kWh |
| WUE improvement | 40% reduction since 2021 |
| Renewable energy projects | 600+ across 28 countries |

AWS reports the lowest published PUE and WUE among the major hyperscalers, though direct comparisons are complicated by differences in measurement methodology and reporting boundaries.

### Applicability to Canadian Analysis

None of these reports provide Canada-specific facility data. The reported PUE and WUE values serve as benchmarks for what hyperscale facilities can achieve. Canadian colocation and enterprise data centers are likely to have higher PUE (1.3--1.6) and higher WUE than these hyperscale benchmarks.

---

## 6. OCP Sustainability Metrics Framework

- **Organization:** Open Compute Project
- **URL:** https://www.opencompute.org/documents/dcf-sustainability-metrics-final-r3-docx-pdf

### Overview

The OCP Sustainability Metrics Framework defines 23 metrics across 5 environmental categories for data center operations.

### Key Metrics

| Metric | Category | Description |
|---|---|---|
| PUE | Energy | Total facility energy / IT energy |
| CUE | Carbon | Total CO2 emissions / IT energy |
| WUE | Water | Site water usage / IT energy |
| REF | Renewables | Renewable energy fraction |

### Aspirational Goals

- Net zero Scope 1, 2, and 3 emissions
- Zero waste to landfill
- Water positive operations

### Relevance

Medium-High. Provides a standardized framework for benchmarking data center environmental performance. Useful for defining the metrics that a Canadian assessment should track.

---

## 7. Green Software Foundation SCI

- **Organization:** Green Software Foundation
- **Standard:** ISO/IEC 21031:2024
- **URL:** https://sci.greensoftware.foundation/

### Formula

```
SCI = (E * I + M) / R
```

Where:

| Variable | Description |
|---|---|
| E | Energy consumed by the software system (kWh) |
| I | Location-based marginal carbon intensity of the grid (gCO2e/kWh) |
| M | Embodied carbon emissions of the hardware (gCO2e) |
| R | Functional unit (e.g., per API call, per user, per transaction) |

### Key Design Decisions

- The SCI explicitly does NOT incorporate carbon offsets or renewable energy certificates (RECs)
- Emphasizes genuine reduction in carbon emissions over accounting mechanisms
- Requires specification of a functional unit, enabling comparison across different software systems and deployment configurations
- Location-based intensity (I) makes the score directly sensitive to where the workload runs

### Application to This Research

The SCI formula directly connects the data sources cataloged in this document:

- **E** is derived from IT load data and PUE (benchmarks in this file)
- **I** is derived from carbon intensity sources (02-carbon-intensity.md)
- **M** requires embodied carbon data for servers and infrastructure (not covered in current dataset catalog)
- **R** is defined by the research question

### Relevance

High. The SCI provides a principled framework for quantifying the carbon benefit of carbon-aware workload placement -- shifting a workload from a high-I region (Alberta, 490 gCO2e/kWh) to a low-I region (Quebec, 1.7 gCO2e/kWh) would reduce the SCI score proportionally.

---

## Summary of Benchmark Values

| Parameter | Low (Best) | Typical | High (Worst) | Source |
|---|---|---|---|---|
| PUE (hyperscale) | 1.10 | 1.15 | 1.25 | AWS, Google, Uptime |
| PUE (colocation) | 1.20 | 1.40 | 1.60 | Uptime, LBNL |
| PUE (enterprise/legacy) | 1.40 | 1.56 | 2.00+ | Uptime |
| WUE (air-cooled) | 0.00 | 0.00 | 0.10 | LBNL |
| WUE (evaporative) | 0.50 | 1.50 | 2.50 | LBNL |
| WUE (hyperscale avg) | 0.15 | 0.50 | 1.00 | AWS, Google |
| CUE (Quebec grid) | 0.002 | -- | -- | ECCC |
| CUE (Alberta grid) | -- | 0.490 | -- | ECCC |
| CUE (Ontario grid) | -- | 0.038 | -- | ECCC |

These benchmark values should be used as default parameters in any modeling exercise, with site-specific data substituted where available.
