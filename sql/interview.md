## SQL interview questions

order of execution of SQL

- `selec`t > `from` > `join` > `on` > `where` > `group by` > `having` > `order by` > `limit`

difference between `where` and `having`

- both are used to filter records but where used before aggregation and having used after aggregation

when to use `group by`

- want to apply aggregation function like average to specific value like region to find the aggregated records of the value in different kind

all types of `join` 

- `inner join`, the same records from both tables.
- `left join`, all left table data and the right table which match the left one.
- `right join`, like `left join` but opposite.
- `full join`, return all rows from both tables
- `cross join`, all data from both tables connect with each other (A, B) + (1, 2) → (A,1; A,2; B,1; B,2)
- `natural join`, `inner join` but no need to identify the matched column it will take the column that match from both tables automatically

what are triggers in SQL

- set of instructions that automatically execute when a specified event occurs in the database
    - **Insert Triggers**: Fired when records are added to a table.
    - **Update Triggers**: Fired when records in a table are modified.
    - **Delete Triggers**: Fired when records are removed from a table.

what is stored procedure in SQL

- a set of precompiled SQL statements that can be executed as a single unit

explain all types of window functions

- **Aggregate Functions:  `AVG(salary) OVER (PARTITION BY dept_id)` , `SUM(salary) OVER (ORDER BY emp_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`**
- **Ranking Functions (ROW_NUMBER(), RANK(), DENSE_RANK(), NTILE(n)): `RANK() OVER (ORDER BY salary DESC)`**
- **Value Functions (LAG(), LEAD(), FIRST_VALUE(), LAST_VALUE()): `LAG(salary, 1) OVER (ORDER BY emp_id)`**

what is difference between `delete` and `truncate` 

- delete
    - DML
    - delete rows
- truncate
    - DDL
    - delete all rows and keep only column’s header

what is difference between dml, ddl, and dcl

- dcl for permission
- ddl to manage about a table (create, delete) and its columns (alter → rename, add, drop), views, roles
- dml to manipulate rows in a table (insert, update, delete)

what are aggregate functions and when do we use them 

- min, max, avg, sum, count

which is faster between cte and subquery

- cte  can be more readable when it is called multiple times

what are constraints and types of constraints

- Constraints in SQL enforce rules at the database level
    - **Primary Key, Foreign Key, Unique, Not Null, Check, Default**

type of keys

- primary key: `natural key`, `surrogate key`, `foreign key`

different types of operators

- **Arithmetic Operators:  +** (Addition), - (Subtraction), **\*** (Multiplication), **/** (Division), **%** (Modulo)
- **Comparison Operators: =** (Equal), **<>** (Not Equal), **>** (Greater Than), **<** (Less Than), **>=** (Greater Than or Equal To)**, <=** (Less Than or Equal To)
- **Logical Operators: AND, OR, NOT**
- **Bitwise Operators: & AND, | OR, ^ XOR**
- **Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT**

what are views

- virtual tables based on the result of a query. They don't store data themselves but display data stored in other tables
    - materialized view store data so it consumes storage as well as common tables