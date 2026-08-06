/*==============================================================================
 PHASE 4 : DATA VALIDATION
==============================================================================*/

-- Total Records
SELECT COUNT(*) AS Total_Records
FROM ai_jobs;

-- Preview Data
SELECT *
FROM ai_jobs
LIMIT 10;

-- Table Structure
DESCRIBE ai_jobs;



SELECT
COUNT(*) AS Total_Records,

SUM(job_title IS NULL) AS Null_Job_Title,

SUM(company_location IS NULL) AS Null_Company,

SUM(salary_usd IS NULL) AS Null_Salary

FROM ai_jobs;





SELECT
job_title,
company_location,
salary_usd,
COUNT(*) AS Duplicate_Count
FROM ai_jobs
GROUP BY
job_title,
company_location,
salary_usd
HAVING COUNT(*) > 1;




SELECT

MIN(salary_usd) AS Minimum_Salary,

MAX(salary_usd) AS Maximum_Salary,

AVG(salary_usd) AS Average_Salary

FROM ai_jobs;





SELECT DISTINCT experience_level
FROM ai_jobs
ORDER BY experience_level;



SELECT DISTINCT company_location
FROM ai_jobs
ORDER BY company_location;




