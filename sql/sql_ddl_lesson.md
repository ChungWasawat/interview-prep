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
    name text not null,
    department text,
    position text,
    salary real
    );

--mysql version
create table employee (
    id int NOT NULL,
    pid int,
    name text,
    department text,
    position text,
    salary real,
    UNIQUE (id)
    PRIMARY KEY (id)
    FOREIGN KEY (pid) REFERENCES persons(pid)
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

--delete all rows but keep headers
TRUNCATE TABLE students2;

--delete views  
--1. cascade: drop all objects depend on this view
--2. restrict-default: return error if there are objects depend on the view
drop view films [cascade | restrict]; 
```
4. alter a table (rename, add new column, delete column, change datatype)
```
--rename a table
ALTER TABLE employee
RENAME to employeeV2;

--add new column to a table
ALTER TABLE employeeV2
ADD email text;

--rename column
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;

--delete a column
ALTER TABLE Customers
DROP COLUMN Email;

--delete rows
DELETE FROM students
WHERE student_id = 5;

--change datatype 
ALTER TABLE Persons
ADD DateOfBirth date;
--change datatype 2
ALTER TABLE Persons
ALTER(/MODIFY) COLUMN DateOfBirth year;
--change datatype 3
ALTER TABLE students
ALTER COLUMN average_grade
TYPE integer
USING ROUND(average_grade); -- can transform data while changing type

--add a constraint for a foreign key
ALTER TABLE fact_booksales ADD CONSTRAINT sales_book
    FOREIGN KEY (book_id) REFERENCES dim_book_star (book_id);

--alter view
alter view [if exists] vw_name alter [column] col_name set default expression
alter view [if exists] vw_name alter [column] col_name drop default 
alter view [if exists] vw_name owner to new_owner
alter view [if exists] vw_name rename to new_name
alter view [if exists] vw_name set schema new_schema
alter view [if exists] vw_name set (view_option_name [= view_option_value])
alter view [if exists] vw_name reset (view_option_name [, ..])

--alter role 
alter role admin CREATEROLE;
```
5. create a view
```
--replace when there is update to old query like adding new column but it still remains the old one's schema 
--otherwise drop the old and create new one
create or replace view vw_customer_share
as 
select customer as customer_name
count(*) as purchase count
from sales_table
group by customer_name

--postgresql, to see all views
select * from INFORMATION_SCHEMA.views; 
--postgresql, all views except system views
select * from INFORMATION_SCHEMA.views
where table_schema not in ('pg_catalog', 'information_schema');
--postgresql, create materialized view
create materialized view vw_name as select * from table_name
refresh materialized view vw_name --can use cron to schedule view
```
6. create role 
```
create role alex with password 'password123' valid until '2010-01-01';
--more attributes
create role admin CREATEDB;
```
7. partitioning (need to have an index before do partitioning) (increase query speed as it doesn't need to scan the whole data)
```
create table sales(
    ...
    timestamp date not null
) partition by range(timestamp)
--
create table sales_2010_q1 partition of sales
    for values from ('2010-01-01') to ('2010-03-31')
--create index 
create index on sales('timestamp');
```
