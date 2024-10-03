import textwrap
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow1',
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
    'email': ['sender@domain.com', 'receipt@domain.com'],
    'email_on_failure': True,
    'email_on_retry': True
}

with DAG(
    dag_id='dag_with_catchup_backfill_v02',
    default_args=default_args,
    start_date=days_ago(3),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='fail_task1',
        bash_command='cd non_exist_folder'
    )

    task1.doc_md = textwrap.dedent(
    """\
        #### Task Documentation
        You can document your task using the attributes `doc_md` (markdown),
        `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
        rendered in the UI's Task Instance Details page.
        ![img](https://imgs.xkcd.com/comics/fixing_problems.png)
        **Image Credit:** Randall Munroe, [XKCD](https://xkcd.com/license.html)
    """
    )

    dag.doc_md = __doc__
    dag.doc_md = """ This is a documentation placed anywhere """


    