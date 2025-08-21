DROP DATABASE IF EXISTS `medical-clinic`;
CREATE DATABASE `medical-clinic`;
USE `medical-clinic`;
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    patient_name VARCHAR(100) NOT NULL,
    age INT,
    appointment_date DATE
)
INSERT INTO users (patient_name, age, appointment_date)
VALUES ('James Morgan', 44, '2025-09-14');
INSERT INTO users (patient_name, age, appointment_date)
VALUES ('Carl Weather', 66, '2025-10-12');