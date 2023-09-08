-- Create the database
CREATE DATABASE IF NOT EXISTS `{{MYSQL_DATABASE}}`;

-- select the database
use `{{MYSQL_DATABASE}}`;

-- Create the table of users:
CREATE TABLE IF NOT EXISTS `users` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    password VARBINARY(128) NOT NULL,
    token VARBINARY(128) NOT NULL,
    registration_date DATE,
    last_connection_date DATE,
    telegram_profile VARCHAR(255),
    active ENUM('y', 'n')
);

-- Create a user and grant privileges
CREATE USER IF NOT EXISTS '{{MYSQL_USER}}'@'%' IDENTIFIED BY '{{MYSQL_PASSWORD}}';
GRANT ALL PRIVILEGES ON `{{MYSQL_DATABASE}}`.* TO '{{MYSQL_USER}}'@'%';
FLUSH PRIVILEGES;