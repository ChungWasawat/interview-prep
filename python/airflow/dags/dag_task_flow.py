from datetime import datetime, timedelta

from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

# variable
start_d = days_ago(1)
# start_d = datetime(2021, 10, 6)

# airflow
default_args = {
    'owner': 'airflow1',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

@dag(dag_id='dag_with_taskflow_api_v1', 
     default_args=default_args, 
     start_date=start_d, 
     schedule_interval='@daily')
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Jerry',
            'last_name': 'Fridman'
        }

    @task()
    def get_age():
        return 19

    @task()
    def greet(first_name, last_name, age):
        print(f"Hello World! My name is {first_name} {last_name} "
              f"and I am {age} years old!")
    
    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], 
          last_name=name_dict['last_name'],
          age=age)

greet_dag = hello_world_etl()