-- Go to UTF8
USE hbtn_0c_0;

ALTER DATABASE hbtn_0c_0
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
  CONVERT TO CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- Reset column definition to clear any explicit charset/collation flags
ALTER TABLE first_table
  MODIFY name VARCHAR(256);

-- Re-apply ONLY the required collation (without printing CHARACTER SET in SHOW CREATE)
ALTER TABLE first_table
  MODIFY name VARCHAR(256)
  COLLATE utf8mb4_unicode_ci;
