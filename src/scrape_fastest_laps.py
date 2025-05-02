# Data ingestion
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.formula1.com/en/results/2025/fastest-laps'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='f1-table')
rows = table.find('tr')[1:]

data = []
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)
    
colums = ['Grand Prix', 'Driver', 'Car', 'Time']
df_fastest = pd.DataFrame(data, columns=colums)

# Save the raw data
df_fastest.to_csv('data/raw/fastest_laps_2025.csv', index=False)

print(df_fastest)