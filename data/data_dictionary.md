# Data Dictionary – Synthetic Support Case Dataset

## Overview
This dataset contains **synthetic global technical support case data** designed to mimic real-world support operations across APAC, EMEA, and the Americas.  
The data is anonymized and generated for **business analysis and operational optimization demonstrations**.

**Total Records**: 1,200 support cases  
**Time Period**: Rolling 12 months  
**Data Type**: Synthetic (non-production)

---

## Field Descriptions

| Field Name | Data Type | Description | Example Values |
|----------|----------|------------|----------------|
| `Dat` | Integer | Unique support case identifier | 1880123 |
| `Site Name` | String | Customer site or location name | CGV Shanghai Fudi, AMC Empire 25 |
| `Status` | String | Current lifecycle status of the case | Solving, Resolved, Closed |
| `Priority` | String | Business priority assigned to the case | Critical, Major, Minor, Informational |
| `Severity` | String | Technical severity classification | High (Critical), Medium (Major) |
| `Screen Status` | String | Operational screen status at time of report | UP, DOWN |
| `State` | String | Geographic state or country | CA, France, Japan |
| `Case status` | String | Operational case status (mirrors Status) | Solving, Closed |
| `Type` | String | Channel through which case was raised | Email Request, Web Support |
| `Category` | String | Equipment or system category | Projector, Audio, Network |
| `Reported Issue` | String | Description of the reported technical issue | NO IMAGE, Network Connectivity Issue |
| `Resolution` | String | Resolution action taken | Replaced Component, Software Update Applied |
| `Queue Name` | String | Support queue handling the case | EMEA Issues, APAC Dispatched |
| `Region` | String | Geographic support region | APAC, EMEA, Americas |
| `Market` | String | Market or customer grouping | Market-UK-CDS, Market-NY |
| `Creation Time` | String (datetime) | Case creation timestamp | 3/15/2024 14:30 |
| `Last Update Time` | String (datetime) | Last update or resolution timestamp | 3/18/2024 09:15 |
| `Resolution time` | Integer | Case resolution duration (days) | 2, 14, 45 |

---

## Priority Definitions

- **Critical**: Service-affecting issues requiring immediate attention
- **Major**: Significant operational impact
- **Minor**: Low-impact issues with available workarounds
- **Informational**: Requests or non-disruptive issues

---

## Severity Definitions

- **High**: Complete service outage or critical failure
- **Medium**: Partial functionality degradation
- **Low**: Minor operational inconvenience

---

## Known Data Characteristics

- **Outliers**: ~5% of cases have significantly longer resolution times to simulate complex investigations
- **Misclassifications**: Intentional mismatches between priority and severity reflect real operational inconsistencies
- **Regional Patterns**:
  - APAC generally resolves cases faster
  - EMEA shows higher variability in resolution time
- **Operational Realism**: Queue routing and resolution actions vary by region

---

## Data Quality Notes

This dataset is **synthetically generated** for portfolio and demonstration purposes only.  
It does not contain real customer or operational data.

**Last Updated**: December 2025

