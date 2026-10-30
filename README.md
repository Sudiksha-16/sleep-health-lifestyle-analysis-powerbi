# Sleep Health & Lifestyle Analysis

## Project Overview

Sleep Health & Lifestyle Analysis is a data analytics project that explores the relationship between sleep patterns, lifestyle habits, stress levels and sleep quality.

The project uses Python for data cleaning and exploratory data analysis, MySQL for querying and analyzing the dataset, and Power BI for interactive data visualization.

The objective is to identify patterns in sleep quality and understand how factors such as occupation, age, BMI category, physical activity and stress levels relate to sleep.

## Tools & Technologies

- **Python:** Pandas, NumPy, Matplotlib
- **SQL:** MySQL
- **Data Visualization:** Microsoft Power BI
- **Development Environment:** VS Code, MySQL Workbench

## Dataset

The dataset contains **1,500 records and 13 original columns** describing individual sleep and lifestyle characteristics.

Key attributes include:

- Gender and Age
- Occupation
- Sleep Duration
- Quality of Sleep
- Physical Activity Level
- Stress Level
- BMI Category
- Blood Pressure
- Heart Rate
- Daily Steps
- Sleep Disorder

## Project Workflow

### 1. Data Cleaning & Preparation — Python

- Inspected the dataset structure, column types and missing values.
- Checked for duplicate records and inconsistencies.
- Cleaned text fields and transformed relevant columns.
- Separated blood pressure into systolic and diastolic values.
- Created age groups for further analysis.
- Preserved missing sleep-disorder values instead of assuming they represented the absence of a disorder.
- Exported the cleaned dataset for further analysis.

### 2. Exploratory Data Analysis — Python

Performed exploratory analysis to investigate:

- Average sleep quality across occupations.
- Relationship between stress levels and sleep quality.
- Sleep duration across different age groups.
- Sleep-disorder distribution.
- Sleep quality by BMI category and gender.
- Physical activity levels and sleep quality.
- Correlations between numerical lifestyle and sleep variables.

Generated charts and summary CSV files to support the analysis.

### 3. SQL Analysis — MySQL

Imported the cleaned dataset into MySQL and performed analytical queries using:

- SELECT, WHERE and ORDER BY
- Aggregate functions such as COUNT, AVG and SUM
- GROUP BY
- CASE statements
- Common Table Expressions (CTEs)
- Data quality and missing-value checks

Additional analysis included sleep quality by occupation, gender and BMI, sleep-duration categories, daily-step groups, blood pressure groups and sleep-disorder distribution.

### 4. Dashboard — Power BI

Developed an interactive Power BI dashboard using the sleep health dataset to present key findings and lifestyle patterns.

The dashboard is included in the `powerbi` folder.

## Key Findings

- The dataset contains 1,500 records with no duplicate records.
- Average sleep duration is approximately 7.75 hours.
- Average sleep quality is approximately 5.83 out of 10.
- Average stress level is approximately 6.01.
- Sleep quality varies across occupations, with Artists having the highest average and Lawyers the lowest in this dataset.
- The high sleep-quality group has a lower average stress level than the moderate and low groups.
- Sleep-disorder information is missing for 961 records (64.07%).
- Average sleep quality is higher in the groups reporting longer sleep duration.

These findings describe patterns in the available dataset and do not establish causal relationships.

## Project Structure

```text
SleepHealthAnalysis/
│
├── data/
│   └── Sleep_Health_Lifestyle_Dataset.csv
│
├── src/
│   └── sleep_health_analysis.py
│
├── sql/
│   └── sleep_health_analysis.sql
│
├── powerbi/
│   └── Sleep_Health_Lifestyle_Analysis_Dashboard.pbix
│
├── reports/
│   ├── sleep_health_cleaned.csv
│   └── eda/
│       ├── Analysis CSV files
│       └── Generated charts
│
├── screenshots/
│
└── README.md
```

## Limitations

- The analysis is based on a dataset containing 1,500 records and should not be considered representative of the entire population.
- Sleep-disorder information is missing for a substantial number of records.
- Some relationships observed are correlations and do not establish causation.
- The dataset contains exactly 100 records for each occupation, which may indicate a structured or balanced sample rather than a naturally representative workforce.

## Future Improvements

- Add more detailed SQL analysis and reporting.
- Improve dashboard interactivity and filtering.
- Explore additional lifestyle factors and their relationships with sleep quality.
- Incorporate larger datasets for broader analysis.

---

**Project:** Sleep Health & Lifestyle Analysis  
**Tools:** Python | MySQL | Power BI