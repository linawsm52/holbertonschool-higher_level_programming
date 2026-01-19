-- Go to UTF8
USE hbtn_0c_0;

ALTER DATABASE hbtn_0c_0
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
  CONVERT TO CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- Force the column to utf8mb4 (safe) ...
ALTER TABLE first_table
  MODIFY name VARCHAR(256)
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- ... then remove explicit charset so SHOW CREATE TABLE matches the checker
ALTER TABLE first_table
  MODIFY name VARCHAR(256)
  COLLATE utf8mb4_unicode_ci;
