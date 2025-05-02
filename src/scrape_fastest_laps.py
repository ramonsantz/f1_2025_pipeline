# Data ingestion
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = 'https://www.formula1.com/en/results/2025/fastest-laps'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='f1-table')
rows = table.find_all('tr')[1:]

data = []

def split_driver_name(driver_text):
    # Regular expression to separate pilot's full name and abbreviation    
    match = re.match(r"([a-zA-Z\s]+)([A-Z]{3})", driver_text)
    if match:
        name = match.group(1)  #Full name
        abbreviation = match.group(2)  #abbreviation
        return name, abbreviation
    return driver_text, ""


for row in rows:
    cols = row.find_all('td')
    
    if len(cols) > 0:
        grand_prix = cols[0].text.strip()
        
        driver_name, driver_abbr = split_driver_name(cols[1].text.strip())
        
        car = cols[2].text.strip()
        time = cols[3].text.strip()
        
        data.append([grand_prix, driver_name, driver_abbr, car, time])
    
columns = ['Grand Prix', 'Driver','Driver Abbreviation', 'Car', 'Time']
df_fastest = pd.DataFrame(data, columns=columns)

# Save the raw data
df_fastest.to_csv('data/raw/fastest_laps_2025.csv', index=False)

print(df_fastest)