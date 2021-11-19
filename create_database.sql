-- CREATE DATABASE STATISTICS_EXAMPLE_DB;
-- SHOW DATABASES;

-- USE STATISTICS_EXAMPLE_DB;
CREATE TABLE IF NOT EXISTS CONTINUOUS_EXAMPLE (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ORIGIN_ID INT NOT NULL,
    TOTAL_BILL FLOAT NOT NULL,
    TIP FLOAT NOT NULL,
    SEX VARCHAR(10) NOT NULL,
    SMOKER VARCHAR(5) NOT NULL,
    DAY VARCHAR(10) NOT NULL,
    TIME VARCHAR(15) NOT NULL,
    SIZE INT NOT NULL
);
