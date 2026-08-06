/*==============================================================================
 PHASE 6 : BUSINESS ANALYSIS
 Project : Global AI & Data Science Jobs Analysis 2026
==============================================================================*/

-- ============================================================================
-- 1. Average Salary by Experience Level
-- ============================================================================

SELECT
    experience_level,
    COUNT(*) AS Total_Jobs,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY experience_level
ORDER BY Average_Salary DESC;

-- ============================================================================
-- 2. Top 10 Highest Paying Job Titles
-- ============================================================================

SELECT
    job_title,
    COUNT(*) AS Total_Jobs,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY job_title
ORDER BY Average_Salary DESC
LIMIT 10;

-- ============================================================================
-- 3. Highest Paying Countries
-- ============================================================================

SELECT
    company_location,
    COUNT(*) AS Total_Jobs,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY company_location
ORDER BY Average_Salary DESC
LIMIT 10;

-- ============================================================================
-- 4. Salary by Company Size
-- ============================================================================

SELECT
    company_size,
    COUNT(*) AS Total_Companies,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY company_size
ORDER BY Average_Salary DESC;

-- ============================================================================
-- 5. Salary by Remote Work Ratio
-- ============================================================================

SELECT
    remote_ratio,
    COUNT(*) AS Total_Jobs,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY remote_ratio
ORDER BY remote_ratio;

-- ============================================================================
-- 6. AI Tool Usage vs Salary
-- ============================================================================

SELECT
    uses_ai_tools_daily,
    COUNT(*) AS Employees,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY uses_ai_tools_daily;

-- ============================================================================
-- 7. Certification Impact on Salary
-- ============================================================================

SELECT
    certifications_count,
    COUNT(*) AS Employees,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY certifications_count
ORDER BY certifications_count;

-- ============================================================================
-- 8. Education Level vs Salary
-- ============================================================================

SELECT
    education_level,
    COUNT(*) AS Employees,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY education_level
ORDER BY Average_Salary DESC;

-- ============================================================================
-- 9. Job Satisfaction by Industry
-- ============================================================================

SELECT
    industry,
    ROUND(AVG(job_satisfaction_score),2) AS Avg_Satisfaction
FROM ai_jobs
GROUP BY industry
ORDER BY Avg_Satisfaction DESC;

-- ============================================================================
-- 10. Industries with Average Salary Above $150,000
-- ============================================================================

SELECT
    industry,
    ROUND(AVG(salary_usd),2) AS Average_Salary
FROM ai_jobs
GROUP BY industry
HAVING AVG(salary_usd) > 150000
ORDER BY Average_Salary DESC;

-- ============================================================================
-- 11. Salary Category Distribution
-- ============================================================================

SELECT
    salary_category,
    COUNT(*) AS Total_Jobs
FROM ai_jobs
GROUP BY salary_category
ORDER BY Total_Jobs DESC;

-- ============================================================================
-- 12. AI Usage Level Distribution
-- ============================================================================

SELECT
    ai_usage_level,
    COUNT(*) AS Employees
FROM ai_jobs
GROUP BY ai_usage_level
ORDER BY Employees DESC;

-- ============================================================================
-- 13. Workload Distribution
-- ============================================================================

SELECT
    workload,
    COUNT(*) AS Employees
FROM ai_jobs
GROUP BY workload
ORDER BY Employees DESC;

-- ============================================================================
-- 14. Average Weekly Hours by Experience Level
-- ============================================================================

SELECT
    experience_level,
    ROUND(AVG(weekly_hours),2) AS Avg_Weekly_Hours
FROM ai_jobs
GROUP BY experience_level
ORDER BY Avg_Weekly_Hours DESC;

-- ============================================================================
-- 15. Bonus Percentage by Company Size
-- ============================================================================

SELECT
    company_size,
    ROUND(AVG(bonus_pct),2) AS Avg_Bonus
FROM ai_jobs
GROUP BY company_size
ORDER BY Avg_Bonus DESC;