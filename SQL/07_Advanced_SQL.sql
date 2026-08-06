/*==============================================================================
 PHASE 7 : ADVANCED SQL ANALYSIS
 Project : Global AI & Data Science Jobs Analysis 2026
 Author  : Rana Muhammad Daniyal Farooq
==============================================================================*/

-- ============================================================================
-- 1. Rank Jobs by Salary
-- ============================================================================

SELECT
    job_title,
    salary_usd,
    RANK() OVER (ORDER BY salary_usd DESC) AS Salary_Rank
FROM ai_jobs;

-- ============================================================================
-- 2. Dense Rank Jobs by Salary
-- ============================================================================

SELECT
    job_title,
    salary_usd,
    DENSE_RANK() OVER (ORDER BY salary_usd DESC) AS Dense_Rank
FROM ai_jobs;

-- ============================================================================
-- 3. Row Number for Each Job
-- ============================================================================

SELECT
    job_title,
    salary_usd,
    ROW_NUMBER() OVER (ORDER BY salary_usd DESC) AS Row_Num
FROM ai_jobs;

-- ============================================================================
-- 4. Running Average Salary
-- ============================================================================

SELECT
    salary_usd,
    ROUND(
        AVG(salary_usd) OVER (
            ORDER BY salary_usd
        ),2
    ) AS Running_Average
FROM ai_jobs;

-- ============================================================================
-- 5. Rank Employees Within Each Country
-- ============================================================================

SELECT
    company_location,
    job_title,
    salary_usd,

    RANK() OVER (
        PARTITION BY company_location
        ORDER BY salary_usd DESC
    ) AS Country_Rank

FROM ai_jobs;

-- ============================================================================
-- 6. Top Paid Employee From Each Country
-- ============================================================================

WITH CountrySalaryRank AS (

    SELECT
        company_location,
        job_title,
        salary_usd,

        RANK() OVER (
            PARTITION BY company_location
            ORDER BY salary_usd DESC
        ) AS Salary_Rank

    FROM ai_jobs
)

SELECT *
FROM CountrySalaryRank
WHERE Salary_Rank = 1;

-- ============================================================================
-- 7. Salary Compared to Overall Average
-- ============================================================================

SELECT
    job_title,
    salary_usd,

    CASE

        WHEN salary_usd >
             (SELECT AVG(salary_usd) FROM ai_jobs)

        THEN 'Above Average'

        ELSE 'Below Average'

    END AS Salary_Status

FROM ai_jobs;

-- ============================================================================
-- 8. Salary Category Using CASE
-- ============================================================================

SELECT
    job_title,
    salary_usd,

    CASE

        WHEN salary_usd >= 200000 THEN 'Very High'

        WHEN salary_usd >= 150000 THEN 'High'

        WHEN salary_usd >= 100000 THEN 'Medium'

        ELSE 'Low'

    END AS Salary_Level

FROM ai_jobs;

-- ============================================================================
-- 9. Create Salary Summary View
-- ============================================================================

CREATE OR REPLACE VIEW vw_salary_summary AS

SELECT

    experience_level,

    COUNT(*) AS Total_Jobs,

    ROUND(AVG(salary_usd),2) AS Average_Salary,

    ROUND(MAX(salary_usd),2) AS Highest_Salary,

    ROUND(MIN(salary_usd),2) AS Lowest_Salary

FROM ai_jobs

GROUP BY experience_level;

-- View Result

SELECT *
FROM vw_salary_summary;

-- ============================================================================
-- 10. Top 10 Highest Salaries
-- ============================================================================

SELECT
    job_title,
    company_location,
    salary_usd
FROM ai_jobs
ORDER BY salary_usd DESC
LIMIT 10;

-- ============================================================================
-- 11. Employees Working More Than Average Weekly Hours
-- ============================================================================

SELECT
    job_title,
    weekly_hours,
    salary_usd
FROM ai_jobs
WHERE weekly_hours >
(
    SELECT AVG(weekly_hours)
    FROM ai_jobs
)
ORDER BY weekly_hours DESC;

-- ============================================================================
-- 12. Average Salary by AI Usage Level Using CTE
-- ============================================================================

WITH AIUsageSummary AS (

    SELECT
        ai_usage_level,
        ROUND(AVG(salary_usd),2) AS Average_Salary

    FROM ai_jobs

    GROUP BY ai_usage_level
)

SELECT *
FROM AIUsageSummary
ORDER BY Average_Salary DESC;