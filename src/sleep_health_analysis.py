
import pandas as pd
from pathlib import Path

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = BASE_DIR / "data" / "Sleep_Health_Lifestyle_Dataset.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

print("\n========== SLEEP HEALTH DATA ANALYSIS ==========")

# 1. Dataset dimensions
print("\n1. DATASET DIMENSIONS")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Column names
print("\n2. COLUMN NAMES")
print(df.columns.tolist())

# 3. Dataset information
print("\n3. DATASET INFORMATION")
df.info()

# 4. Missing values
print("\n4. MISSING VALUES")
print(df.isnull().sum())

# 5. Duplicate records
print("\n5. DUPLICATE RECORDS")
print("Duplicates:", df.duplicated().sum())

# 6. Statistical summary
print("\n6. STATISTICAL SUMMARY")
print(df.describe(include="all").to_string())

# 7. Sleep disorder distribution
print("\n7. SLEEP DISORDER DISTRIBUTION")
print(df["Sleep Disorder"].value_counts(dropna=False))


# 8. DATA QUALITY ANALYSIS

print("\n8. DATA QUALITY ANALYSIS")

# Missing value percentages
missing_summary = pd.DataFrame({
    "Missing Values": df.isnull().sum(),
    "Missing Percentage": (df.isnull().sum() / len(df)) * 100
})

print("\nMissing Value Summary:")
print(missing_summary.round(2))


# 9. UNIQUE CATEGORICAL VALUES

print("\n9. UNIQUE CATEGORICAL VALUES")

categorical_columns = [
    "Gender",
    "Occupation",
    "BMI Category",
    "Sleep Disorder"
]

for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].value_counts(dropna=False))


# 10. NUMERICAL COLUMN RANGES

print("\n10. NUMERICAL COLUMN RANGES")

numeric_columns = [
    "Age",
    "Sleep Duration",
    "Quality of Sleep",
    "Physical Activity Level",
    "Stress Level",
    "Heart Rate",
    "Daily Steps"
]

for column in numeric_columns:
    print(f"\n{column}")
    print("Minimum:", df[column].min())
    print("Maximum:", df[column].max())


# 11. BLOOD PRESSURE FORMAT CHECK

print("\n11. BLOOD PRESSURE FORMAT CHECK")

bp_parts = df["Blood Pressure"].astype(str).str.split("/", expand=True)

print("Number of blood pressure components:", bp_parts.shape[1])
print("Sample blood pressure values:")
print(df["Blood Pressure"].head(10).to_list())

if bp_parts.shape[1] == 2:
    systolic = pd.to_numeric(bp_parts[0], errors="coerce")
    diastolic = pd.to_numeric(bp_parts[1], errors="coerce")

    print("\nInvalid systolic values:", systolic.isna().sum())
    print("Invalid diastolic values:", diastolic.isna().sum())

print("\nDATA QUALITY CHECK COMPLETED")


# 12. DATA CLEANING AND TRANSFORMATION

print("\n12. DATA CLEANING AND TRANSFORMATION")

cleaned_df = df.copy()

# Standardize text columns
text_columns = cleaned_df.select_dtypes(include="object").columns

for column in text_columns:
    cleaned_df[column] = cleaned_df[column].str.strip()

# Split blood pressure into two columns
bp_parts = cleaned_df["Blood Pressure"].str.split("/", expand=True)

cleaned_df["Systolic BP"] = pd.to_numeric(
    bp_parts[0], errors="coerce"
)

cleaned_df["Diastolic BP"] = pd.to_numeric(
    bp_parts[1], errors="coerce"
)

# Create age groups
cleaned_df["Age Group"] = pd.cut(
    cleaned_df["Age"],
    bins=[17, 25, 35, 45, 55, 65, 80],
    labels=[
        "18-25",
        "26-35",
        "36-45",
        "46-55",
        "56-65",
        "66-80"
    ]
)

# Save cleaned dataset
OUTPUT_DIR = BASE_DIR / "reports"
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_PATH = OUTPUT_DIR / "sleep_health_cleaned.csv"

cleaned_df.to_csv(OUTPUT_PATH, index=False)

print("\nCleaned dataset saved:", OUTPUT_PATH)
print("Cleaned rows:", cleaned_df.shape[0])
print("Cleaned columns:", cleaned_df.shape[1])

print("\nNew columns:")
print(["Systolic BP", "Diastolic BP", "Age Group"])

print("\nCleaning completed successfully.")


# 13. EXPLORATORY DATA ANALYSIS (EDA)

import matplotlib.pyplot as plt

print("\n13. EXPLORATORY DATA ANALYSIS")

# Create an EDA output folder
EDA_DIR = BASE_DIR / "reports" / "eda"
EDA_DIR.mkdir(parents=True, exist_ok=True)


# ANALYSIS 1: Average sleep quality by occupation

occupation_analysis = (
    cleaned_df.groupby("Occupation")["Quality of Sleep"]
    .mean()
    .sort_values(ascending=False)
)

print("\n1. AVERAGE SLEEP QUALITY BY OCCUPATION")
print(occupation_analysis.round(2))

occupation_analysis.to_csv(
    EDA_DIR / "sleep_quality_by_occupation.csv"
)

plt.figure(figsize=(11, 6))
occupation_analysis.sort_values().plot(kind="barh")

plt.title("Average Sleep Quality by Occupation")
plt.xlabel("Average Sleep Quality")
plt.ylabel("Occupation")
plt.tight_layout()

plt.savefig(
    EDA_DIR / "sleep_quality_by_occupation.png",
    dpi=300
)
plt.close()


# ANALYSIS 2: Stress level vs sleep quality

stress_analysis = (
    cleaned_df.groupby("Stress Level")["Quality of Sleep"]
    .agg(["mean", "count"])
    .round(2)
)

print("\n2. STRESS LEVEL VS SLEEP QUALITY")
print(stress_analysis)

stress_analysis.to_csv(
    EDA_DIR / "stress_vs_sleep_quality.csv"
)

plt.figure(figsize=(9, 5))
plt.plot(
    stress_analysis.index,
    stress_analysis["mean"],
    marker="o"
)

plt.title("Average Sleep Quality by Stress Level")
plt.xlabel("Stress Level")
plt.ylabel("Average Sleep Quality")
plt.xticks(range(1, 11))
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(
    EDA_DIR / "stress_vs_sleep_quality.png",
    dpi=300
)
plt.close()


# ANALYSIS 3: Sleep duration by age group

age_analysis = (
    cleaned_df.groupby("Age Group", observed=False)["Sleep Duration"]
    .agg(["mean", "count"])
    .round(2)
)

print("\n3. SLEEP DURATION BY AGE GROUP")
print(age_analysis)

age_analysis.to_csv(
    EDA_DIR / "sleep_duration_by_age_group.csv"
)

plt.figure(figsize=(9, 5))
age_analysis["mean"].plot(kind="bar")

plt.title("Average Sleep Duration by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Sleep Duration (Hours)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    EDA_DIR / "sleep_duration_by_age_group.png",
    dpi=300
)
plt.close()


# ANALYSIS 4: Sleep disorder distribution

disorder_analysis = (
    cleaned_df["Sleep Disorder"]
    .fillna("Not recorded")
    .value_counts()
)

print("\n4. SLEEP DISORDER DISTRIBUTION")
print(disorder_analysis)

disorder_analysis.to_csv(
    EDA_DIR / "sleep_disorder_distribution.csv"
)

plt.figure(figsize=(9, 6))
disorder_analysis.plot(kind="bar")

plt.title("Distribution of Sleep Disorder Records")
plt.xlabel("Sleep Disorder Category")
plt.ylabel("Number of Records")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()

plt.savefig(
    EDA_DIR / "sleep_disorder_distribution.png",
    dpi=300
)
plt.close()


print("\nEDA analysis completed.")
print("Analysis outputs saved in:", EDA_DIR)


# 14. ADVANCED EXPLORATORY ANALYSIS

print("\n14. ADVANCED EXPLORATORY ANALYSIS")


# ANALYSIS 5: Sleep quality by BMI category

bmi_analysis = (
    cleaned_df.groupby("BMI Category")["Quality of Sleep"]
    .agg(["mean", "count"])
    .round(2)
)

print("\n5. SLEEP QUALITY BY BMI CATEGORY")
print(bmi_analysis)

bmi_analysis.to_csv(
    EDA_DIR / "sleep_quality_by_bmi.csv"
)

plt.figure(figsize=(8, 5))
bmi_analysis["mean"].plot(kind="bar")

plt.title("Average Sleep Quality by BMI Category")
plt.xlabel("BMI Category")
plt.ylabel("Average Sleep Quality")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    EDA_DIR / "sleep_quality_by_bmi.png",
    dpi=300
)
plt.close()


# ANALYSIS 6: Sleep quality by gender

gender_analysis = (
    cleaned_df.groupby("Gender")["Quality of Sleep"]
    .agg(["mean", "count"])
    .round(2)
)

print("\n6. SLEEP QUALITY BY GENDER")
print(gender_analysis)

gender_analysis.to_csv(
    EDA_DIR / "sleep_quality_by_gender.csv"
)

plt.figure(figsize=(7, 5))
gender_analysis["mean"].plot(kind="bar")

plt.title("Average Sleep Quality by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Sleep Quality")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    EDA_DIR / "sleep_quality_by_gender.png",
    dpi=300
)
plt.close()


# ANALYSIS 7: Physical activity vs sleep quality

activity_analysis = (
    cleaned_df.groupby("Physical Activity Level")["Quality of Sleep"]
    .agg(["mean", "count"])
    .reset_index()
)

print("\n7. PHYSICAL ACTIVITY VS SLEEP QUALITY")
print(activity_analysis.head(15))

activity_analysis.to_csv(
    EDA_DIR / "activity_vs_sleep_quality.csv",
    index=False
)

plt.figure(figsize=(9, 5))
plt.scatter(
    cleaned_df["Physical Activity Level"],
    cleaned_df["Quality of Sleep"],
    alpha=0.5
)

plt.title("Physical Activity Level vs Sleep Quality")
plt.xlabel("Physical Activity Level")
plt.ylabel("Sleep Quality")
plt.tight_layout()

plt.savefig(
    EDA_DIR / "activity_vs_sleep_quality.png",
    dpi=300
)
plt.close()


# ANALYSIS 8: Correlation analysis

correlation_columns = [
    "Age",
    "Sleep Duration",
    "Quality of Sleep",
    "Physical Activity Level",
    "Stress Level",
    "Heart Rate",
    "Daily Steps",
    "Systolic BP",
    "Diastolic BP"
]

correlation_matrix = cleaned_df[
    correlation_columns
].corr()

print("\n8. CORRELATION MATRIX")
print(correlation_matrix.round(2))

correlation_matrix.to_csv(
    EDA_DIR / "correlation_matrix.csv"
)

plt.figure(figsize=(11, 8))

plt.imshow(
    correlation_matrix,
    cmap="coolwarm",
    aspect="auto",
    vmin=-1,
    vmax=1
)

plt.colorbar(label="Correlation")
plt.xticks(
    range(len(correlation_columns)),
    correlation_columns,
    rotation=45,
    ha="right"
)
plt.yticks(
    range(len(correlation_columns)),
    correlation_columns
)

plt.title("Correlation Between Sleep and Lifestyle Variables")
plt.tight_layout()

plt.savefig(
    EDA_DIR / "correlation_matrix.png",
    dpi=300
)
plt.close()


print("\nAdvanced exploratory analysis completed.")

print("\n========== ANALYSIS COMPLETED ==========")
