CREATE DATABASE BloodDonations;
USE BloodDonations;

CREATE TABLE donors
(
    name VARCHAR(100) NOT NULL,
    weight INTEGER NOT NULL,
    gender VARCHAR(6),
    date_of_birth DATE NOT NULL,
    last_donation DATE,
    last_month_sickness VARCHAR(3),
    unique_identifier VARCHAR(8) PRIMARY KEY,
    expiration_of_id DATE NOT NULL,
    blood_type VARCHAR(3) NOT NULL,
    hemoglobin INTEGER NOT NULL,
    email VARCHAR(100),
    mobil VARCHAR(13)
);

CREATE TABLE donations
(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    date_of_event DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    zip_code VARCHAR(4) NOT NULL,
    city VARCHAR(25),
    address VARCHAR(100),
    number_of_available_beds INTEGER NOT NULL,
    planned_donor_number INTEGER NOT NULL,
    final_donor_number INTEGER
);
