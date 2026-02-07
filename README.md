# HR Analytics Dashboard — Workforce Insights & Attrition Trends

## Overview

This project simulates a real-world HR analytics scenario using synthetically generated employee data to demonstrate end-to-end analytics workflows, dashboard design, and business insight generation.

The objective is to build a comprehensive HR dashboard that provides both executive-level summaries and detailed employee records to support data-driven workforce planning.

An interactive Tableau dashboard is used to explore hiring trends, workforce demographics, performance patterns, and compensation metrics.

> **Note:** The dataset used in this project is synthetic and generated using Python. Insights are illustrative and intended to demonstrate analytical techniques rather than reflect real organizational data.

---

## Business Problem

HR teams often lack centralized visibility into workforce composition, attrition trends, and salary distribution. Decision-makers require intuitive dashboards that combine high-level KPIs with granular employee-level data.

This project addresses the following needs:

- Monitor hiring and termination trends over time  
- Understand workforce demographics and education levels  
- Analyze salary patterns across departments, age groups, and gender  
- Enable drill-down analysis through detailed employee records  

---

## Dataset

Synthetic HR dataset containing **8,950 employee records** spanning 2015–2024.

### Key attributes include:

- Employee ID  
- Gender, age, education level  
- Department and job title  
- Performance rating  
- Salary and adjusted salary  
- Hire and termination dates  
- State and city  

The dataset was generated using Python with controlled probability distributions to simulate realistic corporate workforce patterns.

---

## Dashboard

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

## Tools Used

- Python (synthetic data generation and preprocessing)  
- Tableau (interactive dashboard development)  
- Excel (data validation)  

---

## Key Insights (Simulated Scenario)

- Attrition appears highest among early-tenure employees, highlighting potential onboarding and engagement gaps  
- Salary varies significantly across departments and education levels  
- Higher education levels show correlation with stronger performance ratings  
- Gender-based salary differences emerge in specific roles and education bands  
- Compensation trends differ by age group across departments  

---

## Business Recommendations (Illustrative)

- Implement targeted retention programs for early-career employees  
- Monitor department-level attrition metrics as early risk indicators  
- Standardize compensation bands to reduce discrepancies  
- Leverage performance insights to guide learning and development initiatives  

---

## Data Generation Methodology

Employee records were generated using Python with structured logic:

- Gender distribution: 54% Male / 46% Female  
- Department and job titles assigned via weighted probabilities  
- Education levels mapped to job roles  
- Salaries generated based on department-specific ranges  
- Performance ratings assigned probabilistically  
- Termination applied to 11.2% of employees with time-based constraints  
- Adjusted salary calculated using age, gender, and education multipliers  

This controlled approach enables realistic HR analytics scenarios while preserving data privacy.

---

## How to Run

1. Clone the repository  
2. Install Python dependencies  
3. Run the data generation script to create the dataset  
4. Open the Tableau workbook or dashboard link  

---

## Author

**Kaustubh Pawar**  
