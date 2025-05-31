from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import papermill as pm  # ← usamos diretamente o papermill

def executar_notebook():
    notebook_path = '/opt/airflow/src/transform_race_data.ipynb'
    output_path = '/opt/airflow/data/output_notebook.ipynb'

    # Executa o notebook diretamente com a API papermill
    pm.execute_notebook(
        input_path=notebook_path,
        output_path=output_path,
        parameters={}  # ← se quiser passar parâmetros para o notebook
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
    description='Pipeline de dados F1 semanal',
    schedule_interval='@weekly',
    start_date=datetime(2025, 5, 1),
    catchup=False,
    tags=['f1', 'pipeline'],
) as dag:

    tarefa_executar_notebook = PythonOperator(
        task_id='executar_notebook',
        python_callable=executar_notebook
    )

    tarefa_executar_notebook
