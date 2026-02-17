# Grid and Electricity Data Sources

This document catalogs the primary data sources for Canadian grid electricity generation, demand, and pricing. Each source is documented with access details, temporal and spatial granularity, and relevance to data center carbon footprint modeling.

---

## 1. IESO -- Ontario

- **Organization:** Independent Electricity System Operator
- **URL:** https://www.ieso.ca/power-data/data-directory
- **Spatial Coverage:** Ontario

### Available Datasets

| Dataset | Format | Granularity | Historical Depth |
|---|---|---|---|
| Generator Output & Capability Report | CSV, XML | Hourly | 2010 -- present |
| Generator Output by Fuel Type | XML | Hourly | Multi-year |
| Ontario and Market Demand | CSV, XML | Hourly | Rolling 30 days |
| Variable Generation Forecast (Wind/Solar) | CSV | Hourly | Rolling |
| Industrial Load by Sector | CSV | Monthly | Multi-year |
| Day-ahead Zonal Price | CSV | Hourly | Multi-year |

### Key Fields

- Generation by fuel type: Nuclear, Hydro, Gas, Wind, Solar, Biofuel (MW)
- System demand (MW)
- Zonal and Hourly Ontario Energy Price ($/MWh)

### Programmatic Access

- **`gridstatus` Python library** (`pip install gridstatus`)
- Wraps IESO data with convenience methods including `get_fuel_mix()` and `get_load()`
- Also supports other North American ISOs for cross-border comparison

### Access Restrictions

- All datasets are publicly available at no cost
- No API key required for direct CSV/XML downloads
- `gridstatus` library is open-source (MIT license)

### Relevance

Essential for computing time-varying carbon intensity for the Toronto corridor, which hosts approximately 40% of Canadian data center capacity. Hourly fuel-mix data enables marginal emissions modeling rather than relying on static annual averages.

---

## 2. AESO -- Alberta

- **Organization:** Alberta Electric System Operator
- **URL:** https://www.aeso.ca/market/market-and-system-reporting/data-requests/
- **Spatial Coverage:** Alberta

### Available Datasets

| Dataset | Format | Granularity | Historical Depth |
|---|---|---|---|
| Hourly Generation Metered Volumes | CSV | Hourly | 2001 -- July 2025 |
| Pool Price | CSV | Hourly | 2001 -- July 2025 |
| Alberta Internal Load (AIL) | CSV | Hourly | 2001 -- July 2025 |
| Historical Generation Data | CSV | 5-min, Hourly | Multi-year |
| Hourly Load by Area/Region | CSV | Hourly | Jan 2011 -- Dec 2024 |

### Key Fields

- Generation metered volumes by asset and fuel type (MW)
- Pool price ($/MWh)
- Alberta Internal Load (MW)
- Area and regional load breakdowns

### Programmatic Access

- JSON API available for real-time and near-real-time data
- `gridstatus` Python library also supports AESO
- Custom data requests available at $100/hr with 10--15 business day turnaround

### Access Restrictions

- Standard datasets are publicly available
- Custom data extracts require a formal request and fee

### Relevance

Critical for this project. Calgary is the fastest-growing Canadian data center market, with over 25% of planned future capacity. Alberta's grid is fossil-heavy, with an annual average intensity of approximately 490 gCO2e/kWh, making it the jurisdiction where data center siting decisions have the largest marginal carbon impact.

---

## 3. Hydro-Quebec -- Quebec

- **Organization:** Hydro-Quebec
- **URL:** https://donnees.hydroquebec.com/explore/
- **Spatial Coverage:** Quebec

### Available Datasets

| Dataset | Format | Granularity | Historical Depth |
|---|---|---|---|
| Sources of Electricity Generated | CSV, API | Hourly | May 2021 -- present |
| Electricity Demand | CSV, API | 15-minute | Multi-year |
| Historical Generation | CSV | Hourly | Multi-year |
| Estimate of Direct GHG Emissions | CSV | Variable | Multi-year |

### Key Fields

- Date and timestamp
- Total generation (MW)
- Generation by source: hydraulique, eolien, solaire, thermique, autres

### Programmatic Access

- **REST API endpoint:**
  ```
  https://donnees.hydroquebec.com/api/explore/v2.1/catalog/datasets/production-electricite-quebec/records
  ```
- **`electricite-quebec` Python package** (`pip install electricite-quebec`)
- No authentication required for public datasets

### Access Restrictions

- All datasets are publicly available under open data license
- API is rate-limited but accessible without registration

### Relevance

High. Montreal is the second-largest Canadian data center market. Quebec's near-zero carbon grid (approximately 1.7 gCO2e/kWh) makes it a prime candidate for carbon-optimized workload placement. The 15-minute demand data enables fine-grained modeling of grid stress periods.

---

## 4. BC Hydro -- British Columbia

- **Organization:** BC Hydro
- **URL:** https://www.bchydro.com/energy-in-bc/operations/transmission/transmission-system/balancing-authority-load-data.html
- **Spatial Coverage:** British Columbia

### Available Datasets

| Dataset | Format | Granularity | Historical Depth |
|---|---|---|---|
| Balancing Authority Load Data | Excel | Hourly, Daily | Multi-year |
| Actual Flow Data | Excel | 5-minute | Multi-year |
| Historical Total Hourly Actual Flow | Excel | Hourly | Multi-year |

### Key Fields

- System load (MW)
- Transmission flow volumes
- Import/export flows

### Programmatic Access

- No dedicated API available
- Data distributed as Excel workbooks requiring manual or scripted download

### Limitations

- No real-time generation-by-fuel-type breakdown via open API
- Load data is available but fuel-mix must be inferred from annual reports or third-party sources (e.g., CCEI)

### Relevance

Medium. British Columbia's grid is over 95% hydroelectric (approximately 15 gCO2e/kWh). Vancouver has 28+ data center facilities. The lack of granular fuel-mix data is partially mitigated by the grid's near-constant low-carbon composition.

---

## 5. SaskPower -- Saskatchewan

- **Organization:** SaskPower
- **URL:** https://www.saskpower.com/
- **Spatial Coverage:** Saskatchewan

### Available Data

- Daily generation breakdowns by fuel type available since September 2022
- Reported as daily averages only
- No programmatic API available

### Limitations

- Coarse temporal granularity (daily average rather than hourly)
- No structured download or API endpoint

### Relevance

Low-Medium. Saskatchewan has a high-carbon grid (approximately 670 gCO2e/kWh) but limited data center presence. Useful for completeness in national modeling but not a priority market.

---

## 6. CCEI -- Canadian Centre for Energy Information (NRCan)

- **Organization:** Natural Resources Canada
- **URL:** https://energy-information.canada.ca/en/resources/high-frequency-electricity-data
- **Spatial Coverage:** All provinces and territories

### Available Variables

- Demand/load
- Generation by fuel type
- Reserve margins
- Pricing
- Imports/exports

### Granularity

- Hourly for most variables (some 5-minute data available)

### Programmatic Access

- **JSON API:** `https://energy-information.canada.ca/en/json/`
- Structured endpoints for each province and variable

### Data Quality Note

The CCEI aggregates data from provincial ISOs and utilities via web-scraping methods. This can introduce gaps, duplicates, and lag compared to primary ISO sources. Recommended practice: use CCEI for cross-provincial comparison and discovery, but validate against primary ISO sources for any single-province analysis.

### Relevance

Very High. This is the best unified multi-provincial source with API access. It enables consistent cross-provincial comparison without needing to integrate disparate ISO data formats individually.

---

## 7. Statistics Canada Table 25-10-0015-01

- **Organization:** Statistics Canada
- **URL:** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2510001501
- **Spatial Coverage:** National and provincial

### Description

Monthly electric power generation by type of electricity (hydraulic turbine, steam turbine, nuclear, combustion turbine, wind, solar, tidal, other). Data available at both national and provincial levels.

### Latest Release

January 30, 2026.

### Format

- CSV download via Statistics Canada Open License
- CANSIM/CODR table format

### Relevance

High for establishing historical baselines and performing cross-provincial trend analysis. Monthly granularity is sufficient for long-term capacity planning but too coarse for operational carbon intensity modeling.

---

## 8. Canada Energy Regulator (CER)

- **Organization:** Canada Energy Regulator
- **URL:** https://open.canada.ca/data/en/dataset/2cdf43fc-d4aa-4604-9f21-29777d955810
- **Spatial Coverage:** National and provincial

### Available Datasets

| Dataset | Format | Temporal Coverage |
|---|---|---|
| Electricity Generation and Capacity | CSV | Annual, 2005 -- 2016 |
| Provincial/Territorial Energy Profiles | HTML, PDF | Current |
| Canada's Energy Future Projections | CSV, PDF | Projections to 2050 |

### Relevance

Medium. The historical generation dataset has a limited time range (ending 2016). The Energy Future projections are valuable for modeling forward-looking scenarios for grid decarbonization and data center demand growth.

---

## Summary Table

| Source | Format | Granularity | Spatial Coverage | Access | Primary Use |
|---|---|---|---|---|---|
| IESO (Ontario) | CSV, XML | Hourly | Ontario | Free, open | Real-time fuel mix and carbon intensity |
| AESO (Alberta) | CSV, JSON | Hourly, 5-min | Alberta | Free + paid custom | Fossil-heavy grid carbon modeling |
| Hydro-Quebec | CSV, REST API | 15-min, Hourly | Quebec | Free, open | Low-carbon grid baseline |
| BC Hydro | Excel | Hourly, 5-min | British Columbia | Free | Load data for BC corridor |
| SaskPower | Web only | Daily | Saskatchewan | Free | National completeness |
| CCEI (NRCan) | JSON API | Hourly, 5-min | All provinces | Free, open | Unified cross-provincial comparison |
| Statistics Canada | CSV | Monthly | National + provincial | Free, open | Historical baselines and trends |
| CER | CSV, PDF | Annual | National + provincial | Free, open | Future demand projections |

---

## Recommended Integration Approach

1. **Primary sources:** Use IESO, AESO, and Hydro-Quebec APIs for the three largest data center markets (Ontario, Alberta, Quebec).
2. **Cross-provincial layer:** Use CCEI as the unified backbone for consistent multi-province analysis.
3. **Validation:** Cross-check CCEI data against primary ISO sources for each province.
4. **Programmatic access:** Leverage `gridstatus` for IESO and AESO, `electricite-quebec` for Hydro-Quebec, and direct JSON for CCEI.
5. **Historical context:** Use Statistics Canada and CER datasets for long-term trend analysis and future projections.
