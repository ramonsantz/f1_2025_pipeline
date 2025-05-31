# Data ingestion
import pandas as pd
import os

def run_ingestion():
    url_csv = "https://raw.githubusercontent.com/toUpperCase78/formula1-datasets/refs/heads/master/Formula1_2025Season_RaceResults.csv"
    df_race = pd.read_csv(url_csv)
    
    # Salvar no container do Airflow
    airflow_output_dir = '/opt/airflow/data/raw'
    os.makedirs(airflow_output_dir, exist_ok=True)
    airflow_output_path = os.path.join(airflow_output_dir, 'race_results_2025.csv')
    df_race.to_csv(airflow_output_path, index=False)
    print(f"[OK] Race results salvo no Airflow em {airflow_output_path}")

    # Salvar localmente
    local_output_path = 'data/raw/race_results_2025.csv'
    df_race.to_csv(local_output_path, index=False)
    print(f"[OK] Race results salvo localmente em {local_output_path}")

if __name__ == "__main__":
    run_ingestion()
