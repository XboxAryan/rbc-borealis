# Societal Impact Modeling for Data Center Siting

## What Is the Problem?

- AI data centers are rapidly expanding across Canada.  
- They consume large amounts of electricity and water.  
- Their environmental and societal impact varies significantly by region depending on:
  - Grid carbon intensity  
  - Grid reserve margins and reliability  
  - Climate (cooling demand)  
  - Local water stress  
- Policymakers currently lack:
  - A transparent, data-driven tool to evaluate environmental and societal risk before siting  
  - An uncertainty-aware decision framework  
- Siting decisions are often driven by cost and infrastructure access rather than community vulnerability.

**Core policy question:**  
Given a proposed data center in Region R, is it environmentally and socially responsible to build there?

---

## Why ML Can Help

ML helps by:

- Learning nonlinear relationships between climate variables and cooling overhead  
- Predicting grid stress conditions from historical demand, reserve, and volatility patterns  
- Forecasting carbon intensity and identifying high-emission periods  
- Modeling water intensity as a function of climate and regional water stress  
- Quantifying prediction uncertainty in data-scarce regions  
- Simulating the marginal impact of adding data center load under different scenarios  

---

## What Data to Use

### 1️⃣ Grid Stress Model

**What It Predicts**  
Probability of high-stress grid state per region per hour.

**True Label**  
Binary label:
- 1 if grid in high-stress state  
- 0 otherwise  

High-stress defined by:
- Demand / available capacity above threshold  
- Low reserve margin  
- Price spike events  
- Emergency alerts  
- Carbon intensity spikes  

**Where Data Comes From**  
- Independent Electricity System Operator (Ontario)  
- Alberta Electric System Operator  
- Canada Energy Regulator  

These provide:
- Hourly demand  
- Generation mix  
- Reserve information  
- Market signals  

**Connection to Data Centers**  
Simulate adding additional MW load and recompute stress probability to measure incremental risk.

---

### 2️⃣ Carbon Intensity Model

**What It Predicts**  
Carbon intensity (gCO₂/kWh) per region per hour.

**True Label**  
Observed carbon intensity values.

**Where Data Comes From**  
- Electricity Maps  
- Statistics Canada  

**Connection to Data Centers**  
CO₂ emissions = Total energy consumption × Carbon intensity.  
Forecasting volatility identifies high-emission operating windows.

---

### 3️⃣ Cooling / PUE Regression

**What It Predicts**  
Cooling overhead multiplier (PUE).

**True Label**  
Benchmark PUE ranges derived from industry and government studies.

Sources:
- U.S. Department of Energy  

Climate features:
- Environment and Climate Change Canada  

**Connection to Data Centers**  
Total energy = IT energy × Predicted PUE.

---

### 4️⃣ Water Intensity Model

**What It Predicts**  
Cooling-related water intensity proxy (liters per kWh).

**True Label**  
Derived proxy using:
- Sector-level water usage  
- Water stress indices  
- Climate-based cooling demand  

Data sources:
- Statistics Canada  
- World Resources Institute  
- Environment and Climate Change Canada  

**Connection to Data Centers**  
Water usage = Total energy × Predicted water intensity.  
Adjusted using regional water stress multiplier.

---

### 5️⃣ Data Center Location Layer

Used for:
- Regional mapping  
- Scenario simulation  
- Geographical anchoring  

Sources:
- Canada Energy Regulator  
- OpenStreetMap  

---

## Final Combined Output

For each region:

Predict:
- Energy overhead  
- Carbon impact  
- Water impact  
- Grid stress probability  

Then compute:

**Societal Impact Score** =  
- Normalized carbon harm  
- Water harm × local water stress  
- Grid stress risk  
- Uncertainty penalty  

Lower score indicates a more responsible siting decision.
