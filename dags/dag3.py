from datetime import datetime
import random
from airflow import DAG
from airflow.operators.python import PythonOperator


# Function to generate a random number and save it
def generate_random_number():
    number = random.randint(1, 100)
    with open("/tmp/random.txt", "w") as f:
        f.write(str(number))
    print(f"Random number {number} saved to /tmp/random.txt")


# Define the DAG
with DAG(
    dag_id="random_number_generator",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",  # runs once a day
    catchup=False,
    tags=["example"],
) as dag:

    generate_task = PythonOperator(
        task_id="generate_random_number",
        python_callable=generate_random_number,
    )

    generate_task
