# HR Analytics: Workforce Insights & Attrition Trends

## Overview

This project simulates a real-world HR analytics scenario using synthetically generated employee data to demonstrate professional analytics workflows, dashboard design, and business insight generation.

The objective is to diagnose workforce structure, compensation dynamics, and attrition patterns, and to evaluate whether employee churn can be predicted using available HR data.

The project is intentionally split into two parts:

- Business-focused workforce analytics (Part A)
- CRISP-DM–based attrition modeling (Part B)

This mirrors real analytics practice: **strategic insight first, predictive modeling second.**

An interactive Tableau dashboard complements the Python analysis for executive exploration.

> **Note:** The dataset used in this project is synthetic and generated using Python. Insights are illustrative and intended to demonstrate analytical methodology rather than reflect real organizational data.

---

## Project Structure

hr-analytics/   
│   
├ notebooks/   
│   ├ hr_storytelling_final.ipynb   
│   └ hr_crispdm_final_report.ipynb   
│   
├ data/   
│   └ HumanResources_India.csv   
│   
├ scripts/   
│   └ generate_hr_data.py   
│   
├ artifacts/   
├ README.md     
└ requirements.txt   

---

## 🧬 Data Generation

The dataset used in this project is synthetically generated using Python.

Script: scripts/generate_hr_data.py

The generator simulates realistic HR attributes including:

- demographics
- hiring timelines
- department distributions
- job titles
- salary ranges
- education levels
- performance ratings
- termination events

This ensures full reproducibility and transparency of assumptions.

---

## 📘 Data Dictionary

| Column | Description |
|--------|------------|
| employee_id | Unique employee identifier |
| first_name | Employee first name |
| last_name | Employee last name |
| gender | Male / Female |
| city | City of employment |
| state | State of employment |
| hiredate | Employee hire date |
| termdate | Termination date (null if active) |
| department | Department assignment |
| job_title | Role title |
| education_level | Highest education attained |
| performance_rating | Most recent performance evaluation |
| overtime | Indicates overtime status |
| salary | Annual salary |
| birthdate | Date of birth |

### Engineered Fields (created during analysis)

| Column | Description |
|--------|------------|
| age | Calculated from birthdate |
| tenure_years | Years since hire |
| is_terminated | Boolean attrition flag |
| hire_year | Year hired |
| tenure_band | Binned tenure category |
| salary_to_dept_median | Salary normalized by department median |

---

## Part A — Workforce Analytics (Business Storytelling)

**File:** `notebooks/hr_analytics.ipynb`

This notebook focuses on descriptive analytics and strategic workforce insights.

Key analyses include:

- Workforce snapshot and attrition overview
- Hiring and termination trends
- Compensation architecture using median and interquartile ranges
- Salary compression across support functions
- Age vs salary relationship
- Tenure-based attrition patterns
- Executive insights and strategic recommendations

### Key Findings

- The organization operates across three compensation tiers (IT highest, Sales/Finance middle, support functions lowest)
- Support roles experience salary compression with limited upward mobility
- Age explains only ~2% of salary variance — compensation is primarily role-driven
- Attrition occurs across multiple career stages rather than only early tenure
- Limited internal mobility presents long-term retention risk

This notebook answers:

> *What is happening in the workforce, why it matters, and what leadership should do.*

No machine learning is used in Part A — this is purely business analytics.

---

## Part B — Attrition Modeling (CRISP-DM)

**File:** `notebooks/CRISPDM_report.ipynb`

This notebook implements a full CRISP-DM modeling pipeline:

1. Business Understanding  
2. Data Understanding  
3. Feature Engineering  
4. Feature–Attrition Association  
5. Baseline Logistic Regression  
6. Random Forest + Probability Calibration  
7. Risk Scoring (demonstration only)  
8. Executive Modeling Report  

### Modeling Results

- All static HR features show near-zero correlation with attrition
- Logistic regression achieves recall only by generating excessive false positives
- Random Forest collapses to majority-class prediction
- ROC AUC < 0.5 confirms absence of predictive signal
- Risk scores are illustrative only and not operationally usable

### Core Conclusion

Attrition cannot be reliably predicted using demographic and snapshot HR attributes alone.

This is a **data limitation, not a modeling limitation.**

The modeling notebook demonstrates responsible analytics by identifying missing behavioral drivers rather than forcing weak models into production.

---

## 📊 Dashboard

Interactive Tableau dashboard:

https://public.tableau.com/app/profile/kaustubh.pawar22/viz/HRAnalytics_17447607351070/HRAnalytics

The dashboard is structured into:

### Overview
- Total hired, active, and terminated employees  
- Hiring and termination trends by year  
- Workforce distribution by department and job title  
- HQ vs branch comparison  
- Geographic employee distribution  

### Demographics
- Gender ratio  
- Age group distribution  
- Education levels  
- Performance ratings by educational background  

### Income Analysis
- Salary comparison across education levels and gender  
- Age vs salary correlations by department  

### Employee Records
- Filterable employee-level table for detailed analysis  

---

## ⚠️ Important Notes

- Dataset is synthetically generated for portfolio purposes.
- Results are directional and intended to demonstrate analytical methodology.
- Risk scores should not be operationalized.
- Predictive retention requires behavioral data such as performance trends, promotions, engagement metrics, and manager changes.

---

## 🛠️ Requirements

Python 3.10+

Main libraries:

- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  
- scipy  

Both notebooks expect `HumanResources_India.csv` in the `/data` directory.

---

## 🎯 Skills Demonstrated

- Business analytics & executive storytelling  
- Compensation architecture analysis (median + IQR)  
- Workforce diagnostics  
- CRISP-DM methodology  
- Feature engineering  
- Class imbalance handling  
- Probability calibration  
- Ethical model evaluation  
- Strategic recommendation development  

---

## Author

Kaustubh Pawar  
Portfolio: https://kaustubhpawar.com  

