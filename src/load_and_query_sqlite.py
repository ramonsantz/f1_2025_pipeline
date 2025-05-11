import sqlite3
import pandas as pd

#Connect SQLite
conn = sqlite3.connect('db/f1_datawarehouse.sqlite')
cursor= conn.cursor()

with open('sql/create_tables.sql', 'r') as f:
    cursor.executescript(f.read())
    
#Load CSVs
df_race = pd.read_csv('data/processed/race_results_2025_clean.csv')
df_fast = pd.read_csv('data/processed/fastest_laps_2025_clean.csv')

# Create unique drivers table
drivers = pd.DataFrame({'name': pd.concat([df_race['driver'], df_fast['driver']]).drop_duplicates()})
drivers['id'] = range(1, len(drivers)+1)

# Inserir drivers
for _, row in drivers.iterrows():
    cursor.execute("INSERT INTO drivers (id, name) VALUES (?, ?)", (row['id'], row['name']))

# Mapear driver_id nos DataFrames
df_race = df_race.merge(drivers, how='left', left_on='driver', right_on='name')
df_fast = df_fast.merge(drivers, how='left', left_on='driver', right_on='name')

# Inserir race_results
for _, row in df_race.iterrows():
    cursor.execute("""
        INSERT INTO race_results (
            track, position, no, driver_id, team, starting_grid,
            laps, time_retired, points, set_fastest_lap, fastest_lap_time, position_gain
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row['track'], row['position'], row['no'], row['id'], row['team'], row['starting_grid'],
        row['laps'], row['time/retired'], row['points'], row['set_fastest_lap'],
        row['fastest_lap_time'], row['position_gain']
    ))

# Inserir fastest_laps
for _, row in df_fast.iterrows():
    cursor.execute("""
        INSERT INTO fastest_laps (
            grand_prix, driver_id, driver_abbreviation, car, time
        ) VALUES (?, ?, ?, ?, ?)
    """, (
        row['grand_prix'], row['id'], row['driver_abbreviation'], row['car'], row['time']
    ))

# Finalizar
conn.commit()

# Abrir e rodar as consultas SQL do arquivo queries.sql
with open('sql/queries.sql', 'r') as f:
    queries = f.read().split(';')  # Separar as consultas pelo ponto e vírgula

# Executar cada consulta e exibir os resultados
for query in queries:
    if query.strip():  # Verifica se a consulta não está vazia
        cursor.execute(query)
        results = cursor.fetchall()

        print(f"\n\n{query.strip()}")
        for row in results:
            print(row)

conn.close()