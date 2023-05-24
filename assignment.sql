use website ;
select * from customers;
select count(distinct(city)) from customers ;
select distinct(city) from customers ;
select * from Order_Details ;
select min(quantity),max(quantity) from order_details;
select sum(quantity),avg(quantity) from order_details;
select * from products ;
select productid,productname from products  LIMIT 11 OFFSET 4;
select * from suppliers ;
select * from suppliers where SupplierName like '_a%';
select * from customers where not country = 'usa' and not country='canada' ;
select * from Order_Details ;
select * from orders;
select count(distinct(city)) from customers ;
SELECT *FROM Employees WHERE FirstName NOT IN ('Sanjay', 'Sonia');
CREATE TABLE SupplierDetail AS SELECT * FROM Suppliers;
DELETE FROM Customers
WHERE Country = 'Venezuela';

SELECT *
FROM Customers;




