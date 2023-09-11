
-- prepares a MySQL server for the project PiyasaFashion

CREATE DATABASE IF NOT EXISTS piyasa_dev_db;
CREATE USER IF NOT EXISTS 'piyasa_dev'@'localhost' IDENTIFIED BY 'piyasa_dev_pwd';
GRANT ALL PRIVILEGES ON `piyasa_dev_db`.* TO 'piyasa_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'piyasa_dev'@'localhost';
FLUSH PRIVILEGES;