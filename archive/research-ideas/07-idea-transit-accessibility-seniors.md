# Idea #6: Predicting Transit Accessibility Gaps for Seniors and Disabled Persons

**Acceptance Likelihood: 3.7/5 — Good Pick (Higher Risk)**

---

## The Problem

Canada's population is aging rapidly. As physical capabilities decline and retirement incomes limit car ownership, seniors become increasingly dependent on public transit. Yet transit systems are largely designed for commuters, not elderly or disabled riders.

### Key Statistics
- **18.5%** of Canadians are aged 65+ (2024), projected to reach **25%** by 2050
- Seniors are **more dependent on transit** than working-age adults once they stop driving
- Only **57%** of Canadians aged 65+ have access to convenient public transit
- **22%** of Canadians have at least one disability affecting mobility
- Social isolation among seniors is linked to poor transit access — increases dementia and depression risk
- Rural and suburban seniors have the worst access to transit

### Why It Matters
Transit accessibility directly affects seniors' ability to access healthcare, grocery stores, social activities, and essential services. Poor transit means isolation, missed medical appointments, food insecurity, and declining health. Identifying transit gaps helps cities prioritize route expansions, paratransit services, and accessible infrastructure investment.

---

## Why Machine Learning Can Help

Transit accessibility is a function of multiple interacting spatial and demographic features:

- **Transit route coverage** (stops, frequency, hours of operation)
- **Population density of seniors** by neighborhood
- **Distance to key destinations** (hospitals, pharmacies, grocery stores, community centers)
- **Walkability and terrain** (hills, sidewalk quality, winter conditions)
- **Service reliability** (delays, cancellations)
- **Disability prevalence** by area

ML can combine these into a composite accessibility score and identify neighborhoods where the gap between need and service is largest.

### ML Tasks
1. **Regression:** Predict accessibility score from transit + demographic features
2. **Clustering:** Identify typologies of underserved neighborhoods
3. **Classification:** Flag areas where senior density is high but transit access is low
4. **Gap analysis:** Rank neighborhoods by accessibility deficit

### Published Approaches
- **Logistic regression:** Used to model transit usage frequency among seniors across 6 Canadian regions
- **Statistical + ML comparison:** Random Forest vs. logistic regression for transit ridership in equity context
- **Spatial accessibility measures:** StatCan computed 28 measures combining transit data with destinations

---

## Datasets

### 1. StatCan Spatial Accessibility Measures (Primary)
- **Source:** Statistics Canada
- **URL:** https://www150.statcan.gc.ca/n1/pub/18-001-x/18-001-x2024005-eng.htm
- **Contains:** 28 accessibility measures: 7 destinations (employment, healthcare, education, grocery, sports, cultural, childcare) x 3 transport modes (walking, transit peak, transit off-peak) x coverage types
- **Format:** Downloadable data tables

### 2. Metrolinx Mobility Assessment (GTHA)
- **Source:** Metrolinx
- **URL:** https://assets.metrolinx.com/image/upload/v1663240156/Documents/Metrolinx/Assessing_and_Measuring_the_Factors_Affecting_Mobility_Transportation_Accessibility_and_Social_Need.pdf
- **Contains:** Detailed mobility and accessibility assessment for Greater Toronto and Hamilton Area
- **Use:** Methodology reference and supplementary data for GTHA-focused model

### 3. Municipal GTFS Transit Feeds
- **Source:** Transit agencies (TTC, TransLink, STM, OC Transpo, etc.)
- **Contains:** Real-time and scheduled transit data (routes, stops, frequencies, delays)
- **Format:** GTFS standard — machine-readable, widely available
- **Use:** Feature engineering for transit service quality metrics

---

## Proposed ML Pipeline

```
1. Data collection & integration
   - Download StatCan accessibility measures
   - Obtain Census data on senior population density by dissemination area
   - Download GTFS feeds for target cities (Toronto, Vancouver, Montreal)
   - Get destination locations (hospitals, pharmacies, grocery stores) from open data

2. Feature engineering
   - Senior density score per neighborhood
   - Transit frequency within walking distance
   - Average travel time to top-5 senior-relevant destinations
   - Walkability index (sidewalks, elevation, winter conditions)
   - Service reliability metrics (from GTFS real-time data)

3. Model training
   - Random Forest regressor (predict composite accessibility score)
   - K-means clustering (identify neighborhood typologies)
   - Logistic regression (classify underserved vs. well-served areas)
   - Spatial autocorrelation analysis

4. Evaluation
   - Regression accuracy (MAE, R²)
   - Cluster interpretability (do typologies make intuitive sense?)
   - Validation against known senior-underserved areas
   - Cross-city generalization

5. Deliverable
   - Interactive map of transit accessibility gaps for seniors
   - Neighborhood ranking by accessibility deficit
   - Recommendations for route extensions and paratransit placement
```

---

## Strengths

- **Completely novel:** Never attempted in Let's SOLVE It. Fresh territory.
- **Growing importance:** Aging population makes this increasingly relevant
- **Government data exists:** StatCan accessibility measures + GTFS feeds are free and well-structured
- **Equity angle:** Directly helps vulnerable population (elderly, disabled)
- **Policy-relevant:** Cities actively making transit investment decisions

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Hard to scope tightly | Focus on single city (Toronto or Vancouver). Limit to 3-5 destination types. |
| Accessibility is multidimensional | Pick a clear primary metric (e.g., travel time to healthcare) |
| GTFS data integration complex | Use pre-computed StatCan measures as primary. GTFS as stretch goal. |
| Weaker ML task definition | Frame clearly: predict which neighborhoods will lose transit access as routes change |
| Requires spatial analysis expertise | Use standard libraries (GeoPandas, Folium) — well-documented for Python |

---

## References

- StatCan (2024): "Active and Public Transportation Spatial Accessibility Measures" — https://www150.statcan.gc.ca/n1/pub/18-001-x/18-001-x2024005-eng.htm
- ScienceDirect (2023): "An accessibility-based methodology to prioritize public-transit investments for older adults in Canada" — https://www.sciencedirect.com/science/article/pii/S0143622823001534
- ScienceDirect (2025): "Examining the influence of personal-time-based accessibility on public transit use among older adults across Canada" — https://www.sciencedirect.com/science/article/pii/S2590198225000600
- Metrolinx: "Assessing and Measuring Factors Affecting Mobility" — https://assets.metrolinx.com/image/upload/v1663240156/Documents/Metrolinx/Assessing_and_Measuring_the_Factors_Affecting_Mobility_Transportation_Accessibility_and_Social_Need.pdf
