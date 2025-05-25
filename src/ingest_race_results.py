# Data ingestion
import pandas as pd
import os

def run_ingestion():
    url_csv = "https://raw.githubusercontent.com/toUpperCase78/formula1-datasets/refs/heads/master/Formula1_2025Season_RaceResults.csv"
    df_race = pd.read_csv(url_csv)

    output_path = os.path.join('/opt/airflow/data/raw', 'race_results_2025.csv')
    df_race.to_csv(output_path, index=False)
    print(f"[OK] Race results salvo em {output_path}")


"""
import pandas as pd

url_csv = "https://raw.githubusercontent.com/toUpperCase78/formula1-datasets/refs/heads/master/Formula1_2025Season_RaceResults.csv"
df_race = pd.read_csv(url_csv)

df_race.to_csv('data/raw/race_results_2025.csv', index=False)
"""
