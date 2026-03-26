# Water Stress and Climate Data Sources

This document catalogs data sources for evaluating water consumption by data centers and the climate conditions that determine cooling requirements. Water usage is an increasingly scrutinized environmental impact of data center operations, particularly for facilities relying on evaporative cooling.

---

## 1. WRI Aqueduct Water Risk Atlas (v4.0)

- **Organization:** World Resources Institute
- **URL:** https://www.wri.org/applications/aqueduct/water-risk-atlas/
- **GitHub:** https://github.com/wri/Aqueduct40
- **Spatial Coverage:** Global, including full Canada at sub-basin level
- **License:** CC BY 4.0 (free for research and commercial use)

### Available Indicators

| Indicator | Description |
|---|---|
| Baseline Water Stress | Ratio of total withdrawals to available renewable supply |
| Water Depletion | Ratio of total consumption to available renewable supply |
| Interannual Variability | Year-to-year variation in water supply |
| Seasonal Variability | Within-year variation in water supply |
| Drought Risk | Probability and severity of drought events |
| Riverine Flood Risk | Probability and severity of river flooding |
| Coastal Flood Risk | Probability and severity of coastal flooding |
| Groundwater Decline | Rate of groundwater table decline |

### Download Options

- **Location Analyzer:** Upload specific site coordinates for targeted risk assessment
- **Full Database:** Download the entire global dataset as GeoJSON or Shapefile
- **GitHub Repository:** Full dataset and documentation available for programmatic access

### Relevance

High. Essential for evaluating whether water-cooled data centers are sustainable at a given location. A facility sited in a high water-stress sub-basin faces both environmental risk (community impact, reputational damage) and operational risk (potential future water use restrictions). This dataset enables location-specific risk scoring for any candidate site in Canada.

---

## 2. ECCC Climate Normals and Historical Weather Data

- **Organization:** Environment and Climate Change Canada
- **URL (Normals):** https://climate.weather.gc.ca/climate_normals/
- **URL (Extraction Tool):** https://climate-change.canada.ca/climate-data/
- **Spatial Coverage:** 8,756 climate stations across Canada

### Available Datasets

| Dataset | Format | Granularity |
|---|---|---|
| Climate Normals 1991--2020 | CSV, GeoJSON | Monthly (30-year averages) |
| Historical Weather Data | CSV | Hourly, Daily, Monthly |
| Climate Data Extraction Tool | CSV (custom) | Variable |

### Key Variables

- Temperature (mean, max, min)
- Relative humidity
- Wet-bulb temperature (derived)
- Precipitation (rain, snow, total)
- Wind speed and direction
- Heating degree days
- Cooling degree days
- Hours of bright sunshine

### Critical Variables for Data Center Cooling

The most important variables for data center thermal modeling are:

- **Wet-bulb temperature:** Determines the effectiveness of evaporative cooling systems. Lower wet-bulb temperatures enable more efficient free cooling.
- **Dry-bulb temperature:** Determines air-side free cooling potential. ASHRAE recommends data center inlet temperatures up to 27C (Class A1), enabling free cooling whenever outdoor temperature is below this threshold.
- **Relative humidity:** Affects both evaporative cooling efficiency and the need for humidification/dehumidification within the data hall.
- **Cooling degree days (CDD):** Aggregate metric indicating annual mechanical cooling demand.

### Relevance

Very High for cooling load modeling. The number of hours per year where outdoor conditions permit free cooling (air-side or water-side economization) directly determines the PUE and WUE of a facility. Canadian locations generally offer substantial free cooling potential compared to warmer climates, but there is significant variation between, for example, Toronto (CDD ~400) and Montreal (CDD ~300) versus Edmonton (CDD ~100).

---

## 3. Statistics Canada Water Use Tables

- **Organization:** Statistics Canada
- **Spatial Coverage:** National and provincial

### Available Tables

| Table | Content | Frequency |
|---|---|---|
| CANSIM 153-0101 | Water use by sector | Biennial |
| CANSIM 153-0116 | Physical flow account for water use | Biennial |
| Table 38-10-0271-01 | Potable water use by sector | Biennial |

### Key Findings from Available Data

- Industrial, commercial, and institutional sectors used 1,247 million cubic metres of water in 2021, representing 26% of total Canadian water use
- Thermal-electric power generation used 99.3% of its water intake for cooling and condensing purposes
- Residential water use accounted for approximately 55% of total potable water use

### Critical Limitation

Data centers are NOT broken out as a separate category in Statistics Canada reporting. They fall within the commercial/institutional aggregate, which also includes offices, retail, hospitals, schools, and other commercial buildings. This means there is no official Canadian statistical source for data center water consumption at the national level.

### Relevance

Medium. Provides useful sectoral baselines for contextualizing data center water use within total commercial water consumption. The absence of DC-specific data is itself a significant finding that underscores the lack of transparency in Canadian data center water reporting.

---

## 4. Known Canadian Data Center Water Data Points

Despite the absence of systematic reporting, several specific data points have emerged through investigative journalism, municipal planning documents, and industry disclosures.

| Facility / Region | Water Usage | Source |
|---|---|---|
| Etobicoke, Toronto (proposed) | Approved for 39.75 L/s withdrawal | CBC News |
| Microsoft complex, Vaughan ON | Expected 730 million L/year | CBC News / municipal planning |
| 1 MW data center (generic benchmark) | Up to 25.5 million L/year | Industry benchmark estimates |
| QScale Q01, Levis QC | ~100 MW waste heat redirected to households | QScale industry reporting |

### CBC Investigative Reporting

- **URL:** https://www.cbc.ca/news/ai-data-centre-canada-water-use-9.6939684
- Published 2024
- Investigated water permits and municipal planning documents for large data center projects in the Greater Toronto Area
- Found that individual facilities can consume water at rates comparable to small municipalities
- Highlighted the lack of federal or provincial disclosure requirements for data center water use

### Contextualizing the Numbers

- The Microsoft Vaughan facility's expected 730 million L/year is roughly equivalent to the annual water consumption of a town of 12,000--15,000 residents
- The 39.75 L/s withdrawal rate for the Etobicoke facility equates to approximately 1.25 billion L/year if operating at full capacity
- These figures are site-specific and depend heavily on the cooling technology deployed, local climate conditions, and IT load

### Relevance

The scarcity of systematic Canadian data center water reporting is itself a key finding that motivates research in this area. The available data points, while limited, demonstrate that individual large facilities can have material impacts on local water resources.

---

## 5. Additional Climate Data Sources

### ERA5 Reanalysis (Copernicus Climate Data Store)

- **Organization:** European Centre for Medium-Range Weather Forecasts (ECMWF)
- **URL:** https://cds.climate.copernicus.eu/
- **Coverage:** Global, 0.25-degree grid resolution
- **Variables:** Temperature, humidity, wind, precipitation, radiation, and hundreds of others
- **Granularity:** Hourly, 1940 -- present
- **Access:** Free registration required

ERA5 provides spatially continuous hourly climate data for any location in Canada, filling gaps where ECCC station coverage is sparse. Particularly useful for sites that are distant from the nearest weather station.

### Canadian Regional Climate Model (CanRCM4)

- **Organization:** Environment and Climate Change Canada
- **URL:** https://climate-scenarios.canada.ca/
- **Coverage:** Canada, ~25 km grid resolution
- **Variables:** Projected temperature, precipitation, humidity under RCP 2.6, 4.5, and 8.5 scenarios
- **Granularity:** Daily, projections to 2100

Relevant for assessing how climate change will affect future cooling requirements. A facility being built today will operate for 15--25 years; projections indicate that cooling degree days may increase by 30--50% in southern Ontario by 2050 under moderate warming scenarios.

---

## Integration Notes

### Water-Energy Nexus

Water and energy data must be analyzed jointly for data center impact assessment:

- Evaporative cooling reduces electricity consumption (lower PUE) but increases water consumption (higher WUE)
- Air-cooled systems eliminate water use but require more electricity for fans and compressors
- The optimal cooling strategy depends on local water stress, grid carbon intensity, and climate conditions

### Recommended Workflow

1. Use WRI Aqueduct to classify candidate sites by water stress level
2. Use ECCC Climate Normals to estimate annual free cooling hours and required mechanical cooling capacity
3. Use the water-energy tradeoff to model PUE and WUE for each cooling configuration
4. Validate against known Canadian data points (CBC reporting, municipal records) where available
5. Use ERA5 for any sites lacking nearby ECCC weather stations
6. Apply CanRCM4 projections for forward-looking risk assessment
