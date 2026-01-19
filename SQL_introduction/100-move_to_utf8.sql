-- Go to UTF8
USE hbtn_0c_0;

DROP TABLE IF EXISTS first_table;

CREATE TABLE first_table (
  id INT DEFAULT NULL,
  name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  score INT DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
