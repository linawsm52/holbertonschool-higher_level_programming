-- Go to UTF8
USE hbtn_0c_0;

ALTER DATABASE hbtn_0c_0
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS first_table_tmp (
  id INT DEFAULT NULL,
  name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  score INT DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO first_table_tmp (id, name, score)
SELECT id, name, score FROM first_table;

DROP TABLE first_table;

RENAME TABLE first_table_tmp TO first_table;
