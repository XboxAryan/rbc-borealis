# Sustainability Frameworks and Standards

---

## Overview

This document catalogs the sustainability frameworks, industry standards, and multi-criteria decision analysis methods referenced in the Societal Impact Score design. Each framework is documented with its standard identifier, key formulas, and specific relevance to this project.

---

## Green Software Foundation -- Software Carbon Intensity (SCI)

- **Standard:** ISO/IEC 21031:2024
- **Specification:** https://sci.greensoftware.foundation/
- **GitHub:** https://github.com/Green-Software-Foundation/sci

### Formula

```
SCI = (E x I + M) / R
```

| Variable | Definition | Units |
|---|---|---|
| E | Energy consumed by the software system | kWh |
| I | Region-specific marginal carbon intensity of the electricity grid | gCO2/kWh |
| M | Embodied emissions of the hardware (manufacturing, transport, end-of-life) | gCO2 |
| R | Functional unit of the software system | per user, per API call, per ML training run |

### Key Design Principles

- **No offsets:** SCI explicitly does not incorporate renewable energy certificates (RECs) or carbon offsets. The metric reflects actual emissions at the point of consumption, not net-of-offset accounting.
- **Marginal, not average:** The standard recommends using marginal carbon intensity (the emission factor of the generation that would actually be dispatched to serve incremental load) rather than annual grid averages.
- **Improvement-oriented:** SCI is designed to be compared across time or across configurations. A lower score indicates genuine emission reductions, not accounting tricks.

### SCI Sensitivity Dimensions

The SCI standard identifies three levers for reducing the score:

1. **Carbon awareness:** Shifting workloads to times and places with lower grid carbon intensity
2. **Energy efficiency:** Reducing the total energy consumed per functional unit
3. **Hardware efficiency:** Extending hardware lifespan, using efficient hardware, reducing embodied emissions

### Relevance to This Project

Our Societal Impact Score extends the SCI concept from software-level assessment to facility-siting-level assessment. Where SCI evaluates "how carbon-intensive is this software running on this infrastructure?", our SIS evaluates "how carbon-intensive would any software be if we build a data center at this location?" The SCI framework validates the use of marginal carbon intensity and the exclusion of offset accounting in our methodology.

---

## Open Compute Project (OCP) Sustainability Metrics

- **Organization:** Open Compute Project Foundation
- **Document:** "Sustainability Metrics" (Revision 3)
- **URL:** https://www.opencompute.org/documents/dcf-sustainability-metrics-final-r3-docx-pdf

### Metric Categories

The OCP defines 23 sustainability metrics across five environmental categories:

| Category | Key Metrics | Count |
|---|---|---|
| Energy | PUE, ERE, DCIE, renewable energy fraction | 6 |
| Carbon | CUE, Scope 1/2/3 GHG emissions | 4 |
| Water | WUE, water source type, recycled water fraction | 4 |
| Waste | Waste diversion rate, e-waste recycling rate | 5 |
| Land | Land use efficiency, ecosystem impact | 4 |

### Metrics Used in This Project

| Metric | Definition | Formula | Target Range |
|---|---|---|---|
| PUE | Power Usage Effectiveness | Total facility energy / IT equipment energy | 1.0 (ideal) to 2.0+ (poor) |
| CUE | Carbon Usage Effectiveness | Total CO2 emissions / IT equipment energy | 0 (zero carbon) to 1.0+ |
| WUE | Water Usage Effectiveness | Total water usage / IT equipment energy | 0 (zero water) to 2.5+ L/kWh |

### Aspirational Goals

The OCP sets long-term aspirational targets for the industry:

- Net zero Scope 1, 2, and 3 greenhouse gas emissions
- Zero waste to landfill
- Net positive water impact (returning more clean water than consumed)
- 100% renewable energy for operations

### Relevance to This Project

The OCP metrics provide the industry-standard definitions for the efficiency parameters used in our sub-models. PUE, CUE, and WUE are the three core metrics that our model estimates for each candidate site. Adopting OCP definitions ensures our outputs are directly comparable to industry reporting.

---

## DOE Best Practices Guide for Data Center Design (2024)

- **Organization:** US Department of Energy
- **URL:** https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design_0.pdf

### Metric Definitions

| Metric | Formula | Interpretation |
|---|---|---|
| PUE | Total facility energy / IT equipment energy | Values closer to 1.0 indicate higher efficiency |
| ERE | (Total energy - Reused energy) / IT equipment energy | Accounts for waste heat recovery; ERE < PUE when heat is reused |
| WUE | Annual water usage / IT equipment energy | Litres per kWh; lower is better |
| CUE | Total CO2 emissions / IT equipment energy | kgCO2/kWh; lower is better |

### ERE: Energy Reuse Effectiveness

ERE is a refinement of PUE that credits facilities for capturing and reusing waste heat. For example, the QScale Q01 facility in Levis, Quebec redirects approximately 100 MW of waste heat to household heating. Under ERE accounting, this reduces the effective energy overhead of the facility.

```
ERE = (Total_energy - Reused_energy) / IT_energy
```

ERE is always less than or equal to PUE. A facility with significant heat reuse may have a PUE of 1.3 but an ERE of 1.05.

### Relevance to This Project

The DOE guide provides authoritative metric definitions that ground our model outputs in established terminology. The ERE concept is relevant as a stretch goal -- accounting for waste heat reuse in the SIS would reward facilities like QScale that contribute positively to their communities.

---

## Multi-Criteria Decision Analysis (MCDA)

- **Overview:** https://www.sciencedirect.com/topics/social-sciences/multiple-criteria-decision-analysis
- **Key Reference:** Wieckowski et al. 2023, https://journals.sagepub.com/doi/10.3233/KES-230487
- **Sustainability Scoring:** https://www.sciencedirect.com/science/article/pii/S1470160X14002647

### Methods Comparison

| Method | Full Name | Approach | Complexity | Transparency |
|---|---|---|---|---|
| WLC | Weighted Linear Combination | Weighted sum of normalized scores | Low | High |
| AHP | Analytic Hierarchy Process | Pairwise comparisons to derive weights | Medium | Medium |
| TOPSIS | Technique for Order Preference | Distance from ideal/anti-ideal solutions | Medium | Medium |
| ELECTRE | Elimination and Choice Translating Reality | Outranking with concordance/discordance | High | Low |
| PROMETHEE | Preference Ranking Organization Method | Preference flows between alternatives | High | Low |

### Our Approach

**Primary method: Weighted Linear Combination (WLC)**

```
SIS = w1 * GridStress + w2 * CarbonIntensity + w3 * PUE + w4 * WaterIntensity
```

Where w1 + w2 + w3 + w4 = 1 and each sub-score is normalized to a 0-1 scale.

**Rationale for WLC:**
- Most transparent and interpretable method
- Directly communicates how each dimension contributes to the final score
- Easy for policymakers and non-technical stakeholders to understand
- Sensitivity analysis with alternative weights is straightforward
- Sufficient for a first-generation tool; more sophisticated methods can be applied later

**Alternative weights via AHP (stretch goal):**
- AHP derives weights from pairwise comparisons by domain experts
- Example: "Is carbon intensity more or less important than water stress for your region?"
- Produces mathematically consistent weights with a consistency ratio check
- Requires stakeholder engagement beyond the team, making it a stretch goal

### Relevance to This Project

MCDA provides the theoretical foundation for combining our four sub-model outputs into a single composite score. The choice of WLC with equal default weights is a deliberate simplification that maximizes transparency and reproducibility. Sensitivity analysis across weight configurations demonstrates that the tool's core insights (e.g., Quebec dominates Alberta on carbon) are robust to reasonable alternative weighting schemes.

---

## Uptime Institute Tier Classification

- **Organization:** Uptime Institute
- **Standard:** Tier Standard: Topology (Edition 8)

### Tier Definitions

| Tier | Name | Uptime SLA | Annual Downtime | Key Characteristics |
|---|---|---|---|---|
| I | Basic | 99.671% | 28.8 hours | Single path for power and cooling, no redundancy |
| II | Redundant Components | 99.741% | 22.7 hours | Redundant capacity components (N+1) |
| III | Concurrently Maintainable | 99.982% | 1.6 hours | Multiple power and cooling paths, one active |
| IV | Fault Tolerant | 99.995% | 0.4 hours | Multiple active paths, fault tolerant |

### Tier and PUE Relationship

Higher tiers require more redundant infrastructure (backup generators, redundant cooling loops, uninterruptible power supplies), which increases facility overhead energy and typically raises PUE.

| Tier | Typical PUE Range | Explanation |
|---|---|---|
| I | 1.3 - 1.8 | Minimal overhead, but also minimal cooling optimization |
| II | 1.3 - 1.6 | Redundant components add some overhead |
| III | 1.2 - 1.5 | Better-engineered facilities offset redundancy overhead |
| IV | 1.2 - 1.4 | Highest engineering standards, but maximum redundancy |

Modern hyperscale facilities (Google, Microsoft, AWS) often operate at Tier III-equivalent reliability with custom engineering that achieves PUE 1.1-1.2, below the typical range for their tier.

### Relevance to This Project

Tier classification affects PUE assumptions in our model. When estimating PUE for a proposed facility, the assumed tier level determines the baseline overhead. For the MVP, we assume Tier III (the most common for new commercial data centers) and note the sensitivity of PUE estimates to tier choice.

---

## ISO 14064 and GHG Protocol

- **ISO 14064:** International standard for quantification and reporting of greenhouse gas emissions
- **GHG Protocol:** https://ghgprotocol.org/

### Scope Definitions

| Scope | What It Covers | Data Center Example |
|---|---|---|
| Scope 1 | Direct emissions from owned sources | Backup diesel generators |
| Scope 2 | Indirect emissions from purchased electricity | Grid electricity for IT and cooling |
| Scope 3 | All other indirect emissions | Embodied carbon in servers, construction, supply chain |

### Relevance to This Project

Our carbon intensity model focuses on Scope 2 emissions (purchased electricity), which represent 85-95% of a data center's operational carbon footprint. Scope 1 (backup generators) is small for modern facilities. Scope 3 (embodied carbon) is important but requires lifecycle assessment data that is outside the MVP scope.

---

## Key References

- Green Software Foundation, Software Carbon Intensity Specification: https://sci.greensoftware.foundation/
- Open Compute Project, Sustainability Metrics (Rev 3): https://www.opencompute.org/documents/dcf-sustainability-metrics-final-r3-docx-pdf
- DOE, Best Practice Guide for Data Center Design, 2024
- Wieckowski et al. 2023, "Multi-Criteria Decision Analysis Methods," Knowledge Engineering and Software
- Uptime Institute, Tier Standard: Topology, Edition 8
- GHG Protocol: https://ghgprotocol.org/
