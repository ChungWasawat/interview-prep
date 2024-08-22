# SQL
* "--select " to comment a line
- "/*select .. */"  to comment multiple lines
## DDL
1. create a table and set column details
```
--need to check about datatypes in each database

create table employee (
    id int NOT NULL PRIMARY KEY ,
    pid int UNIQUE,
    name text,
    department text,
    position text,
    salary real
    );

--mysql version
create table employee (
    id int NOT NULL PRIMARY KEY,
    pid int,
    name text,
    department text,
    position text,
    salary real
    UNIQUE (pid)
    );
```
2. copy table (can create a table from a csv file with this command in duckdb)
```
CREATE TABLE employeeV2_Backup AS
SELECT * FROM employeeV2;
```
3. delete table
```
DROP TABLE employeeV2_Backup;
```
4. alter a table (rename, add new column, delete column, change datatype)
```
--rename a table
ALTER TABLE employee
RENAME to employeeV2;

--add new column to a table
ALTER TABLE employeeV2
ADD email text;

--delete a column
ALTER TABLE Customers
DROP COLUMN Email;

--change datatype 
ALTER TABLE Persons
ADD DateOfBirth date;
--change datatype 2
ALTER TABLE Persons
ALTER(/MODIFY) COLUMN DateOfBirth year;
```

## DML
1. add new data to the table
```
INSERT INTO employee VALUES
    (1, "David", "Marketing", "CEO", 120000),
    (2, "Mary", "Marketing";, "VP", 85000),
    (3, "Henry", "Sales", "Manager", 60000);
```
2. update existing data
```
UPDATE employee
Set salary=99000
WHERE id=1;
--
UPDATE employee
Set salary=99000
WHERE id in between 2 and 5;
```
delete rows 
```
--common query
DELETE FROM employee
WHERE id in (4,5);

--with subquery as condition
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
* avoid to use window function `over (partition by order by)` because the cost is so expensive as db have to scan all rows
### basic command
1. use "in" in where clause
```
SELECT *
FROM employee
WHERE department IN ("Marketing", "IT");

--not
--1
select * FROM customers 
where not(country = 'france');
--2
select * FROM customers 
where country not in ( 'France', 'Brazil', 'USA' );
```
2. basic agg function
```
SELECT 
    ROUND(AVG(milliseconds), 2) avg_mill, 
    SUM(milliseconds) sum_mill, 
    MIN(milliseconds) min_mill, 
    MAX(milliseconds) AS max_mill, 
    COUNT(milliseconds) count_mill 
FROM tracks;
```
3. random number and limit/offset
```
--show only first n row
SELECT name, random()
FROM tracks
order by random() DESC limit n 

--show after first n row
SELECT name, random()
FROM tracks
order by random() DESC offset n 
```

### work with string
1. create a new column from another one
```
SELECT
    name,
    LOWER(name) || "@company.com" as company_email
FROM employee;
```
2. `substring` to split string 
```
SELECT SUBSTRING ('COMPSCI101', 1, 7);
```
3. find string with regular expression
```
--postgresql use ~ or !~ 
select *
from Patients
where conditions ~ '^(.*\s)?DIAB1' 

--glob
select FirstName, Country from customers
where upper(country) glob '[UB]*'; 

--regexp
select FirstName, Country from customers
where upper(country) regexp '^[UB]';
```
4. find specific text using `like`
```
--1 % = anything
select FirstName, LastName, Country, Email FROM customers 
where Email like "%hotmail.com";
--2 _ = anything but only character
select FirstName, LastName, Country, Email FROM customers 
where FirstName like "M_rc";
```
5. use `string_agg()` to merge all text in to on row
```
--postgresql
select sell_date, count(distinct product) as num_sold, string_agg(distinct product, ',') as products
from Activities
group by sell_date
order by 2 desc
```
6. use `char_length` to filter a number of letters
```
select tweet_id
from Tweets
where char_length(content) > 15
```
### about date
1. extract specific format from datetime  
```
--sqlite strftime()
SELECT
    invoicedate,
    CAST(STRFTIME('%Y', invoicedate) AS INT) AS year,
    STRFTIME('%m', invoicedate) AS month,
    STRFTIME('%d', invoicedate) AS day,
    strftime('%Y-%M', INVOICEDATE) AS MONTHID
FROM invoices
WHERE YEAR = 2010;

--mysql date_format()
select 
    DATE_FORMAT(trans_date, "%Y-%m") as month ,
from Transactions
where DATE_FORMAT(trans_date, "%Y-%m") = "2018-12"
```
2. use `data_add()` to add/reduce date
```
--mysql
SELECT W1.id
FROM Weather W1
JOIN Weather W2
ON W1.recordDate = DATE_ADD(W2.recordDate, INTERVAL 1 DAY)
WHERE W1.temperature > W2.temperature;
```
3. use `datediff()` to find difference between two dates
```
--mysql
SELECT w1.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1
  AND w1.temperature > w2.temperature;
```
### deal with multiple tables
1. `inner join`
```
-- join with more than one column
select *
from artists as a1
join albums as a2 
	on a1.CustomerId = a2.CustomerId
	and a1.Country = a2.Country 
```
2. use `where` as `join`
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
3. use `intercept` to select only rows which have the same values from two tables 
```
SELECT id FROM book_shop 
INTERSECT 
SELECT id FROM favourite_book;
```
4. use `except` to select only distinct values on left table
```
SELECT id FROM book_shop 
EXCEPT 
SELECT id FROM favourite_book;
```
5. use `union` to select all values from both tables but their schemas have to be equivalent 
```
--1 no include duplicate
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers

--2 include duplicate
SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers

--3 with using natural join (similar to inner join but not return the common column)
WITH 
TheMostActiveUser AS (
    SELECT user_id, name
    FROM 
        Users
        NATURAL JOIN MovieRating
    GROUP BY user_id, name
    ORDER BY COUNT(*) DESC, name
    LIMIT 1
),
TheBestMovieFebruary AS (
    SELECT movie_id, title
    FROM
        Movies
        NATURAL JOIN MovieRating
    WHERE DATE_TRUNC('month', created_at) ='2020-02-01' 
    GROUP BY movie_id, title
    ORDER BY AVG(rating) DESC, title
    LIMIT 1
)

SELECT name AS results
FROM TheMostActiveUser
UNION ALL
SELECT title as results
FROM TheBestMovieFebruary
```
### about condition
1.  `case when` condition
```
SELECT
    Company,
    CASE
        WHEN Company is not NULL then &quot;Corporate&quot;
        ELSE &quot;End Customer&quot;
    END as segment
FROM customers;
```
2. `coalesce(targeted column, value to replace null)` 
* it can be replaced in some sql databases which have `ifnull`
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
### window function
1. `ntile()` to rows to 4 groups based on specific column
```
select 
    segment, 
    count(*), 
    avg(Milliseconds) from(
	    select 
	        title as albumName,
	        name as trackName, 
	        Milliseconds, 
	        ntile(4) over(order by Milliseconds desc) as segment 
	from albums
	join tracks using(AlbumId)
)
group by segment;
```
2. `rank()` to sort rows by column and assign a rank but if find tie, will skip to the next rank like `1 2 2 4`  
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
* `dense_rank()`: like `rank()` but not skip rank `1 2 2 3`
* `row_number()`: assigns a sequential integer number to each row in the query’s result set, so the number won't be the same




