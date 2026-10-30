-- ============================================
-- SLEEP HEALTH & LIFESTYLE ANALYSIS
-- SQL Exploratory Data Analysis
-- ============================================

USE sleep_health_analysis;

-- 1. OVERALL DATASET SUMMARY

SELECT
    COUNT(*) AS total_records,
    ROUND(AVG(age), 2) AS average_age,
    ROUND(AVG(sleep_duration), 2) AS average_sleep_duration,
    ROUND(AVG(quality_of_sleep), 2) AS average_sleep_quality,
    ROUND(AVG(stress_level), 2) AS average_stress_level,
    ROUND(AVG(physical_activity_level), 2) AS average_physical_activity,
    ROUND(AVG(daily_steps), 0) AS average_daily_steps
FROM sleep_records;

-- 2. SLEEP QUALITY BY OCCUPATION

SELECT
    occupation,
    COUNT(*) AS total_people,
    ROUND(AVG(sleep_duration), 2) AS avg_sleep_duration,
    ROUND(AVG(quality_of_sleep), 2) AS avg_sleep_quality,
    ROUND(AVG(stress_level), 2) AS avg_stress_level
FROM sleep_records
GROUP BY occupation
ORDER BY avg_sleep_quality DESC;

-- 3. SLEEP QUALITY BY GENDER

SELECT
    gender,
    COUNT(*) AS total_people,
    ROUND(AVG(sleep_duration), 2) AS avg_sleep_duration,
    ROUND(AVG(quality_of_sleep), 2) AS avg_sleep_quality,
    ROUND(AVG(stress_level), 2) AS avg_stress_level
FROM sleep_records
GROUP BY gender
ORDER BY avg_sleep_quality DESC;

-- 4. SLEEP QUALITY BY BMI CATEGORY

SELECT
    bmi_category,
    COUNT(*) AS total_people,
    ROUND(AVG(sleep_duration), 2) AS avg_sleep_duration,
    ROUND(AVG(quality_of_sleep), 2) AS avg_sleep_quality,
    ROUND(AVG(stress_level), 2) AS avg_stress_level
FROM sleep_records
GROUP BY bmi_category
ORDER BY avg_sleep_quality DESC;

-- 5. STRESS LEVEL VS SLEEP QUALITY

SELECT
    stress_level,
    COUNT(*) AS total_people,
    ROUND(AVG(sleep_duration), 2) AS avg_sleep_duration,
    ROUND(AVG(quality_of_sleep), 2) AS avg_sleep_quality
FROM sleep_records
GROUP BY stress_level
ORDER BY stress_level;

-- 6. SLEEP DURATION BY AGE GROUP

SELECT
    age_group,
    COUNT(*) AS total_people,
    ROUND(AVG(sleep_duration), 2) AS avg_sleep_duration,
    ROUND(AVG(quality_of_sleep), 2) AS avg_sleep_quality
FROM sleep_records
GROUP BY age_group
ORDER BY
    CASE age_group
        WHEN '18-25' THEN 1
        WHEN '26-35' THEN 2
        WHEN '36-45' THEN 3
        WHEN '46-55' THEN 4
        WHEN '56-65' THEN 5
        WHEN '66-80' THEN 6
    END;

    -- 7. SLEEP DISORDER DISTRIBUTION

SELECT
    COALESCE(sleep_disorder, 'Not recorded') AS sleep_disorder,
    COUNT(*) AS total_people,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM sleep_records),
        2
    ) AS percentage
FROM sleep_records
GROUP BY sleep_disorder
ORDER BY total_people DESC;

-- 8. SLEEP DISORDER BY BMI CATEGORY

SELECT
    bmi_category,
    COALESCE(sleep_disorder, 'Not recorded') AS sleep_disorder,
    COUNT(*) AS total_people
FROM sleep_records
GROUP BY
    bmi_category,
    sleep_disorder
ORDER BY
    bmi_category,
    total_people DESC;

    -- 9. SLEEP DISORDER BY OCCUPATION

SELECT
    occupation,
    COALESCE(sleep_disorder, 'Not recorded') AS sleep_disorder,
    COUNT(*) AS total_people
FROM sleep_records
GROUP BY
    occupation,
    sleep_disorder
ORDER BY
    occupation,
    total_people DESC;

    -- 10. SLEEP DISORDER BY GENDER

SELECT
    gender,
    COALESCE(sleep_disorder, 'Not recorded') AS sleep_disorder,
    COUNT(*) AS total_people
FROM sleep_records
GROUP BY
    gender,
    sleep_disorder
ORDER BY
    gender,
    total_people DESC;

    -- 11. PHYSICAL ACTIVITY VS SLEEP QUALITY

SELECT
    physical_activity_level,
    COUNT(*) AS total_people,
    ROUND(AVG(quality_of_sleep), 2) AS avg_sleep_quality,
    ROUND(AVG(sleep_duration), 2) AS avg_sleep_duration
FROM sleep_records
GROUP BY physical_activity_level
ORDER BY physical_activity_level;

-- 12. HEART RATE VS SLEEP QUALITY

SELECT
    heart_rate,
    COUNT(*) AS total_people,
    ROUND(AVG(quality_of_sleep), 2) AS avg_sleep_quality,
    ROUND(AVG(sleep_duration), 2) AS avg_sleep_duration
FROM sleep_records
GROUP BY heart_rate
ORDER BY heart_rate;

-- 13. BLOOD PRESSURE VS SLEEP QUALITY

SELECT
    ROUND(AVG(systolic_bp), 2) AS avg_systolic_bp,
    ROUND(AVG(diastolic_bp), 2) AS avg_diastolic_bp,
    ROUND(AVG(quality_of_sleep), 2) AS avg_sleep_quality,
    ROUND(AVG(sleep_duration), 2) AS avg_sleep_duration,
    COUNT(*) AS total_people
FROM sleep_records;

-- 14. SYSTOLIC BLOOD PRESSURE VS SLEEP QUALITY

SELECT
    CASE
        WHEN systolic_bp < 120 THEN 'Below 120'
        WHEN systolic_bp < 130 THEN '120-129'
        WHEN systolic_bp < 140 THEN '130-139'
        ELSE '140 and above'
    END AS systolic_bp_group,
    COUNT(*) AS total_people,
    ROUND(AVG(systolic_bp), 2) AS avg_systolic_bp,
    ROUND(AVG(quality_of_sleep), 2) AS avg_sleep_quality
FROM sleep_records
GROUP BY systolic_bp_group
ORDER BY MIN(systolic_bp);

-- 15. DAILY STEPS VS SLEEP QUALITY

SELECT
    CASE
        WHEN daily_steps < 4000 THEN 'Below 4000'
        WHEN daily_steps < 6000 THEN '4000-5999'
        WHEN daily_steps < 8000 THEN '6000-7999'
        ELSE '8000 and above'
    END AS daily_steps_group,
    COUNT(*) AS total_people,
    ROUND(AVG(daily_steps), 0) AS avg_daily_steps,
    ROUND(AVG(quality_of_sleep), 2) AS avg_sleep_quality,
    ROUND(AVG(sleep_duration), 2) AS avg_sleep_duration
FROM sleep_records
GROUP BY daily_steps_group
ORDER BY MIN(daily_steps);

-- 16. SLEEP QUALITY BY SLEEP DURATION CATEGORY

SELECT
    CASE
        WHEN sleep_duration < 6 THEN 'Below 6 hours'
        WHEN sleep_duration < 7 THEN '6-6.9 hours'
        WHEN sleep_duration < 8 THEN '7-7.9 hours'
        ELSE '8 hours and above'
    END AS sleep_duration_group,
    COUNT(*) AS total_people,
    ROUND(AVG(sleep_duration), 2) AS avg_sleep_duration,
    ROUND(AVG(quality_of_sleep), 2) AS avg_sleep_quality,
    ROUND(AVG(stress_level), 2) AS avg_stress_level
FROM sleep_records
GROUP BY sleep_duration_group
ORDER BY MIN(sleep_duration);

-- 17. DATA QUALITY CHECK

SELECT
    COUNT(*) AS total_records,

    SUM(CASE WHEN gender IS NULL THEN 1 ELSE 0 END) AS missing_gender,

    SUM(CASE WHEN occupation IS NULL THEN 1 ELSE 0 END) AS missing_occupation,

    SUM(CASE WHEN sleep_duration IS NULL THEN 1 ELSE 0 END) AS missing_sleep_duration,

    SUM(CASE WHEN quality_of_sleep IS NULL THEN 1 ELSE 0 END) AS missing_sleep_quality,

    SUM(CASE WHEN bmi_category IS NULL THEN 1 ELSE 0 END) AS missing_bmi,

    SUM(CASE WHEN sleep_disorder IS NULL THEN 1 ELSE 0 END) AS missing_sleep_disorder

FROM sleep_records;

-- 18. ADVANCED ANALYSIS USING CTE

WITH SleepQualityGroups AS (
    SELECT
        person_id,
        sleep_duration,
        quality_of_sleep,
        stress_level,
        CASE
            WHEN quality_of_sleep >= 8 THEN 'High'
            WHEN quality_of_sleep >= 5 THEN 'Moderate'
            ELSE 'Low'
        END AS sleep_quality_group
    FROM sleep_records
)

SELECT
    sleep_quality_group,
    COUNT(*) AS total_people,
    ROUND(AVG(sleep_duration), 2) AS avg_sleep_duration,
    ROUND(AVG(stress_level), 2) AS avg_stress_level
FROM SleepQualityGroups
GROUP BY sleep_quality_group
ORDER BY
    CASE sleep_quality_group
        WHEN 'High' THEN 1
        WHEN 'Moderate' THEN 2
        WHEN 'Low' THEN 3
    END;