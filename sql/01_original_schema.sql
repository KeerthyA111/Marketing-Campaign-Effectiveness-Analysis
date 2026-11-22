-- Original SQL recovered from the Marketing Campaign Effectiveness capstone.
-- This is basic schema creation and inspection, not analytical SQL.
-- Data types and keys reflect the original work and may require revision before loading production-like data.

CREATE DATABASE marketing_Campaign_data;
USE marketing_Campaign_data;

CREATE TABLE customers (
    Customer_ID VARCHAR(10) NOT NULL PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    City VARCHAR(50),
    Country VARCHAR(50)
);

CREATE TABLE customer_conversions (
    Customer_ID VARCHAR(10) NOT NULL PRIMARY KEY,
    Campaign_ID VARCHAR(10),
    Conversion_date DATETIME(6),
    Revenue VARCHAR(4)
);

CREATE TABLE campaigns (
    Campaign_ID VARCHAR(10) NOT NULL PRIMARY KEY,
    Campaign_Name VARCHAR(40),
    Channel_Name VARCHAR(10),
    Start_date DATETIME,
    End_date DATETIME,
    Budget VARCHAR(5)
);

CREATE TABLE impression_clicks (
    Campaign_ID VARCHAR(10) NOT NULL PRIMARY KEY,
    Campaign_Name VARCHAR(40),
    Date_impression DATE,
    Impression INT,
    Date_click DATE,
    Clicks INT
);

SELECT * FROM campaigns;
SELECT * FROM customer_conversions;
SELECT * FROM impression_clicks;
SELECT * FROM customers;
