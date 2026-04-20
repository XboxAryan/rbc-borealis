# Carbon Intensity Data Sources

This document catalogs the primary data sources for computing and validating carbon intensity of electricity consumed by Canadian data centers. Carbon intensity -- expressed in gCO2e/kWh -- is the central metric linking data center energy consumption to environmental impact.

---

## 1. Electricity Maps

- **Organization:** Electricity Maps (formerly electricityMap)
- **URL:** https://app.electricitymaps.com/datasets
- **API Documentation:** https://portal.electricitymaps.com/developer-hub/api/getting-started
- **Open-Source Parsers:** https://github.com/electricitymaps/electricitymaps-contrib

### Canadian Zone Coverage

Electricity Maps defines 11 Canadian zones:

| Zone Code | Region |
|---|---|
| CA-AB | Alberta |
| CA-BC | British Columbia |
| CA-MB | Manitoba |
| CA-NB | New Brunswick |
| CA-NL | Newfoundland and Labrador |
| CA-NS | Nova Scotia |
| CA-ON | Ontario |
| CA-PE | Prince Edward Island |
| CA-QC | Quebec |
| CA-SK | Saskatchewan |
| CA-YT | Yukon |

### Free Tier

- Live carbon intensity for 200+ regions worldwide
- Single API endpoint: `/v3/carbon-intensity/latest`
- Rate-limited (exact limits vary; check current documentation)
- 5 free CSV dataset downloads from the historical data portal

### Historical Data

- Available for download at yearly, monthly, daily, and sub-hourly (5-minute) granularity
- Coverage: 2021 -- 2024
- Format: CSV

### Methodology

- Reports gCO2eq/kWh including life-cycle emissions (not just direct combustion)
- Accounts for cross-border electricity imports and exports
- Uses real-time generation data from ISOs and utilities
- Open-source parsers on GitHub enable local replication and validation of methodology

### Access Model

| Tier | Historical Data | Live API | Cost |
|---|---|---|---|
| Free | 5 CSV downloads | 1 endpoint, rate-limited | $0 |
| Paid (research) | Full archive, programmatic | Multiple endpoints | Contact for pricing |
| Enterprise | Full archive, SLA | Full API suite | Contact for pricing |

### Relevance

Very High. Electricity Maps provides pre-computed carbon intensity at high temporal granularity, eliminating the need to build custom emission factor pipelines from raw generation data. The 11 Canadian zones cover all major data center markets.

---

## 2. ECCC Provincial Emission Factors (Official Government Values)

- **Organization:** Environment and Climate Change Canada
- **URL:** https://www.canada.ca/en/environment-climate-change/services/climate-change/pricing-pollution-how-it-will-work/output-based-pricing-system/federal-greenhouse-gas-offset-system/emission-factors-reference-values.html
- **Spatial Coverage:** All provinces and territories

### 2025 Provincial Emission Factors

| Province/Territory | Emission Factor (gCO2e/kWh) |
|---|---|
| Manitoba | 1.4 |
| Quebec | 1.7 |
| British Columbia | 15 |
| Newfoundland and Labrador | 18 |
| Ontario | 38 |
| Yukon | 70 |
| Northwest Territories | 190 |
| New Brunswick | 350 |
| Prince Edward Island | 350 |
| Alberta | 490 |
| Saskatchewan | 670 |
| Nova Scotia | 700 |
| Nunavut | 820 |

### Methodology

- These are annual average consumption-based intensities
- Account for inter-provincial electricity transfers (imports and exports)
- Published by ECCC for the Federal Greenhouse Gas Offset System
- Values are available for calendar years 2023 through 2026

### Key Observations

- The range spans nearly three orders of magnitude: Manitoba at 1.4 gCO2e/kWh versus Nunavut at 820 gCO2e/kWh
- Ontario (38 gCO2e/kWh) is relatively clean due to nuclear and hydro dominance, but hourly variability can be significant when gas peakers are dispatched
- Alberta (490 gCO2e/kWh) is the critical jurisdiction for carbon-aware data center siting given the rapid growth in DC capacity there

### Relevance

Very High. These are the official Government of Canada ground truth values for annual calibration of any carbon intensity model. Any project-level estimates should be reconcilable with these published factors.

---

## 3. National Inventory Report (NIR) Part 3

- **Organization:** Environment and Climate Change Canada
- **URL:** https://open.canada.ca/data/en/dataset/779c7bcf-4982-47eb-af1b-a33618a05e5b
- **Spatial Coverage:** National and provincial

### Available Tables

| Table | Content |
|---|---|
| A13-2 through A13-14 | Provincial electricity GHG intensity time series |
| Coverage period | 1990 -- 2022 |
| Format | CSV, Excel (via Open Government Portal) |

### Description

The National Inventory Report is Canada's official submission to the UNFCCC. Part 3 contains detailed annexes with provincial electricity generation and associated GHG emissions data spanning over three decades.

### Key Use Cases

- Establishing long-term trends in grid decarbonization by province
- Quantifying the rate of change in emission factors over time
- Identifying provinces where grid carbon intensity is declining fastest (or stalling)

### Relevance

High for historical trend analysis. The 30+ year time series shows the trajectory of grid decarbonization for each province, which is essential context for projecting future carbon intensity and evaluating the long-term value of carbon-aware workload placement strategies.

---

## 4. IEA Emissions Factors 2025

- **Organization:** International Energy Agency
- **Spatial Coverage:** National level (Canada aggregate)

### Description

The IEA publishes annual emission factors for electricity generation by country. For Canada, this provides a single national-level factor that does not distinguish between provinces.

### Access

- Database product (paid subscription)
- Some research institutions have institutional access
- Not freely available for general use

### Limitations

- National-level only: does not capture the massive inter-provincial variation (1.4 to 820 gCO2e/kWh)
- Primarily useful for international benchmarking rather than provincial-level modeling

### Relevance

Low for provincial modeling. Useful only for comparing Canada's aggregate grid intensity against other countries.

---

## 5. Climatiq API

- **Organization:** Climatiq
- **URL:** https://www.climatiq.io/data/source/government-of-canada
- **Spatial Coverage:** Provincial (sourced from Government of Canada data)

### Description

Climatiq provides a REST API that offers pre-parsed access to Canadian government emission factors alongside emission factors from hundreds of other sources globally.

### Access

- Free tier available with rate limits
- REST API with JSON responses
- No special authentication beyond API key registration

### Key Advantage

Programmatic access to official Canadian emission factors without needing to manually parse government publications. Useful for integrating emission factors into automated pipelines.

### Relevance

Medium. Offers convenience for programmatic access to factors that are also available directly from ECCC. Adds value through a standardized API format and the ability to query multiple countries' factors through a single interface.

---

## Integration Strategy

### Temporal Resolution Hierarchy

For modeling carbon intensity at different time scales, the following hierarchy is recommended:

| Time Scale | Primary Source | Fallback Source |
|---|---|---|
| Sub-hourly (5-min) | Electricity Maps | Primary ISO data + custom pipeline |
| Hourly | Electricity Maps, CCEI | Primary ISO data + gridstatus |
| Daily | Electricity Maps aggregated | CCEI aggregated |
| Monthly | Statistics Canada 25-10-0015 | NIR Part 3 |
| Annual | ECCC Provincial Factors | NIR Part 3, IEA |

### Validation Approach

1. Use ECCC Provincial Emission Factors as the annual ground truth
2. Aggregate hourly Electricity Maps data to annual averages
3. Compare the two: deviations beyond 10% warrant investigation into methodological differences (e.g., life-cycle vs. direct emissions, treatment of imports/exports)
4. Use NIR historical data to validate that trends are consistent across sources

### Marginal vs. Average Emission Factors

A critical methodological decision is whether to use average or marginal emission factors:

- **Average intensity:** Total emissions divided by total generation. Appropriate for attributional accounting (e.g., reporting a data center's annual carbon footprint).
- **Marginal intensity:** The emission rate of the generator that would be dispatched next (or curtailed) in response to a change in load. Appropriate for consequential analysis (e.g., evaluating the carbon impact of adding a new data center to the grid).

Electricity Maps provides both average and marginal intensity estimates. ECCC factors are average-based. The choice between them depends on the research question being asked.
