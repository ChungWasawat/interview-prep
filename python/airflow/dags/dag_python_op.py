from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import dag
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


# variable
w_xcom = True
start_d = days_ago(1)
# start_d = datetime(2021, 10, 6)

# airflow
default_args = {
    'owner': 'airflow1',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

def greet(some_dict, w_xcom, ti):
    if w_xcom == True:
        print("some dict: ", some_dict)
        first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
        last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
        age = ti.xcom_pull(task_ids='get_age', key='age')
        print(f"Hello World! My name is {first_name} {last_name}, "
            f"and I am {age} years old!")
    else:
        print("some dict: ", some_dict)
        print(f"Hello World! My name is {some_dict['first_n']} {some_dict['last_n']}, "
            f"and I am {some_dict['age']} years old!")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Jerry')
    ti.xcom_push(key='last_name', value='Fridman')

def get_age(ti):
    ti.xcom_push(key='age', value=19)


# version 1
"""
with DAG(
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v1',
    description='Our first dag using python operator',
    start_date=datetime(2021, 10, 6),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'some_dict': {'a': 1, 'b': 2}}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1
"""
# version 2    
@dag(   default_args=default_args, 
        dag_id='our_dag_with_python_operator_v1',
        description='Our first dag using python operator',
        start_date=start_d,
        schedule_interval='@daily'        
    )
def python_operator():
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'some_dict': {'first_n': 'Marc', 'last_n': 'Lamont', 'age': 30}, 'w_xcom': w_xcom}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1
    
python_operator()