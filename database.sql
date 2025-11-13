CREATE DATABASE event_db;

USE event_db;

CREATE TABLE registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    mobile VARCHAR(10) NOT NULL,
    event VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
select * from registrations;

