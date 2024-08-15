from datetime import datetime

from faker import Faker
import random

import pandas as pd
import duckdb
import polars as pl


# constant variables
fake = Faker()
Faker.seed(42)
random.seed(42)
path = 'student/'

def create_student(student:list, student_n:int) -> list:
    for i in range(1, student_n +1):
        id = i
        name = fake.name().split(" ")
        dob = fake.date_of_birth(minimum_age=17, maximum_age= 24)
        student.append([id, name[0], name[1], dob])
    return student

def create_course(course:list, course_n:int, course_set:list) -> list:
    for i in range(1, course_n +1):
        id = i
        course_name = random.choices(course_set)
        course_set.remove(course_name[0])
        cred = random.choices([1, 2, 3], weights = [1, 3, 11])
        course.append([id, course_name[0], cred[0]])
    return course

def create_exam(exam:list, exam_n:int, course_n:int) -> list:
    for i in range(1, exam_n + 1):
        id = i
        c_id = random.randint(1, course_n)
        date = fake.date_between(start_date=datetime(2024,5,1), end_date=datetime(2024,5,12))
        exam.append([id, c_id, date])
    return exam

def create_studentexam(studentexam:dict, student_n:int, exam_n:int, exam_transaction:int) -> dict:
    for i in range(exam_transaction):
        studentexam_dict['student_id'].append(random.randint(1, student_n))
        studentexam_dict['exam_id'].append(random.randint(1, exam_n))
        studentexam_dict['score'].append(random.randint(0, 100))
    return studentexam


if __name__ == "__main__":
    student_row = 22
    course_row = 2
    exam_row = 3
    exam_transaction = 60
    course_list = ['Math', 'Physics', 'Chemistry', 'English', 'History', 'Arts']

    student_column = ["student_id", "first_name", "last_name", "date_of_birth"]
    course_column = ["course_id", "course_name", "credits"]
    exam_column = ["exam_id", "course_id", "exam_date"]
    #studentexam_column = ["student_id", "exam_id", "score"]
    studentexam_dict = {'student_id': [],  'exam_id': [],  'score': []}

    """create dataframe"""
    student_data = create_student([], student_row)
    df_student = pd.DataFrame(student_data, columns=student_column)
    pl_df_student = pl.DataFrame(student_data, schema=student_column, orient="row")
    #print(df_student, pl_df_student)

    course_data = create_course([], course_row, course_list)
    df_course = pd.DataFrame(course_data, columns=course_column)
    #pl_df_course = pl.DataFrame(course_data, schema=course_column, orient="row")
    #print(df_course, pl_df_course)

    exam_data = create_exam([], exam_row, course_row)
    df_exam = pd.DataFrame(exam_data, columns=exam_column)
    #pl_df_exam = pl.DataFrame(exam_data, schema=exam_column, orient="row")
    #print(df_exam, pl_df_exam)

    student_exam_data = create_studentexam(studentexam_dict, student_row, exam_row, exam_transaction)
    #df_studentexam = pd.DataFrame(student_exam_data)
    pl_df_studentexam = pl.DataFrame(student_exam_data)
    #print(df_studentexam, pl_df_studentexam)

    """write dataframe into files"""
    df_student.to_csv(f'{path}student.csv', index=False)
    pl_df_student.write_csv(f'{path}student_pl.csv')
    duckdb.sql("SELECT * FROM pl_df_student").write_csv(f"{path}student_duckdb.csv") 

    duckdb.sql("SELECT * FROM df_student").write_parquet(f"{path}student.parquet")
    df_course.to_parquet(f"{path}course.parquet")
    duckdb.sql("SELECT * FROM df_exam").write_parquet(f"{path}exam.parquet")
    pl_df_studentexam.write_parquet(f"{path}studentexam.parquet")


