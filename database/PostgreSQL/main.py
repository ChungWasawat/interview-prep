from sqlalchemy import insert, func
from sqlalchemy import Table, Column, ForeignKey, ForeignKeyConstraint
from sqlalchemy import Integer, Text, Date, Boolean
from utils.db_sqlalchemy import db_connect, create_tables, metadata

def insert_rows(connection, table, data):

    connection.execute(insert(table), data)
    connection.commit()

if __name__ == "__main__":
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
    create_tables(engine)

    new_courses = [
        {"course_name": "Computer", "credits": 2},
        {"course_name": "Math", "credits": 3},
        {"course_name": "English", "credits": 3},
    ]
    insert_rows(connection, course, new_courses)

    new_students = [
        {"first_name": "Wanda", "last_name": "Amore", "date_of_birth": "12 Jan 2015"},
        {"first_name": "Clifford", "last_name": "Wilkinson", "date_of_birth": "23 May 2015"},
        {"first_name": "Marc", "last_name": "Lamont", "date_of_birth": "8 Feb 2015"},
        {"first_name": "Joanne", "last_name": "Rowe", "date_of_birth": "30 Jun 2015"},
    ]
    insert_rows(connection, students, new_students)

    new_courses_att = [
        {"course_id": 1, "student_id": 1, "attended_date": "28 Jul 2024", "attended": True},
        {"course_id": 1, "student_id": 2, "attended_date": "28 Jul 2024", "attended": True},
        {"course_id": 1, "student_id": 3, "attended_date": "28 Jul 2024", "attended": False},
        {"course_id": 1, "student_id": 4, "attended_date": "28 Jul 2024", "attended": True},
        {"course_id": 2, "student_id": 1, "attended_date": "27 Jul 2024", "attended": False},
        {"course_id": 2, "student_id": 2, "attended_date": "27 Jul 2024", "attended": True},
        {"course_id": 2, "student_id": 3, "attended_date": "27 Jul 2024", "attended": True},
        {"course_id": 2, "student_id": 4, "attended_date": "27 Jul 2024", "attended": False},
        {"course_id": 3, "student_id": 1, "attended_date": "28 Jul 2024", "attended": True},
        {"course_id": 3, "student_id": 2, "attended_date": "28 Jul 2024", "attended": True},
        {"course_id": 3, "student_id": 3, "attended_date": "28 Jul 2024", "attended": False},
        {"course_id": 3, "student_id": 4, "attended_date": "28 Jul 2024", "attended": True},
    ]
    insert_rows(connection, courses_att, new_courses_att)

    connection.close()
