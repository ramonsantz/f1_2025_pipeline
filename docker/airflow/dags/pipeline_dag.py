from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print("Ramon Santos! Airflow está rodando!")

with DAG(
    dag_id='f1_DataEngineer_airflow',
    start_date=datetime(2025, 5, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task = PythonOperator(
        task_id='print_hello',
        python_callable=hello_world
    )
