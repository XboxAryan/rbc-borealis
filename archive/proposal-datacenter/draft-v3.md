# Societal Impact Modeling for AI Data Center Siting in Canada

## What is the problem?

AI data centers are expanding rapidly across Canada. The country currently hosts 10.3 GW of data center capacity, with an additional 9 GW in the development pipeline -- nearly doubling the installed base within the next few years. These facilities consume enormous amounts of electricity and water, and their environmental impact varies dramatically depending on where they are built.

A 100 MW data center in Alberta produces approximately 430,000 tonnes of CO2 per year under standard grid-average accounting, while the same facility in Quebec produces roughly 1,500 tonnes -- a 286-fold difference. But this comparison understates the real complexity. Research in the *Journal of Industrial Ecology* (Dandres et al. 2016) shows that the marginal electricity actually serving new data center loads in Canada is dominated by natural gas and coal, with a GHG intensity of 0.85-1.01 kg CO2-eq/kWh -- roughly 5x higher than the Canadian average. Worse, 60-70% of this marginal electricity comes from reduced exports to the United States, triggering compensating fossil fuel generation south of the border. Even siting in "clean" provinces has significant carbon consequences that standard accounting misses entirely.

Yet no publicly available tool exists to help policymakers evaluate these tradeoffs -- including the hidden marginal and cross-border effects -- before a siting decision is made. This gap is becoming urgent. In December 2025, Ontario passed Bill 40, the first Canadian law requiring ministerial approval for data center grid connections -- a signal that governments are actively seeking analytical frameworks for these decisions. Meanwhile, data center siting choices lock in 20 to 30 years of environmental consequences. The decisions being made today will shape Canada's carbon and water footprint for decades.

We propose building the first open-source Societal Impact Score for AI data center siting in Canada: a composite metric that evaluates carbon emissions, water consumption, grid stress, and cooling efficiency for any proposed location, with uncertainty quantification to support honest, evidence-based decision-making.

## Why does this matter to our team?

We rely on AI every day: ChatGPT to debug code at midnight, Copilot to scaffold assignments, and cloud GPUs to run models for our research and internships when our laptops max out. Over the past year, coursework in systems and sustainability, an internship touching grid reliability, and student research on ML models pushed us to ask a question we had mostly ignored: what does all this actually cost the grid and the climate? Digging into Dandres et al. and Ontario's new Bill 40, we realized that "clean" Canadian data centers can hide high marginal and cross-border emissions and that ministers are now expected to approve or deny grid connections without an open, quantitative tool to see those tradeoffs. As students spanning computer science, economics, and finance, we feel a responsibility to build that missing piece: an open Societal Impact Score that turns our own dependence on AI infrastructure into something that helps communities and policymakers make better long-term decisions.

## Why can machine learning help?

The environmental impact of a data center depends on complex, nonlinear interactions between grid conditions, climate, water availability, and facility design. Machine learning is well suited to capturing these relationships.

Our approach involves four sub-models, each addressing a distinct prediction task:

1. **Grid stress prediction:** A classification model trained on hourly electricity demand and reserve margin data to estimate whether adding a data center's load would push a provincial grid toward reliability limits.
2. **Carbon intensity forecasting:** A time-series model forecasting both average and marginal carbon intensity of electricity at a given location. Marginal intensity -- the carbon cost of the next unit of generation dispatched -- is typically 2-5x higher than the grid average in mixed-source provinces (Dandres et al. 2016), and is the methodologically appropriate metric for evaluating new loads.
3. **Cooling efficiency regression:** A regression model predicting Power Usage Effectiveness (PUE) -- the energy overhead from cooling -- based on local climate variables such as temperature and humidity.
4. **Water intensity estimation:** A physics-based model estimating water consumption from cooling systems, weighted by local water stress indices.

These four outputs are combined into a single Societal Impact Score using configurable weights. Monte Carlo simulation propagates uncertainty from each sub-model through the composite score, producing confidence intervals rather than misleading point estimates.

## What data do we plan to use?

We have identified three primary open datasets:

**1. Environment and Climate Change Canada (ECCC) -- Provincial Emission Factors**
Official government emission intensities (gCO2e/kWh) for every Canadian province and territory. These serve as the ground truth for our carbon intensity model.
Link: https://www.canada.ca/en/environment-climate-change/services/climate-change/pricing-pollution-how-it-will-work/output-based-pricing-system/federal-greenhouse-gas-offset-system/emission-factors-reference-values.html

**2. Independent Electricity System Operator (IESO) -- Ontario Hourly Generation Data**
Hourly generation by fuel type (nuclear, hydro, gas, wind, solar), system demand, and market pricing. Available as CSV downloads and via the open-source gridstatus Python library.
Link: https://www.ieso.ca/power-data/data-directory

**3. World Resources Institute (WRI) -- Aqueduct 4.0 Water Risk Atlas**
Sub-basin water stress indices covering all of Canada, including baseline water stress, seasonal variability, and drought risk. Licensed under Creative Commons Attribution 4.0.
Link: https://www.wri.org/applications/aqueduct/water-risk-atlas/

We also draw on the methodological findings of Dandres et al. (2016), published in the *Journal of Industrial Ecology*, which established that marginal generation in Canada is 85-100% fossil-fueled and identified cross-border electricity trade as a critical factor in consequential carbon accounting for new large loads.

## Does this project relate to coursework?

This project is purely extracurricular. It does not fulfill any coursework requirement. It is driven by our shared interest in applying machine learning to sustainability challenges.

## Willingness to pivot

Our team is fully open to pivoting to an alternative community project if selected and our mentor recommends a different direction. We are here to learn and to contribute, and we trust the mentorship process.
