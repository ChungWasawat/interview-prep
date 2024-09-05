# SQL
* "--select " to comment a line
- "/*select .. */"  to comment multiple lines
## DML
1. add new data to the table
```
INSERT INTO employee VALUES
    (1, "David", "Marketing", "CEO", 120000),
    (2, "Mary", "Marketing";, "VP", 85000),
    (3, "Henry", "Sales", "Manager", 60000);

-- select from other tables
INSERT INTO dim_author
SELECT distinct author FROM dim_book_star;

-- insert data to view !!but it should be avoided
insert into films (code, title) values ('T_601', 'Yojimbo')
```
2. update existing data
```
UPDATE employee
Set salary=99000
WHERE id=1;

--different condition
UPDATE employee
Set salary=99000
WHERE id in between 2 and 5;

--update where clause on view (only views from a single table and no window or aggregation function or limit there)
update vw_films set kind = 'Dramatic' where kind = 'Drama' 
```
3. delete rows 
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
