"""
use duckdb as sql
"""
import os
from dotenv import load_dotenv

import duckdb

#variables
load_dotenv()
path = os.getenv("STUDENT_DATA_PATH", default="NaN")
student_path = f"{path}\\student.csv"

"""
How would you modify the schema to include a new feature where each student can have an 
advisor, who is also a student in the system? Describe the changes and write an SQL query to 
find all students who are advisors. (4 points
"""
# q1 add new column "advisor"
q0 = duckdb.sql(f"create TABLE student_csv as SELECT * FROM read_csv('{student_path}')")
q0_1 = duckdb.sql(f"insert into student_csv             \
                    values (23, 'Sanghyeok', 'Lee', '2000-10-21');")
q1 = duckdb.sql(f"alter table student_csv add advisor integer")
q1_1 = duckdb.sql(f"UPDATE student_csv Set advisor=student_id-1 WHERE advisor is null and student_id%3=0;")
q1_2 = duckdb.sql(f"select * from student_csv")
#print(q1_2)


# q2 find all new advisors
q2 = duckdb.sql(f"select s2.student_id, s2.first_name || ' ' || s2.last_name as name, s2.date_of_birth \
                from student_csv s1             \
                join student_csv s2 on s1.advisor = s2.student_id")
#print(q2)

# q3 test window function
q3 = duckdb.sql(f"select student_id, first_name || ' ' || last_name as name, \
                date_of_birth, sum(student_id) over(partition by date_of_birth order by student_id) as test \
                from student_csv              \
                order by 3")
#print(q3)