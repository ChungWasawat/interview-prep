# SQL
* "--select " to comment a line
- "/*select .. */"  to comment multiple lines
## DDL
create a table and set column details
```
create table employee (
    id int UNIQUE,
    name text,
    department text,
    position text,
    salary real
    );
```
copy table
```
CREATE TABLE employeeV2_Backup AS
SELECT * FROM employeeV2;
```
delete table
```
DROP TABLE employeeV2_Backup;
```
rename a table
```
ALTER TABLE employee
RENAME to employeeV2;
```
add new column to a table
```
ALTER TABLE employeeV2
ADD email text;
```
delete a column
```
ALTER TABLE Customers
DROP COLUMN Email;
```
change a type 
```
ALTER TABLE Persons
ADD DateOfBirth date;
--
ALTER TABLE Persons
ALTER(/MODIFY) COLUMN DateOfBirth year;
```
## DML
add new data to the table
```
INSERT INTO employee VALUES
    (1, "David", "Marketing", "CEO", 120000),
    (2, "Mary", "Marketing";, "VP", 85000),
    (3, "Henry", "Sales", "Manager", 60000);
```
update existing data
```
UPDATE employee
Set salary=99000
WHERE id=1;
```
delete rows 
1. no subquery
```
DELETE FROM employee
WHERE id in (4,5);
```
2. subquery
```
DELETE FROM Person 
WHERE id IN (
    SELECT a.id
    FROM (
        SELECT id, email,
               ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
        FROM Person
    ) a
    WHERE a.rn > 1
);
```
## DQL
* avoid to use window function [over (partition by order by)] because the cost is so expensive as db have to scan all rows
create a new column from another one
```
SELECT
    name,
    LOWER(name) || "@company.com" as company_email
FROM employee;
```
substring
```
SELECT SUBSTRING ('PostgreSQL', 1, 8);
```
regular expression
1. ~ / !~ (postgresql)
```
select *
from Patients
where conditions ~ '^(.*\s)?DIAB1' 
```
string_agg() postgresql
```
select sell_date, count(distinct product) as num_sold, string_agg(distinct product, ',') as products
from Activities
group by sell_date
order by 2 desc
```
join
```
select *
from artists as a1
join albums as a2 
	on a1.CustomerId = a2.CustomerId
	and a1.Country = a2.Country – join multiple columns
```
where as join
```
SELECT 
    artists.artistid, 
    artists.name AS artist_name, 
    albums.title AS album_name, 
    tracks.name AS song_name 
FROM artists, albums, tracks 
WHERE 
    artists.artistid = albums.artistid -- PK = FK 
    AND albums.albumid = tracks.albumid 
    AND artists.artistid IN (8, 100, 120)
    AND artists.name != "GGGG";
```
use "in" in where clause
```
SELECT *
FROM employee
WHERE department IN ("Marketing", "IT");
```
not
```
--1
select * FROM customers 
where not(country = 'france');
--2
select * FROM customers 
where country not in ( 'France', 'Brazil', 'USA' );
```
like
```
--1 % = anything
select FirstName, LastName, Country, Email FROM customers 
where Email like "%hotmail.com";
--2 _ = anything but only character
select FirstName, LastName, Country, Email FROM customers 
where FirstName like "M_rc";
```
char_length
```
select tweet_id
from Tweets
where char_length(content) > 15
```
round number
```
SELECT ROUND(salary, 2)
FROM employee;
```
case condition
```
SELECT
    Company,
    CASE
        WHEN Company is not NULL then &quot;Corporate&quot;
        ELSE &quot;End Customer&quot;
    END as segment
FROM customers;
```
basic agg function
```
SELECT 
    ROUND(AVG(milliseconds), 2) avg_mill, 
    SUM(milliseconds) sum_mill, 
    MIN(milliseconds) min_mill, 
    MAX(milliseconds) AS max_mill, 
    COUNT(milliseconds) count_mill 
FROM tracks;
```
extract date from datetime      
1. strftime (sqlite)
```
SELECT
    invoicedate,
    CAST(STRFTIME(&#39;%Y&#39;, invoicedate) AS INT) AS year,

    STRFTIME(&#39;%m&#39;, invoicedate) AS month,
    STRFTIME(&#39;%d&#39;, invoicedate) AS day,
    strftime(&#39;%Y-%M&#39;, INVOICEDATE) AS MONTHID
FROM invoices
WHERE YEAR &lt; 2010;
```
2. date_format (mysql)
```
select 
    DATE_FORMAT(trans_date, "%Y-%m") as month ,
from Transactions
where DATE_FORMAT(trans_date, "%Y-%m") = "2018-12"
```
data_add() -mysql
```
SELECT W1.id
FROM Weather W1
JOIN Weather W2
ON W1.recordDate = DATE_ADD(W2.recordDate, INTERVAL 1 DAY)
WHERE W1.temperature > W2.temperature;
```
datediff() -mysql
```
SELECT w1.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1
  AND w1.temperature > w2.temperature;
```
random number
```
SELECT name, random()
FROM tracks
order by random() DESC limit n --skip first n row
```
regular expression
1. glob
```
select FirstName, Country from customers
where upper(country) glob '[UB]*'; 
```
2. regexp
```
select FirstName, Country from customers
where upper(country) regexp '^[UB]';
```
ntile() and over() with order by
```
select 
    segment, 
    count(*), 
    avg(Milliseconds) from(
	    select 
	        title as albumName,
	        name as trackName, 
	        Milliseconds, 
	        ntile(4) over(order by Milliseconds desc) as segment -- sort millisec descendingly and divide rows to 4 groups
	from albums
	join tracks using(AlbumId)
)
group by segment;
```
coalesce(targeted column, value to replace null)
```
SELECT DISTINCT
   product_name,
   description,
   COALESCE(
      CASE WHEN 
         LENGTH(description) >= 60 
         THEN NULL 
         ELSE description 
         END, 
      product_name) product_name_or_description
FROM products
```
rank() and over() with partition by, order by
```
select * from (
	select 
	    title as albumName,
	    name as trackName, 
	    Milliseconds, 
	    rank() over(PARTITION by title order by Milliseconds) as rankNum
	from albums
	join tracks using(AlbumId)
)
where rankNum = 1;
```
* rank(): create a rank (considered by order by) for each row of the whole table or groups (from partition by) !!skip to next rank after tie (1 2 2 4)
* dense_rank(): like rank() but not skip rank (1 2 2 3)
* row_number(): assigns a sequential integer number to each row in the query’s result set, so the row number shouldn't be the same
intercept -to select only the same values from two tables 
```
SELECT id FROM book_shop 
INTERSECT 
SELECT id FROM favourite_book;
```
except -to select only distinct values of left table
```
SELECT id FROM book_shop 
EXCEPT 
SELECT id FROM favourite_book;
```
union -to select all values from both tables !!!columns have to be equivalent
```
--1
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
--2 include duplicate
SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
```

