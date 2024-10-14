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
3. insert but if exist, update (only postgresql)
```
# excluded refers to the values that were attempted to be inserted
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...)
ON CONFLICT (conflict_column)
DO NOTHING | DO UPDATE SET column1 = excluded.column1, column2 = value2, ...;
```
4. delete rows 
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
5. create trigger to insert/ update/ delete rows
```
--insert log of a newly added row
CREATE TRIGGER LogNewEmployee
AFTER INSERT ON Employees
FOR EACH ROW
BEGIN
    INSERT INTO EmployeeLog (emp_id, action, action_time)
    VALUES (NEW.emp_id, 'INSERT', NOW());
END;
```
6. procedure
```
-- the procedure accept empID, newSalary as input to do an update command
CREATE PROCEDURE UpdateEmployeeSalary (IN empID INT, IN newSalary DECIMAL)
BEGIN
    UPDATE Employees SET salary = newSalary WHERE emp_id = empID;
END;
```