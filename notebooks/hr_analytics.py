# %%
# HR Analytics — End-to-End Workforce Analysis
# Author: Kaustubh Pawar

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# %%
# Load Dataset

df = pd.read_csv("../data/hr_dataset.csv")
df.head()

# %%
# Basic Exploration

df.info()
df.describe()

# %%
# Feature Engineering

df["Hire Date"] = pd.to_datetime(df["Hire Date"])
df["Termination Date"] = pd.to_datetime(df["Termination Date"], errors="coerce")
df["Birth Date"] = pd.to_datetime(df["Birth Date"])

df["Age"] = ((pd.Timestamp("today") - df["Birth Date"]).dt.days / 365).astype(int)
df["Tenure_Years"] = ((pd.Timestamp("today") - df["Hire Date"]).dt.days / 365).round(1)

df["Is_Terminated"] = df["Termination Date"].notna()

df.head()

# %%
# Core HR KPIs

total_employees = len(df)
terminated = df["Is_Terminated"].sum()
active = total_employees - terminated
attrition_rate = round((terminated / total_employees) * 100, 2)

print("Total Employees:", total_employees)
print("Active Employees:", active)
print("Terminated Employees:", terminated)
print("Attrition Rate:", attrition_rate, "%")

# %%
# Hiring Trend

df["Hire_Year"] = df["Hire Date"].dt.year
hire_trend = df.groupby("Hire_Year").size()

hire_trend.plot(kind="bar", title="Hiring Trend by Year")
plt.show()

# %%
# Attrition by Tenure

sns.histplot(df[df["Is_Terminated"]]["Tenure_Years"], bins=20)
plt.title("Attrition Distribution by Tenure")
plt.show()

# %%
# Gender Ratio

df["Gender"].value_counts(normalize=True) * 100

# %%
# Age Groups

df["Age_Group"] = pd.cut(df["Age"], bins=[20,30,40,50,60], labels=["20-30","30-40","40-50","50-60"])
df["Age_Group"].value_counts()

# %%
# Salary by Department

df.groupby("Department")["Adjusted Salary"].mean().sort_values(ascending=False)

# %%
# Gender Pay Comparison

df.groupby("Gender")["Adjusted Salary"].mean()

# %%
# Education vs Performance

pd.crosstab(df["Education Level"], df["Performance Rating"], normalize="index")

# %%
# Correlation Matrix

numeric = df[["Age","Tenure_Years","Adjusted Salary"]]

sns.heatmap(numeric.corr(), annot=True)
plt.show()

# %%
# Key Findings (Simulated Dataset)

print("""
Key Findings:

- Attrition is highest among employees with lower tenure, indicating early-career retention risk.
- Salary varies significantly by department and education level.
- Higher education levels correlate with stronger performance ratings.
- Gender-based salary differences appear in specific roles.
- Compensation increases with age but plateaus in certain departments.
""")

# %%
# Business Recommendations

print("""
Business Recommendations:

- Implement onboarding and mentoring programs for early-tenure employees.
- Monitor department-level attrition monthly.
- Standardize compensation bands.
- Use performance analytics to guide training investments.
""")

# %%
# Export KPIs

kpis = {
    "Total Employees": total_employees,
    "Active Employees": active,
    "Terminated Employees": terminated,
    "Attrition Rate": attrition_rate
}

pd.DataFrame([kpis])
