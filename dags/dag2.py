from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator 

with DAG (
    dag_id = "dag1",
    start_date = datetime(2025, 9, 29),
    schedule_interval = timedelta(minutes= 1),
    catchup = False
) as dag :
    task_hello = BashOperator(
        task_id = "hello",
        bash_command = 'echo "My name is Mohamed Abdelkader"'
    )
    task_docker = BashOperator(
        task_id="docker",
        bash_command="ls -l /tmp"
    )

task_hello>>task_docker

