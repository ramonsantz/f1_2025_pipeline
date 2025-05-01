import os
import pandas as pd

url_csv = "https://raw.githubusercontent.com/toUpperCase78/formula1-datasets/refs/heads/master/Formula1_2025Season_RaceResults.csv"
df_race = pd.read_csv(url_csv)

df_race.to_csv('data/raw/race_results_2025.csv', index=False)
