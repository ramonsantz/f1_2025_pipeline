from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import papermill as pm 
import subprocess 

def ingest_race_results():
    subprocess.run(["python", "/opt/airflow/src/ingest_race_results.py"], check=True)
    
def scrape_fast_laps():
    subprocess.run(["python", "/opt/airflow/src/scrape_fastest_laps.py"], check=True)

def executar_notebook():
    notebook_path = '/opt/airflow/notebook/transform_race_data.ipynb'
    output_path = '/opt/airflow/data/output_notebook.ipynb'

    # Executa notebook com a API papermill
    pm.execute_notebook(
        input_path=notebook_path,
        output_path=output_path,
        parameters={
            "input_path_race": "/opt/airflow/data/raw/race_results_2025.csv",
            "input_path_fastest": "/opt/airflow/data/raw/fastest_laps_2025.csv",
            "output_path_race": "/opt/airflow/data/processed/race_results_2025_clean.csv",
            "output_path_fastest": "/opt/airflow/data/processed/fastest_laps_2025_clean.csv"
        }  # Passar parâmetros para o notebook
    )

default_args = {
    'owner': 'ramon',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'pipeline_dag',
    default_args=default_args,
    description='Pipeline dados F1 semanal',
    schedule_interval='@weekly',
    start_date=datetime(2025, 5, 1),
    catchup=False,
    tags=['f1', 'pipeline'],
) as dag:

    tarefa_ingestao_race = PythonOperator(
        task_id='ingest_race_results',
        python_callable=ingest_race_results
    )
    
    tarefa_scrape_fastest = PythonOperator(
        task_id='scrape_fast_laps',
        python_callable=scrape_fast_laps
    )

    tarefa_executar_notebook = PythonOperator(
        task_id='executar_notebook',
        python_callable=executar_notebook
    )

