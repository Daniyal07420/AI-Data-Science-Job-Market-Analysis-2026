/*==============================================================================
 PHASE 5 : EXPLORATORY DATA ANALYSIS (EDA)
 Project : Global AI & Data Science Jobs Analysis 2026
==============================================================================*/

-- ============================================================================
-- 1. Total Number of Jobs
-- ============================================================================

SELECT COUNT(*) AS Total_Jobs
FROM ai_jobs;

-- ============================================================================
-- 2. Number of Unique Job Titles
-- ============================================================================

SELECT COUNT(DISTINCT job_title) AS Unique_Job_Titles
FROM ai_jobs;

-- ============================================================================
-- 3. List of Unique Job Titles
-- ============================================================================

SELECT DISTINCT job_title
FROM ai_jobs
ORDER BY job_title;

-- ============================================================================
-- 4. Salary Statistics
-- ============================================================================

SELECT
    MIN(salary_usd) AS Minimum_Salary,
    MAX(salary_usd) AS Maximum_Salary,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs;

-- ============================================================================
-- 5. Average Salary by Experience Level
-- ============================================================================

SELECT
    experience_level,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY experience_level
ORDER BY Average_Salary DESC;

-- ============================================================================
-- 6. Average Salary by Employment Type
-- ============================================================================

SELECT
    employment_type,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY employment_type
ORDER BY Average_Salary DESC;

-- ============================================================================
-- 7. Average Salary by Company Size
-- ============================================================================

SELECT
    company_size,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY company_size
ORDER BY Average_Salary DESC;

-- ============================================================================
-- 8. Top 10 Highest Paying Countries
-- ============================================================================

SELECT
    company_location,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY company_location
ORDER BY Average_Salary DESC
LIMIT 10;

-- ============================================================================
-- 9. Top 10 Highest Paying Job Titles
-- ============================================================================

SELECT
    job_title,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY job_title
ORDER BY Average_Salary DESC
LIMIT 10;

-- ============================================================================
-- 10. Average Salary by Industry
-- ============================================================================

SELECT
    industry,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY industry
ORDER BY Average_Salary DESC;

-- ============================================================================
-- 11. Average Salary by Remote Ratio
-- ============================================================================

SELECT
    remote_ratio,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY remote_ratio
ORDER BY remote_ratio;

-- ============================================================================
-- 12. Average Salary by Education Level
-- ============================================================================

SELECT
    education_level,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY education_level
ORDER BY Average_Salary DESC;

-- ============================================================================
-- 13. Average Salary by AI Usage Level
-- ============================================================================

SELECT
    ai_usage_level,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY ai_usage_level
ORDER BY Average_Salary DESC;

-- ============================================================================
-- 14. Average Salary by Certification Level
-- ============================================================================

SELECT
    certification_level,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY certification_level
ORDER BY Average_Salary DESC;

-- ============================================================================
-- 15. Average Job Satisfaction by Industry
-- ============================================================================

SELECT
    industry,
    ROUND(AVG(job_satisfaction_score),2) AS Avg_Job_Satisfaction
FROM ai_jobs
GROUP BY industry
ORDER BY Avg_Job_Satisfaction DESC;