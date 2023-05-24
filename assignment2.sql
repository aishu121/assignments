CREATE DATABASE hotel_management_system;
USE hotel_management_system;

CREATE TABLE Customers (
  Cust_ID INT,
  Cust_Name VARCHAR(50),
  Cust_City VARCHAR(50),
  Cust_RoomNo INT,
  CheckIn_Time DATETIME
);
INSERT INTO Customers (Cust_ID, Cust_Name, Cust_City, Cust_RoomNo, CheckIn_Time)
VALUES
  (1, 'John Smith', 'New York', 101, '2023-05-17 10:30:00'),
  (2, 'Jane Doe', 'Los Angeles', 202, '2023-05-18 14:45:00'),
  (3, 'Robert Johnson', 'Chicago', 303, '2023-05-19 16:20:00'),
  (4, 'Emily Johnson', 'San Francisco', 404, '2023-05-20 12:00:00'),
  (5, 'Michael Brown', 'Seattle', 505, '2023-05-21 09:15:00');




