/*
Creates eventsystem database for data pipeline mini project
Also creates the only table in the database: TicketSales
*/

DROP SCHEMA IF EXISTS eventsystem;

CREATE DATABASE eventsystem;

USE eventsystem;

CREATE TABLE TicketSales (
	ticket_id INT,
	trans_date INT,
	event_id INT,
	event_name VARCHAR(50),
    event_date DATE,
    event_type VARCHAR(10),
    event_city VARCHAR(20),
    customer_id INT,
    price DECIMAL,
    num_tickets INT
);