# Data Center Location and Capacity Data

This document catalogs the available sources for identifying data center locations, operators, and capacity across Canada. Accurate facility-level data is essential for modeling aggregate energy and water demand, yet remains one of the most difficult data categories to obtain at scale.

---

## 1. Commercial Data Center Directories (Free Tier)

Several commercial platforms offer browsable directories of data center facilities with limited free access.

| Source | URL | Listed Facilities | Data Fields (Free) | Access |
|---|---|---|---|---|
| DataCenterMap.com | https://www.datacentermap.com/canada/ | 279 facilities / 231 operators | Location, operator, city | Free browse |
| DataCenters.com | https://www.datacenters.com/locations/canada | ~337 facilities | Location, operator, basic specs | Free browse |
| Baxtel | https://baxtel.com/data-center/canada | Listed (count varies) | Location, operator | Free browse |

### City Breakdown (DataCenterMap.com)

| City | Facilities | Operators |
|---|---|---|
| Toronto | 72 | 42 |
| Montreal | 54 | 18 |
| Vancouver | 28 | 20 |
| Edmonton | 15 | 7 |
| Calgary | 12 | 8 |
| Ottawa | 10 | 7 |
| Winnipeg | 8 | 5 |

### Limitations of Free Tier

- No MW capacity data (critical gap)
- No PUE, WUE, or cooling technology information
- No power source or grid connection details
- Listings may be incomplete or outdated
- Duplicate entries across platforms are common

### Paid Market Research Reports

Comprehensive data center market reports with capacity, pricing, and pipeline data are available from research firms including Arizton, Research and Markets, JLL, CBRE, and Cushman & Wakefield. These reports typically cost $2,500 or more and may have licensing restrictions on derivative use.

---

## 2. CER Market Snapshot (October 2024)

- **Organization:** Canada Energy Regulator
- **URL:** https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/market-snapshots/2024/market-snapshot-energy-demand-from-data-centers-is-steadily-increasing-and-ai-development-is-a-significant-factor.html

### Description

The CER published an interactive market snapshot in October 2024 that includes a map of 239 data centers by province, along with analysis of energy demand growth driven by AI workloads.

### Key Data Points

- Interactive map showing 239 data centers across Canada
- Ontario has the highest facility count, followed by Quebec
- Discussion of projected energy demand growth from AI and hyperscale buildout
- Provincial distribution of facilities

### Limitations

- Point-in-time snapshot (October 2024)
- No individual facility MW capacity
- No regular update cadence announced

### Relevance

Medium-High. Provides an official government-sourced baseline count and geographic distribution. The accompanying analysis of AI-driven demand growth provides useful context for projections.

---

## 3. Market Research Summaries (News and Press)

Aggregated from industry press, news articles, and conference presentations (2024--2025):

### National Overview

| Metric | Value | Source |
|---|---|---|
| Toronto existing capacity | >370 MW (~40% of national total) | Industry reporting |
| Calgary share of planned future capacity | >25% | Industry reporting |
| Existing colocation facilities tracked | 116 | Market aggregators |
| Upcoming/planned facilities | 19+ | Market aggregators |

### Major Operators in Canada

| Operator | Headquarters | Canadian Presence |
|---|---|---|
| eStruxture Data Centers | Montreal, QC | Montreal, Vancouver, Calgary |
| Cologix | Denver, CO | Toronto, Montreal, Vancouver |
| Vantage Data Centers | Denver, CO | Montreal, Quebec City |
| Equinix | Redwood City, CA | Toronto |
| QTS (Blackstone) | Ashburn, VA | Toronto (planned) |
| CBRE / Digital Realty | Various | Multiple Canadian markets |

### Regional Notes

- **Toronto:** Dominant market. Constrained by power availability in some zones. New builds shifting to Vaughan, Markham, and surrounding 905 region.
- **Montreal:** Second-largest market. Attractive due to low electricity costs and near-zero carbon grid. QScale building hyperscale campus in Levis.
- **Calgary:** Fastest-growing market by planned capacity. Driven by proximity to oil/gas sector compute needs and available land/power.
- **Vancouver:** Mature market with 28+ facilities. Growth constrained by high real estate costs and limited available power.

---

## 4. OpenStreetMap

- **Tag:** `telecom=data_center`
- **Visualization:** Open Infrastructure Map (https://openinframap.org/)

### Overpass Turbo Query for Canada

```
[out:json][timeout:60];
(
  nwr["telecom"="data_center"](41.7,-141.0,83.1,-52.6);
);
out body;
>;
out skel qt;
```

This query retrieves all nodes, ways, and relations tagged as data centers within the bounding box covering Canada.

### Limitations

- Crowdsourced data: completeness and accuracy vary significantly by region
- Better coverage for large, well-known facilities; poor coverage for enterprise or private DCs
- No standardized attributes for capacity, power, or cooling
- Tagging conventions are inconsistent (some facilities use `building=data_centre`, `man_made=data_center`, or other variants)

### Relevance

Low-Medium. Useful as a supplementary geospatial check to validate facility locations from other sources. Not reliable as a primary data source for comprehensive inventories.

---

## 5. Provincial Utility Connection Records

Some provincial utilities and system operators maintain records of large industrial connections that can serve as indirect indicators of data center capacity.

### IESO (Ontario)

- Large Load Connection Assessment reports for projects >5 MW
- Publicly posted connection assessments may indicate data center projects
- System Impact Assessments for new connections

### AESO (Alberta)

- Connection queue and project listings
- New generation and load project pipeline

### Limitations

- Not all connections are identifiable as data centers (may be listed under corporate names without facility type)
- Connection applications do not always result in built facilities
- Access may require formal information requests

### Relevance

Low-Medium. Useful for identifying planned large-scale facilities not yet in commercial directories, but requires manual cross-referencing to identify data center projects.

---

## Data Quality Assessment

| Source | Completeness | Accuracy | Timeliness | Capacity Data | Geolocation |
|---|---|---|---|---|---|
| DataCenterMap.com | Medium | Medium | Updated regularly | No (free) | Yes (city) |
| DataCenters.com | Medium-High | Medium | Updated regularly | Partial (free) | Yes (city) |
| CER Snapshot | Medium | High | Point-in-time | No | Yes (province) |
| Industry press | Low | Variable | Current | Partial | Variable |
| OpenStreetMap | Low | Variable | Crowdsourced | No | Yes (coordinates) |
| Utility records | Low | High | Delayed | Partial (MW) | No |

---

## Recommended Approach

Given the fragmented nature of Canadian data center location data, the recommended approach is:

1. **Start with commercial directories** (DataCenterMap.com, DataCenters.com) to establish a baseline facility inventory
2. **Cross-reference with CER snapshot** to validate provincial counts
3. **Supplement with OSM** for geospatial coordinates of major facilities
4. **Monitor industry press** for new announcements and planned capacity additions
5. **Use utility connection records** where available to estimate MW capacity for large facilities
6. **Deduplicate aggressively** -- facilities appear under different names across sources (e.g., operator name vs. building name vs. address)

The absence of a single authoritative Canadian data center registry is a significant data gap. Any composite dataset built from these sources should include confidence levels and provenance tracking for each facility record.
