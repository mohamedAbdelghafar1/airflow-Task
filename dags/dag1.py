from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
def print_number():
    print('helloo')

with DAG (
    dag_id = "dag2",
    start_date = datetime(2025, 9, 29),
    schedule_interval = timedelta(minutes= 1),
    catchup = False
) as dag :
    task_python = PythonOperator(
        task_id = 'python_task',
        python_callable = print_number
    )
