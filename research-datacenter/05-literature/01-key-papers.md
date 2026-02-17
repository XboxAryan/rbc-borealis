# Key Research Papers and Reports

---

## Overview

This document provides an annotated bibliography of the primary research papers and technical reports informing the Societal Impact Score methodology. Each entry includes the full citation, URL, key findings, and specific relevance to this project. Entries are organized by thematic category.

---

## Data Center Environmental Impact

### 1. Dandres et al. 2016 -- Consequences of Future Data Center Deployment in Canada

- **Citation:** Dandres, T., Vandromme, N., Obrekht, G., Wong, A., Nguyen, K.K., Lemieux, Y., Cheriet, M. & Samson, R. "Consequences of Future Data Center Deployment in Canada on Electricity Generation and Environmental Impacts: A 2015-2030 Prospective Study." *Journal of Industrial Ecology* (Yale University), 20(5), 1312-1322, 2016. DOI: 10.1111/jiec.12515
- **Key Findings:**
  - Marginal electricity serving new DC loads in Canada is 47-55% natural gas and 38-48% coal
  - Marginal GHG intensity: 0.85-1.01 kg CO2-eq/kWh -- roughly 5-6x higher than Canada's average of 0.16 kg CO2-eq/kWh
  - 60-70% of marginal electricity comes from reduced electricity exports to the United States, not new Canadian generation
  - Larger deployments (750 MW) have the lowest environmental impact per MW installed across 3 of 4 indicators (economies of scale)
  - Used consequential LCA (CLCA) with the Energy 2020 technoeconomic model + ecoinvent + SimaPro + IMPACT2002+
  - Tracked 4 impact categories: climate change (kg CO2-eq), human health (DALY), ecosystem quality (PDF/m2/yr), natural resources (MJ primary)
  - Modeled 5 scenarios (30-750 MW additional demand by 2030) deployed across Ontario (50%), Quebec (25%), Alberta (25%)
- **Stated Limitations (gaps our project fills):**
  - Could NOT run Monte Carlo simulations for uncertainty quantification -- our SIS provides this
  - Limited to 5 scenarios with no sensitivity analysis -- our tool supports arbitrary configurations
  - No spatial resolution below province level -- our tool scores individual cities
  - No water consumption or cooling efficiency modeling -- our Sub-Models 3 and 4 fill this gap
  - No operational tool produced -- we deliver an open-source scoring tool with interactive visualization
- **Relevance:** The most directly relevant prior work to this project. Dandres et al. established two critical insights: (1) average grid intensity dramatically underestimates the carbon impact of new DC loads because marginal generation is fossil-dominated, and (2) cross-border export displacement is a major externality. Our SIS extends this work by adding uncertainty quantification, water modeling, sub-provincial spatial resolution, and an operational open-source tool -- addressing every limitation the authors identified.

### 2. Xiao & You 2025 -- Roadmap for AI Data Center Sustainability

- **Citation:** Xiao, D. & You, F. "Powering AI data centers sustainably." *Nature Sustainability*, November 2025.
- **Coverage:** Cornell Chronicle: https://news.cornell.edu/stories/2025/11/roadmap-shows-environmental-impact-ai-data-center-boom
- **Key Findings:**
  - US AI data centers projected to emit 24-44 MtCO2/year by 2030
  - Water consumption equivalent to household usage for 6-10 million Americans
  - Smart siting alone reduces water consumption by 52%
  - Coordinated strategies (siting + grid decarbonization + efficient technology) achieve 73% CO2 reduction and 86% water reduction
  - Identified optimal US siting locations: Texas (wind/solar), Montana/Nebraska/South Dakota (wind corridor), New York (nuclear + hydro), Pacific Northwest (hydro)
- **Relevance:** Foundational reference for this project. Demonstrates that siting is the single highest-leverage intervention for data center environmental impact. The study is US-focused, which is precisely the gap this project fills for Canada. Our methodology extends their conceptual framework into an operational, uncertainty-aware scoring tool.

### 2. Patterns 2025 -- Carbon and Water Footprints of Data Centers

- **Citation:** "Carbon and Water Footprints of Data Centers." Patterns, 2025.
- **URL:** https://www.cell.com/patterns/fulltext/S2666-3899(25)00278-8
- **Key Findings:**
  - Comprehensive review of data center environmental impact metrics and measurement methodologies
  - Establishes current best practices for carbon and water footprint accounting at the facility level
  - Identifies gaps in existing measurement frameworks
- **Relevance:** Provides the methodological context for how carbon and water footprints should be measured. Validates our choice of metrics (gCO2/kWh, L/kWh) as aligned with current research consensus.

### 3. Frontiers 2024 -- Forecasting US Data Center CO2 Emissions

- **Citation:** "Forecasting US Data Center CO2 Emissions." Frontiers in Sustainability, 2024.
- **URL:** https://www.frontiersin.org/journals/sustainability/articles/10.3389/frsus.2024.1507030/full
- **Key Findings:**
  - Developed national-level carbon emission forecasting methodology for the US data center sector
  - Demonstrated that sector-level forecasting is feasible using publicly available grid and capacity data
  - Showed that emission trajectories are highly sensitive to grid decarbonization assumptions
- **Relevance:** Methodology reference for carbon forecasting at a national/regional level. Validates the feasibility of emission forecasting from public data, which is the approach we adopt for Canadian provinces.

---

## Carbon Intensity Forecasting

### 4. Maji et al. 2022 -- CarbonCast

- **Citation:** Maji, D., et al. "CarbonCast: Multi-Day Forecasting of Grid Carbon Intensity." ACM BuildSys, 2022.
- **Paper:** https://dl.acm.org/doi/abs/10.1145/3563357.3564079
- **Code:** https://github.com/carbonfirst/CarbonCast
- **Key Findings:**
  - Open-source framework for multi-day carbon intensity forecasting
  - CNN-LSTM architecture achieving MAPE 4.80-13.93% for 96-hour forecasts across 6 US regions
  - Robust to noisy and incomplete input data
  - Uses weather forecasts, historical generation mix, and demand patterns as inputs
  - Demonstrated that carbon-aware workload scheduling can reduce emissions by 10-20% without performance degradation
- **Relevance:** Primary methodological reference for our carbon intensity sub-model. The CNN-LSTM architecture is adaptable to Canadian provincial grids. The open-source codebase provides a potential integration target for the stretch goal. For the MVP, we use a simpler Prophet baseline but validate against CarbonCast's published benchmarks.

### 5. Jones 2025 -- Ensemble Approach for Emission Prediction

- **Citation:** Jones, 2025. Ensemble approach combining XGBoost, LSTM, and SARIMA for power plant emission prediction.
- **Key Findings:**
  - Achieved R-squared = 0.96 on power plant emission prediction
  - Ensemble of XGBoost + LSTM + SARIMA outperformed any individual model
  - XGBoost alone achieved R-squared = 0.91, demonstrating strong standalone performance
  - Feature importance analysis identified generation mix and time-of-day as dominant predictors
- **Relevance:** Validates the ensemble approach we plan to use. Demonstrates that XGBoost provides a strong baseline that can be improved incrementally with temporal models. Supports our MVP strategy of starting with XGBoost and adding Prophet as a complementary temporal model.

---

## Grid Load Forecasting

### 6. Jang et al. 2024 -- Comparative Analysis of Deep Learning for Load Forecasting

- **Citation:** Jang, J., et al. "Comparative Analysis of Deep Learning and Traditional Machine Learning Approaches for Electrical Load Forecasting." International Journal of Energy Research, 2024.
- **URL:** https://onlinelibrary.wiley.com/doi/full/10.1155/2024/5587728
- **Key Findings:**
  - Systematic comparison of 8 model architectures on electrical load forecasting
  - Hybrid LSTM-XGBoost achieves best performance: MAPE 1.18%, R-squared 0.994
  - XGBoost alone achieves MAPE 2.61%, R-squared 0.987 -- competitive with deep learning
  - Feature engineering (temporal, weather, lag features) matters more than model architecture
  - Deep learning provides marginal gains over gradient boosting at significantly higher computational cost
- **Relevance:** Primary benchmark for our grid stress sub-model. Validates XGBoost as sufficient for MVP (no need for deep learning complexity). The feature engineering recommendations directly inform our feature matrix design.

### 7. Nature Scientific Reports 2022 -- Optimised XGBoost for Short-term Load Forecasting

- **Citation:** "Optimised XGBoost Model for Short-term Electric Load Forecasting." Nature Scientific Reports, 2022.
- **URL:** https://www.nature.com/articles/s41598-022-22024-3
- **Key Findings:**
  - XGBoost alone achieves MAPE 2.61% on short-term (1-24 hour) load forecasting
  - Bayesian hyperparameter optimization (learning rate, max depth, n_estimators) improves performance by 15-20% over default settings
  - Temporal features (hour, day-of-week, month) and weather features (temperature, humidity) are the most important input variables
  - Model generalizes well across seasons when trained on full-year data
- **Relevance:** Validates XGBoost as a sufficient standalone model for grid load prediction. Supports our choice of Optuna-based Bayesian optimization for hyperparameter tuning. Confirms that our planned feature set (temporal + weather + demand lags) covers the most important input dimensions.

---

## PUE and Cooling Efficiency

### 8. DeepMind -- Reducing Google Data Centre Cooling Bill by 40%

- **Citation:** DeepMind. "DeepMind AI Reduces Google Data Centre Cooling Bill by 40%."
- **URL:** https://deepmind.google/discover/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-by-40/
- **Key Findings:**
  - Neural network ensemble trained on historical sensor data from Google data centers
  - Achieved 40% reduction in cooling energy consumption
  - Reduced overall PUE by approximately 15%
  - System operates in real-time, adjusting cooling parameters every 5 minutes
  - Demonstrated that ML can optimize data center operations beyond human operator performance
- **Relevance:** Gold standard for ML-driven cooling optimization. Our approach is simpler (regression on climate variables rather than real-time control) but more reproducible and applicable to facility siting decisions before construction. DeepMind optimizes existing facilities; we evaluate proposed locations.

### 9. Lei et al. 2024 -- PUE Sensitivity Analysis across Climate Zones

- **Citation:** Lei, N., et al. "Data Center PUE with Economizer Types across Climate Zones." MDPI Buildings, 14(1), 299, 2024.
- **URL:** https://www.mdpi.com/2075-5309/14/1/299
- **Key Findings:**
  - Sobol sensitivity analysis identifies dry-bulb temperature and wet-bulb temperature as the highest-influence parameters for PUE
  - Economizer type (air-side vs. water-side vs. none) is the second most important factor
  - Climate zone classification (ASHRAE) captures 70-80% of PUE variation
  - PUE ranges from 1.08 (cold, dry climates with air-side economizer) to 1.55 (hot, humid climates without economizer)
  - Interaction effects between temperature and humidity are significant
- **Relevance:** Directly validates our feature selection for the PUE regression model. Confirms that a climate-driven model using TMY weather data can capture the dominant sources of PUE variation. The Sobol sensitivity results inform which features to prioritize.

### 10. NREL/DOE -- Psychrometric Bin Analysis for Data Center Cooling

- **Citation:** NREL/DOE. "Psychrometric Bin Analysis for Alternative Cooling Strategies in Data Centers."
- **URL:** https://www1.eere.energy.gov/buildings/publications/pdfs/rsf/psychrometric_bin_analysis_alternative_cooling_strategies_data_centers.pdf
- **Key Findings:**
  - Most of Canada qualifies for 5,500+ free-cooling hours per year (out of 8,760 total)
  - Air-side economization alone can provide 80% of annual cooling energy in cold climates
  - Psychrometric analysis shows that Canadian cities spend the majority of hours below the ASHRAE recommended supply air temperature threshold
  - Even Toronto (warmest major Canadian DC market) has 4,000+ free-cooling hours
  - Evaporative cooling extends the free-cooling range further in dry climates (Calgary, Saskatoon)
- **Relevance:** Quantifies Canada's inherent climate advantage for data center siting. Provides the empirical basis for our PUE model's assumption that Canadian facilities can achieve lower PUE than comparable US facilities. Supports the argument that smart siting within Canada can yield additional efficiency gains.

---

## Energy Reports

### 11. LBNL 2024 -- United States Data Center Energy Usage Report

- **Citation:** Lawrence Berkeley National Laboratory. "United States Data Center Energy Usage Report." December 2024.
- **URL:** https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf
- **Key Findings:**
  - US data center energy consumption: 58 TWh (2014) to 176 TWh (2023)
  - Projected range: 325-580 TWh by 2028
  - PUE has plateaued at approximately 1.55 industry-wide (hyperscalers achieve 1.1-1.2)
  - WUE methodology and simulation framework for estimating facility-level water consumption
  - Detailed breakdown of energy use by server type, cooling technology, and facility tier
- **Relevance:** Gold standard reference for energy and water efficiency parameters. The PUE/WUE simulation methodology directly informs our semi-synthetic model design. Published PUE distributions by facility type and climate zone serve as calibration targets.

### 12. IEA 2025 -- Energy and AI / Electricity 2025

- **Citation:** International Energy Agency. "Energy and AI." January 2025.
- **URL:** https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
- **Key Findings:**
  - Global data center electricity consumption: approximately 415 TWh in 2024
  - Projected to reach 945 TWh by 2030 (exceeding Japan's total electricity consumption)
  - AI-accelerated servers growing at approximately 30% per year
  - Data centers represent approximately 1.5% of global electricity demand, projected to reach 3.4% by 2030
  - Efficiency gains (PUE improvement, server consolidation) being overwhelmed by demand growth
- **Relevance:** Frames the global context and urgency. The 945 TWh projection establishes that the data center energy problem is not hypothetical but actively unfolding at global scale. Canada's share of this growth motivates the need for a Canadian-specific assessment tool.

---

## Water

### 13. EESI -- Data Centers and Water Consumption

- **Citation:** Environmental and Energy Study Institute. "Data Centers and Water Consumption."
- **URL:** https://www.eesi.org/articles/view/data-centers-and-water-consumption
- **Key Findings:**
  - Comprehensive overview of data center water consumption mechanisms
  - Evaporative cooling accounts for the majority of facility water use
  - Average WUE ranges from 0.5 L/kWh (air-cooled) to 2.5 L/kWh (evaporative cooling)
  - Water consumption is growing faster than energy consumption due to increasing heat density in AI hardware
  - Municipal water systems were not designed for single consumers at data center scale
- **Relevance:** Provides the contextual framing for our water intensity sub-model. Establishes WUE benchmarks that serve as calibration points for our estimation methodology.

### 14. Microsoft 2024 -- Zero-Water Datacenter Design

- **Citation:** Microsoft. "Sustainable by Design: Next-Generation Datacenters Consume Zero Water for Cooling." December 2024.
- **URL:** https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/
- **Key Findings:**
  - Chip-level liquid cooling eliminates the need for evaporative water use entirely
  - Next-generation Microsoft facilities designed to consume zero water for cooling
  - Approach uses direct-to-chip liquid cooling with dry heat rejection (no cooling tower)
  - Applicable to high-density AI racks (50+ kW/rack) where air cooling is insufficient
  - Represents a fundamental shift from water-intensive to water-free cooling architectures
- **Relevance:** Represents the future direction of data center cooling technology. Our water intensity model should account for the possibility that new facilities may adopt zero-water cooling, which would dramatically change the water dimension of the SIS. This technology trajectory informs our scenario modeling and forward-looking analysis.

---

## Key Sources Summary

| # | Authors / Organization | Year | Primary Contribution to This Project |
|---|---|---|---|
| 1 | **Dandres et al.** | **2016** | **Most directly relevant prior work: marginal intensity, cross-border effects, gaps we fill** |
| 2 | Xiao & You | 2025 | Foundational siting framework, US gap |
| 3 | Patterns | 2025 | Carbon/water metric methodology |
| 4 | Frontiers | 2024 | National carbon forecasting methodology |
| 4 | Maji et al. (CarbonCast) | 2022 | Carbon intensity forecasting architecture |
| 5 | Jones | 2025 | Ensemble emission prediction validation |
| 6 | Jang et al. | 2024 | Grid load forecasting benchmarks |
| 7 | Sci. Reports | 2022 | XGBoost load forecasting validation |
| 8 | DeepMind | -- | Cooling optimization gold standard |
| 9 | Lei et al. | 2024 | PUE sensitivity analysis and feature selection |
| 10 | NREL/DOE | -- | Canada free-cooling quantification |
| 11 | LBNL | 2024 | Energy/water efficiency parameters |
| 12 | IEA | 2025 | Global demand context |
| 13 | EESI | -- | Water consumption overview |
| 14 | Microsoft | 2024 | Zero-water cooling technology |
