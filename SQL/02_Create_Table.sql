/*==============================================================================
 PHASE 2 : CREATE TABLE
 Project : Global AI & Data Science Jobs Analysis 2026
==============================================================================*/

-- ============================================================================
-- STEP 1 : Create Main Table
-- ============================================================================

CREATE TABLE ai_jobs (

    job_title VARCHAR(100),
    experience_level VARCHAR(20),
    employment_type VARCHAR(20),
    company_size VARCHAR(20),
    company_location VARCHAR(100),
    employee_residence VARCHAR(100),
    industry VARCHAR(100),

    remote_ratio INT,
    years_experience INT,

    education_level VARCHAR(50),
    primary_language VARCHAR(50),

    has_ml_in_title BOOLEAN,
    manages_people BOOLEAN,

    team_size INT,
    certifications_count INT,

    weekly_hours INT,
    uses_ai_tools_daily BOOLEAN,
    ai_tools_hours_per_week INT,

    salary_currency VARCHAR(10),
    salary_usd DECIMAL(12,2),

    equity_offered_pct DECIMAL(5,2),
    bonus_pct DECIMAL(5,2),

    job_satisfaction_score DECIMAL(3,2),
    interviews_to_offer INT,

    switched_jobs_last_year BOOLEAN,

    upskilling_hours_per_month INT,

    fears_ai_automation_score DECIMAL(3,2),

    salary_category VARCHAR(30),
    experience_group VARCHAR(30),
    ai_usage_level VARCHAR(30),
    workload VARCHAR(30),
    certification_level VARCHAR(30),
    bonus_level VARCHAR(30),
    job_satisfaction_level VARCHAR(30)

);

-- ============================================================================
-- STEP 2 : Verify Table
-- ============================================================================

SHOW TABLES;

DESCRIBE ai_jobs;