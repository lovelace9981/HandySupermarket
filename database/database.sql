CREATE USER IF NOT EXISTS 'USERHANDYSUPERMARKET'@'%' IDENTIFIED BY 'PASSWORD';

CREATE DATABASE IF NOT EXISTS HANDYSUPERMARKET;

GRANT ALL PRIVILEGES ON HANDYSUPERMARKET.* TO 'USERHANDYSUPERMARKET'@'%';

FLUSH PRIVILEGES;