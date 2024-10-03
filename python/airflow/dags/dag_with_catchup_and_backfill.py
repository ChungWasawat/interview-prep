import textwrap
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# variable
start_d = days_ago(3)
# start_d = datetime(2021, 10, 6)

# airflow
default_args = {
    'owner': 'airflow1',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# textwrap.deden = removes any common leading whitespace from every line in the text.
templated_command = textwrap.dedent(
    """
{% for i in range(3) %}
    echo "{{ ds }}"
{% endfor %}
"""
)

with DAG(
    dag_id='dag_with_catchup_backfill_v1',
    default_args=default_args,
    start_date=start_d,
    schedule_interval='0 9,21 * * Tue-Fri',
    catchup=True
) as dag:
    task1 = BashOperator(
        task_id='task1',
        depends_on_past=False,
        bash_command=templated_command,
    )