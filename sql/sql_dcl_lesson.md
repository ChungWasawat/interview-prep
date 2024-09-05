# SQL
* "--select " to comment a line
- "/*select .. */"  to comment multiple lines
## DCL
1. Grant *all privilege are select, insert, delete, index(sql), create, alter(sql), drop(sql), all, update, grant(sql), truncate(postgresql), references(postgresql), connect(postgresql), temporary(postgresql)
```
GRANT SELECT, INSERT, DELETE, UPDATE ON view_name TO 'Amit'@'localhost';
--grant groups role to role
GRANT admin to alex;
```
2. Revoke
```
REVOKE ALL ON view_name FROM public; 
```