"""
use duckdb as sql
"""
import os
from dotenv import load_dotenv

import duckdb

#variables
load_dotenv()
path = os.getenv("STUDENT_DATA_PATH", default="NaN")
student_path = f"{path}\\student.parquet"
course_path = f"{path}\\course.parquet"
exam_path = f"{path}\\exam.parquet"
studentexam_path = f"{path}\\studentexam.parquet"

#read data
#print(duckdb.read_parquet(student_path))
#print(duckdb.sql(f"select * from '{student_path}'"))

#query 1
q1 = duckdb.sql(f"select s.first_name || ' ' || s.last_name as name,  \
                    c.course_name,                          \
                    se.score                                \
                from '{student_path}' s                     \
                join '{studentexam_path}' se                \
                on s.student_id = se.student_id             \
                join '{exam_path}' e                        \
                on se.exam_id = e.exam_id                   \
                join '{course_path}' c                      \
                on e.course_id = c.course_id                \
                where c.course_name = 'English' and         \
                    se.score > 85                           \
                ")
#print(q1)

#query 2


#query 3
q3 = duckdb.sql(f"select c.course_name,                     \
                    round( avg(se.score), 2) as average_score   \
                from '{course_path}' c                      \
                join '{exam_path}' e                        \
                on e.course_id = c.course_id                \
                join '{studentexam_path}' se                \
                on se.exam_id = e.exam_id                   \
                group by c.course_name                      \
                order by 2 desc                             \
                ")
#print(q3)

#query 4
q4 = duckdb.sql(f"select s.student_id,                  \
                s.first_name || ' ' || s.last_name as name      \
                from '{student_path}' s                 \
                left join '{studentexam_path}' se       \
                on s.student_id = se.student_id         \
                where se.exam_id is null                \
                ")
#print(q4)

#query 5
q5 = duckdb.sql(f"select distinct name, *               \
                from (                                  \
                    select c.course_name,               \
                        se.exam_id,                     \
                        s.first_name || ' ' || s.last_name as name,             \
                        se.score,                       \
                        rank_dense() over(partition by c.course_name order by se.score desc) as rank \
                    from '{course_path}' c              \
                    join '{exam_path}' e                \
                    on e.course_id = c.course_id        \
                    join '{studentexam_path}' se        \
                    on se.exam_id = e.exam_id           \
                    join '{student_path}' s             \
                    on se.student_id = s.student_id)    \
                where rank <=5                          \
                order by course_name, rank              \
                ")
#print(q5)

# q6
q6 = duckdb.sql(f"select sum( if(score > 50, 1, 0) ) as morethan50              \
                from '{studentexam_path}'               \
                group by exam_id ")
q6_5 = duckdb.sql(f"select count( * ) as morethan50     \
                    from '{studentexam_path}'           \
                    where score > 50                    \
                    group by exam_id")
#print(q6_5)

# q7 need to order by unique values rather than exam_id to get more understanding example
q7 = duckdb.sql(f"select s.first_name || ' ' || s.last_name as name,            \
                c.course_name, e.exam_id, se.score,     \
                sum(se.score) over (partition by c.course_name order by se.exam_id range unbounded preceding) as sum_score  \
                from '{student_path}' s                 \
                join '{studentexam_path}' se on s.student_id = se.student_id    \
                join '{exam_path}' e on se.exam_id = e.exam_id                  \
                join '{course_path}' c on e.course_id = c.course_id             \
                order by c.course_name, se.exam_id")
#print(q7)

# q8
q8 = duckdb.sql(f"select s.first_name || ' ' || s.last_name as name,            \
                c.course_name, e.exam_id, se.score,     \
                lag(se.score) over (partition by s.student_id, c.course_id order by e.exam_id) as prev_test,    \
                lead(se.score) over (partition by s.student_id, c.course_id order by e.exam_id) as next_test,   \
                ifnull( (se.score/prev_test) -1, 0 ) as progress_from_prev      \
                from '{student_path}' s                 \
                join '{studentexam_path}' se on s.student_id = se.student_id    \
                join '{exam_path}' e on se.exam_id = e.exam_id                  \
                join '{course_path}' c on e.course_id = c.course_id             \
                order by name, c.course_name, se.exam_id")
print(q8)