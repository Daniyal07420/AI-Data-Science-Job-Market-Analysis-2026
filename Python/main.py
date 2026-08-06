"""
==========================================================
Project : Global AI & Data Science Job Salaries Analysis 2026
Author  : Rana Muhammad Daniyal Farooq
Tools   : Python, Pandas, NumPy, Matplotlib, SQL, Power BI

Description:
This project analyzes the global AI & Data Science job market
to identify salary trends, hiring patterns, remote work insights,
and factors influencing compensation.

==========================================================
"""

# ==========================================================
# Step 1: Import Required Libraries
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("whitegrid")

# Create folders
os.makedirs("images", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# Set the style for seaborn
sns.set_style("whitegrid")

# ==========================================================
# Step 2: Load the Dataset
# ==========================================================

try:
    df = pd.read_csv("ai_ds_job_salaries_2026.csv")
    print("=" * 60)
    print("Dataset Loaded Successfully!")
    print("=" * 60)

except FileNotFoundError:
    print("ERROR: Dataset file not found.")
    print("Make sure 'ai_ds_job_salaries_2026.csv' is in the project folder.")
    exit()

except Exception as e:
    print("An unexpected error occurred:")
    print(e)
    exit()


# ==========================================================
# Step 3: Display First Five Records
# ==========================================================

print("\n" + "=" * 60)
print("First Five Rows")
print("=" * 60)
print(df.head())


# ==========================================================
# Step 4: Display Last Five Records
# ==========================================================

print("\n" + "=" * 60)
print("Last Five Rows")
print("=" * 60)
print(df.tail())


# ==========================================================
# Step 5: Dataset Shape
# ==========================================================

print("\n" + "=" * 60)
print("Dataset Shape")
print("=" * 60)
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")


# ==========================================================
# Step 6: Display Column Names
# ==========================================================

print("\n" + "=" * 60)
print("Column Names")
print("=" * 60)

for i, col in enumerate(df.columns, start=1):
    print(f"{i}. {col}")


# ==========================================================
# Step 7: Data Types
# ==========================================================

print("\n" + "=" * 60)
print("Data Types")
print("=" * 60)
print(df.dtypes)


# ==========================================================
# Step 8: Dataset Information
# ==========================================================

print("\n" + "=" * 60)
print("Dataset Information")
print("=" * 60)
df.info()


# ==========================================================
# Step 9: Statistical Summary
# ==========================================================

print("\n" + "=" * 60)
print("Statistical Summary")
print("=" * 60)
print(df.describe())


# ==========================================================
# Step 10: Categorical Data Summary
# ==========================================================

print("\n" + "=" * 60)
print("Categorical Data Summary")
print("=" * 60)

categorical_columns = df.select_dtypes(include="object")

if not categorical_columns.empty:
    print(categorical_columns.describe())
else:
    print("No categorical columns found.")


# ==========================================================
# Step 11: Missing Values
# ==========================================================

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)

missing = df.isnull().sum()

print(missing)

print("\nTotal Missing Values :", missing.sum())


# ==========================================================
# Step 12: Duplicate Records
# ==========================================================

print("\n" + "=" * 60)
print("Duplicate Records")
print("=" * 60)

duplicates = df.duplicated().sum()

print("Duplicate Rows :", duplicates)


# ==========================================================
# Step 13: Memory Usage
# ==========================================================

print("\n" + "=" * 60)
print("Memory Usage")
print("=" * 60)

memory = df.memory_usage(deep=True).sum() / (1024 * 1024)

print(f"Total Memory Used : {memory:.2f} MB")


# ==========================================================
# Step 14: Unique Values
# ==========================================================

print("\n" + "=" * 60)
print("Unique Values in Each Column")
print("=" * 60)

print(df.nunique())


# ==========================================================
# Step 15: Dataset Preview Complete
# ==========================================================

print("\n" + "=" * 60)
print("Exploratory Data Analysis (Phase 1) Completed Successfully.")
print("=" * 60)



# =====================================================
# Step 1: Dataset Shape Before Cleaning
# =====================================================

print("\n" + "=" * 60)
print("Dataset Shape Before Cleaning")
print("=" * 60)
print(df.shape)


# =====================================================
# Step 2: Missing Values
# =====================================================

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)
print(df.isnull().sum())


# =====================================================
# Step 3: Missing Value Percentage
# =====================================================

missing_percentage = (df.isnull().sum() / len(df)) * 100

print("\n" + "=" * 60)
print("Missing Value Percentage")
print("=" * 60)
print(missing_percentage.sort_values(ascending=False))


# =====================================================
# Step 4: Remove Duplicate Records
# =====================================================

duplicates = df.duplicated().sum()

print("\n" + "=" * 60)
print(f"Duplicate Records : {duplicates}")
print("=" * 60)

df = df.drop_duplicates()

print("Dataset Shape After Removing Duplicates:")
print(df.shape)


# =====================================================
# Step 5: Data Types
# =====================================================

print("\n" + "=" * 60)
print("Data Types")
print("=" * 60)
print(df.dtypes)


# =====================================================
# Step 6: Clean Text Columns
# =====================================================

text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

print("\nText Columns Cleaned Successfully!")


# =====================================================
# Step 7: Detect Salary Column
# =====================================================

if "salary_usd" in df.columns:
    salary_col = "salary_usd"
elif "salary_in_usd" in df.columns:
    salary_col = "salary_in_usd"
else:
    raise KeyError(
        "Salary column not found. Please check your dataset column names."
    )


# =====================================================
# Step 8: Salary Summary
# =====================================================

print("\n" + "=" * 60)
print("Salary Summary")
print("=" * 60)
print(df[salary_col].describe())


# =====================================================
# Step 9: Salary Outlier Detection (IQR Method)
# =====================================================

Q1 = df[salary_col].quantile(0.25)
Q3 = df[salary_col].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

outliers = df[
    (df[salary_col] < lower_limit) |
    (df[salary_col] > upper_limit)
]

print("\n" + "=" * 60)
print("Salary Outlier Detection")
print("=" * 60)
print(f"Total Salary Outliers : {len(outliers)}")


# =====================================================
# Step 10: Negative Salary Check
# =====================================================

negative_salary = df[df[salary_col] < 0]

print("\n" + "=" * 60)
print("Negative Salary Records")
print("=" * 60)
print(f"Total Negative Salary Records : {len(negative_salary)}")


# =====================================================
# Step 11: Create Output Folder
# =====================================================

os.makedirs("outputs", exist_ok=True)


# =====================================================
# Step 12: Save Clean Dataset
# =====================================================

output_file = os.path.join("outputs", "cleaned_ai_ds_jobs.csv")

df.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("Clean Dataset Saved Successfully!")
print(f"File Location : {output_file}")
print("=" * 60)




# =====================================================
# Phase 3: Exploratory Data Analysis (EDA)
# =====================================================

import os

# Create images folder automatically
os.makedirs("images", exist_ok=True)

# =====================================================
# Detect Salary Column Automatically
# =====================================================

if "salary_usd" in df.columns:
    salary_col = "salary_usd"
elif "salary_in_usd" in df.columns:
    salary_col = "salary_in_usd"
else:
    raise KeyError("Salary column not found!")

# =====================================================
# Dataset Overview
# =====================================================

print("=" * 60)
print("Dataset Shape :", df.shape)
print("=" * 60)

print("\nColumns:")
print(df.columns.tolist())

# =====================================================
# Salary Distribution
# =====================================================

plt.figure(figsize=(10,6))

plt.hist(df[salary_col], bins=30, edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary (USD)")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig("images/salary_distribution.png", dpi=300)

plt.show()

# =====================================================
# Average Salary by Experience Level
# =====================================================

if "experience_level" in df.columns:

    salary_exp = (
        df.groupby("experience_level")[salary_col]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(8,5))

    salary_exp.plot(kind="bar")

    plt.title("Average Salary by Experience Level")
    plt.xlabel("Experience Level")
    plt.ylabel("Average Salary (USD)")

    plt.tight_layout()

    plt.savefig("images/experience_salary.png", dpi=300)

    plt.show()

# =====================================================
# Average Salary by Company Size
# =====================================================

if "company_size" in df.columns:

    salary_company = (
        df.groupby("company_size")[salary_col]
        .mean()
    )

    plt.figure(figsize=(8,5))

    salary_company.plot(kind="bar")

    plt.title("Average Salary by Company Size")
    plt.xlabel("Company Size")
    plt.ylabel("Average Salary (USD)")

    plt.tight_layout()

    plt.savefig("images/company_size_salary.png", dpi=300)

    plt.show()

# =====================================================
# Top 10 Highest Paying Job Titles
# =====================================================

if "job_title" in df.columns:

    top_jobs = (
        df.groupby("job_title")[salary_col]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12,6))

    top_jobs.plot(kind="bar")

    plt.title("Top 10 Highest Paying Job Titles")
    plt.xlabel("Job Title")
    plt.ylabel("Average Salary (USD)")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig("images/top_jobs.png", dpi=300)

    plt.show()

# =====================================================
# Remote Work Analysis
# =====================================================

if "remote_ratio" in df.columns:

    remote_salary = (
        df.groupby("remote_ratio")[salary_col]
        .mean()
    )

    plt.figure(figsize=(8,5))

    remote_salary.plot(kind="bar")

    plt.title("Average Salary by Remote Ratio")
    plt.xlabel("Remote Ratio")
    plt.ylabel("Average Salary (USD)")

    plt.tight_layout()

    plt.savefig("images/remote_salary.png", dpi=300)

    plt.show()

# =====================================================
# Industry Analysis (Only if Column Exists)
# =====================================================

if "industry" in df.columns:

    industry_salary = (
        df.groupby("industry")[salary_col]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12,6))

    industry_salary.plot(kind="bar")

    plt.title("Top Paying Industries")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig("images/industry_salary.png", dpi=300)

    plt.show()

else:

    print("\nIndustry column not found. Skipping Industry Analysis.")

# =====================================================
# Correlation Matrix
# =====================================================

numeric_df = df.select_dtypes(include=["number"])

corr = numeric_df.corr()

plt.figure(figsize=(10,8))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig("images/correlation_matrix.png", dpi=300)

plt.show()

print("\n" + "=" * 60)
print("EDA Completed Successfully!")
print("All charts have been saved in the 'images' folder.")
print("=" * 60)



















# =====================================================
# Phase 4: Feature Engineering
# =====================================================

import os

# Create outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# =====================================================
# Detect Salary Column
# =====================================================

if "salary_usd" in df.columns:
    salary_col = "salary_usd"
elif "salary_in_usd" in df.columns:
    salary_col = "salary_in_usd"
else:
    raise KeyError("Salary column not found in dataset.")

# =====================================================
# Step 2: Salary Category
# =====================================================

df["salary_category"] = pd.cut(
    df[salary_col],
    bins=[0, 50000, 100000, 150000, 200000, float("inf")],
    labels=[
        "Low",
        "Medium",
        "High",
        "Very High",
        "Premium"
    ]
)

print("\nSalary Category")
print(df["salary_category"].value_counts())

# =====================================================
# Step 3: Experience Group
# =====================================================

if "years_experience" in df.columns:

    df["experience_group"] = pd.cut(
        df["years_experience"],
        bins=[0, 2, 5, 10, 50],
        labels=[
            "Entry",
            "Junior",
            "Mid",
            "Senior"
        ]
    )

    print("\nExperience Group")
    print(df["experience_group"].value_counts())

else:
    print("\nColumn 'years_experience' not found. Skipping.")

# =====================================================
# Step 4: AI Tool Usage Category
# =====================================================

if "ai_tools_hours_per_week" in df.columns:

    df["ai_usage_level"] = pd.cut(
        df["ai_tools_hours_per_week"],
        bins=[0, 5, 10, 20, 100],
        labels=[
            "Low",
            "Moderate",
            "High",
            "Very High"
        ]
    )

    print("\nAI Usage Level")
    print(df["ai_usage_level"].value_counts())

else:
    print("\nColumn 'ai_tools_hours_per_week' not found. Skipping.")

# =====================================================
# Step 5: Weekly Hours Category
# =====================================================

if "weekly_hours" in df.columns:

    df["workload"] = pd.cut(
        df["weekly_hours"],
        bins=[0, 35, 40, 50, 100],
        labels=[
            "Part Time",
            "Standard",
            "Busy",
            "Overloaded"
        ]
    )

    print("\nWorkload")
    print(df["workload"].value_counts())

else:
    print("\nColumn 'weekly_hours' not found. Skipping.")

# =====================================================
# Step 6: Certification Level
# =====================================================

if "certifications_count" in df.columns:

    df["certification_level"] = pd.cut(
        df["certifications_count"],
        bins=[-1, 0, 2, 5, 100],
        labels=[
            "None",
            "Basic",
            "Professional",
            "Expert"
        ]
    )

    print("\nCertification Level")
    print(df["certification_level"].value_counts())

else:
    print("\nColumn 'certifications_count' not found. Skipping.")

# =====================================================
# Step 7: Bonus Category
# =====================================================

if "bonus_pct" in df.columns:

    df["bonus_level"] = pd.cut(
        df["bonus_pct"],
        bins=[-1, 5, 10, 20, 100],
        labels=[
            "Low",
            "Medium",
            "High",
            "Excellent"
        ]
    )

    print("\nBonus Level")
    print(df["bonus_level"].value_counts())

else:
    print("\nColumn 'bonus_pct' not found. Skipping.")

# =====================================================
# Step 8: Job Satisfaction Category
# =====================================================

if "job_satisfaction_score" in df.columns:

    df["job_satisfaction_level"] = pd.cut(
        df["job_satisfaction_score"],
        bins=[0, 2, 3, 4, 5],
        labels=[
            "Poor",
            "Average",
            "Good",
            "Excellent"
        ]
    )

    print("\nJob Satisfaction Level")
    print(df["job_satisfaction_level"].value_counts())

else:
    print("\nColumn 'job_satisfaction_score' not found. Skipping.")

# =====================================================
# Step 9: Save Feature Engineered Dataset
# =====================================================

output_file = "outputs/featured_ai_ds_jobs.csv"

df.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("Feature Engineering Completed Successfully!")
print(f"Dataset Saved At: {output_file}")
print("=" * 60)



# =====================================================
# Step 1: Select Numeric Columns
# =====================================================

numeric_columns = df.select_dtypes(include=np.number).columns

# =====================================================
# Step 2: Mean, Median & Mode
# =====================================================

statistics = pd.DataFrame({
    "Mean": df[numeric_columns].mean(),
    "Median": df[numeric_columns].median(),
    "Mode": df[numeric_columns].mode().iloc[0]
})

print("\nMean, Median & Mode")
print(statistics)

# =====================================================
# Step 3: Standard Deviation & Variance
# =====================================================

variation = pd.DataFrame({
    "Standard Deviation": df[numeric_columns].std(),
    "Variance": df[numeric_columns].var()
})

print("\nVariation")
print(variation)

# =====================================================
# Step 4: Minimum & Maximum
# =====================================================

summary = pd.DataFrame({
    "Minimum": df[numeric_columns].min(),
    "Maximum": df[numeric_columns].max()
})

print("\nMinimum & Maximum")
print(summary)

# =====================================================
# Step 5: Correlation Matrix
# =====================================================

correlation = df[numeric_columns].corr()

print("\nCorrelation Matrix")
print(correlation)

# =====================================================
# Step 6: Correlation Heatmap
# =====================================================

plt.figure(figsize=(12,8))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    "images/statistical_correlation_heatmap.png",
    dpi=300
)

plt.show()

# =====================================================
# Step 7: Salary Percentiles
# =====================================================

print("\nSalary Percentiles")

print(
    df[salary_col].quantile(
        [0.25,0.50,0.75,0.90,0.95]
    )
)

# =====================================================
# Step 8: Skewness & Kurtosis
# =====================================================

print("\nSalary Skewness")
print(df[salary_col].skew())

print("\nSalary Kurtosis")
print(df[salary_col].kurt())

# =====================================================
# Step 9: Salary Outlier Detection
# =====================================================

Q1 = df[salary_col].quantile(0.25)
Q3 = df[salary_col].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df[salary_col] < lower) |
    (df[salary_col] > upper)
]

print("\nTotal Salary Outliers")
print(len(outliers))

# =====================================================
# Step 10: Salary Box Plot
# =====================================================

plt.figure(figsize=(8,5))

plt.boxplot(df[salary_col])

plt.title("Salary Box Plot")
plt.ylabel("Salary (USD)")

plt.tight_layout()

plt.savefig(
    "images/salary_boxplot.png",
    dpi=300
)

plt.show()

# =====================================================
# Step 11: Export Reports
# =====================================================

statistics.to_csv(
    "outputs/statistical_summary.csv",
    index=True
)

variation.to_csv(
    "outputs/statistical_variation.csv",
    index=True
)

summary.to_csv(
    "outputs/min_max_summary.csv",
    index=True
)

correlation.to_csv(
    "outputs/correlation_matrix.csv",
    index=True
)

print("="*60)
print("Statistical Reports Saved Successfully!")
print("Location : outputs/")
print("="*60)



















# =====================================================
# Step 2: Top Paying Job Titles
# =====================================================

top_jobs = (
    df.groupby("job_title")["salary_usd"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Highest Paying Job Titles")
print(top_jobs)

# 📌 Business Insight
#Executive and specialized AI roles consistently command the highest salaries, indicating a premium for advanced technical expertise.


# =====================================================
# Step 3: Experience Level Analysis
# =====================================================

experience_salary = (
    df.groupby("experience_level")["salary_usd"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Salary by Experience Level")
print(experience_salary)

# 📌 Business Insight

#Salary increases significantly with experience, highlighting career progression as a key driver of compensation.


# =====================================================
# Step 4: Company Size Analysis
# =====================================================

company_salary = (
    df.groupby("company_size")["salary_usd"]
    .mean()
)

print("\nAverage Salary by Company Size")
print(company_salary)
# 📌 Business Insight
# Large organizations generally provide higher salaries than small and medium-sized companies.


# =====================================================
# Step 5: Country Analysis
# =====================================================

country_salary = (
    df.groupby("company_location")["salary_usd"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Paying Countries")
print(country_salary)
#📌 Business Insight
# Compensation varies considerably across countries, reflecting differences in economic conditions and demand for AI talent.


# =====================================================
# Step 6: Industry Analysis
# =====================================================

industry_salary = (
    df.groupby("industry")["salary_usd"]
    .mean()
    .sort_values(ascending=False)
)

print("\nIndustry Analysis")
print(industry_salary)

# 📌 Business Insight
# Certain industries consistently offer above-average salaries, indicating stronger investment in AI capabilities.


# =====================================================
# Step 7: Remote Work Analysis
# =====================================================

remote_salary = (
    df.groupby("remote_ratio")["salary_usd"]
    .mean()
)

print("\nRemote Work Analysis")
print(remote_salary)

# 📌 Business Insight
#Fully remote positions remain competitive in compensation, suggesting that remote work continues to be a viable employment model.


# =====================================================
# Step 8: Certification Analysis
# =====================================================

cert_salary = (
    df.groupby("certification_level")["salary_usd"]
    .mean()
)

print("\nCertification Analysis")
print(cert_salary)

# 📌 Business Insight
# Professionals with more certifications tend to earn higher salaries, suggesting that continuous learning may contribute to career growth.


# =====================================================
# Step 9: AI Tool Usage
# =====================================================

ai_usage = (
    df.groupby("ai_usage_level")["salary_usd"]
    .mean()
)

print("\nAI Tool Usage Analysis")
print(ai_usage)

# 📌 Business Insight

# Higher AI tool usage is associated with higher average salaries, indicating that AI proficiency is valued in the job market.


# =====================================================
# Step 10: Job Satisfaction
# =====================================================

satisfaction = (
    df.groupby("job_satisfaction_level")["salary_usd"]
    .mean()
)

print("\nJob Satisfaction Analysis")
print(satisfaction)

# 📌 Business Insight

# Employees reporting higher job satisfaction also tend to receive higher salaries, though this relationship should be interpreted alongside other factors.


# =====================================================
# Step 11: Export Business Insights
# =====================================================

top_jobs.to_csv("outputs/top_paying_jobs.csv")
country_salary.to_csv("outputs/top_paying_countries.csv")
industry_salary.to_csv("outputs/top_industries.csv")

print(" Business Insight Reports Saved Successfully!")

# 📄 Executive Summary (Report)

# This project analyzed 5,000 AI and Data Science job records to identify salary trends, workforce patterns, and factors influencing compensation.
# Key findings include:
# • Senior professionals consistently earn higher salaries than entry-level employees.
# • Large organizations generally offer more competitive compensation packages.
# • AI-focused and executive job titles command the highest salaries.
# • Countries differ significantly in salary levels, reflecting regional market conditions.
# • Continuous upskilling, certifications, and AI tool usage are associated with higher earning potential.
# • Remote work remains a competitive employment model with attractive salary opportunities.



# 📄 Business Recommendations

# 1. Encourage continuous learning and professional certifications.
# 2. Prioritize AI tool proficiency to improve career opportunities.
# 3. Benchmark salaries by country before expanding hiring.
# 4. Invest in experienced professionals for leadership roles.
# 5. Maintain flexible remote work policies to attract global talent.
# 6. Use salary benchmarking to remain competitive in the AI job market.