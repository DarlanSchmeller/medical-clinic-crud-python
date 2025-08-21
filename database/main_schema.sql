DROP DATABASE IF EXISTS `medical-clinic`;
CREATE DATABASE `medical-clinic`;
USE `medical-clinic`;
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    patient_name VARCHAR(100) NOT NULL,
    age INT,
    email VARCHAR(100) NOT NULL
);
INSERT INTO users (patient_name, age, email)
VALUES ('James Morgan', 44, 'jamesmorgan@gmail.com');
INSERT INTO users (patient_name, age, email)
VALUES ('Carl Weather', 66, 'carlweather@gmail.com');