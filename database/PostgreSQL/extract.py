from sqlalchemy import select, text
from sqlalchemy import Table, Column, Integer, Text, Date, ForeignKey, Boolean
from utils.db_sqlalchemy import db_connect, metadata


def fetch_data(result, option):
    if option == "all":
        data = result.fetchall()
        for d in data:
            print(d)
            #print(d[1])

    elif option == "many":
        data = result.fetchmany(2)
        print(data)

    elif option == "one":
        data = result.fetchone()
        print(data)


engine, connection = db_connect()
course = Table(
    "courses",
    metadata,
    Column("course_id", Integer, primary_key=True, autoincrement="auto"),
    Column("course_name", Text, nullable=False),
    Column("credits", Integer, nullable=False),
)
courses_att = Table(
    "courses_attendance",
    metadata,
    Column("course_id", Integer, ForeignKey("courses.course_id", ondelete="CASCADE"), primary_key=True),
    Column("student_id", Integer, ForeignKey("students.student_id", ondelete="CASCADE"), primary_key=True),
    Column("attended_date", Date, nullable=False),
    Column("attended", Boolean, nullable=False),
)
students = Table(
    "students",
    metadata,
    Column("student_id", Integer, primary_key=True, autoincrement="auto"),
    Column("first_name", Text, nullable=False),
    Column("last_name", Text, nullable=False),
    Column("date_of_birth", Date, nullable=False),
)

query1 = select(students).where(students.c.date_of_birth < "1 Jun 2015")
query2 = course.select().where(course.c.course_id == 2)
query3 = text(f"select * from courses_attendance")

data = connection.execute(query3)
fetch_data(data, "all")
#fetch_data(data, "many")
#fetch_data(data, "one")

connection.close()

