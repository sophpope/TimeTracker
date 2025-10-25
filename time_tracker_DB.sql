CREATE DATABASE time_tracker_db;

USE time_tracker_db;

CREATE TABLE time_tracked(
    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    app_name VARCHAR(100) NOT NULL,
    info VARCHAR(100),
    start_time TIME,
    end_time TIME,
    duration_seconds FLOAT(2)
);

ALTER TABLE time_tracked
ADD start_date DATETIME,
ADD end_date DATETIME;

ALTER TABLE time_tracked
RENAME COLUMN start_date to start,
RENAME COLUMN end_date to end,
DROP COLUMN start_time,
DROP COLUMN end_time;

SHOW TABLES;

SELECT * FROM time_tracked;