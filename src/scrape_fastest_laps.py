import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re

def run_scraper():
    url = 'https://www.formula1.com/en/results/2025/fastest-laps'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    rows = soup.select('table tbody tr')

    data = []

    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 4:
            # GP
            grand_prix_parts = cols[0].stripped_strings
            grand_prix_list = list(grand_prix_parts)
            grand_prix = grand_prix_list[-1] if grand_prix_list else ''

            # DriverName
            driver_span = cols[1]
            first_name_tag = driver_span.select_one('span.max-lg\\:hidden')
            last_name_tag = driver_span.select('span.max-md\\:hidden')
            abbr_tag = driver_span.select_one('span.md\\:hidden')

            first_name = first_name_tag.text.strip() if first_name_tag else ''
            last_name = ''.join([tag.text.strip() for tag in last_name_tag]) if last_name_tag else ''
            driver_full_name = f"{first_name} {last_name}".strip()

            driver_abbr = abbr_tag.text.strip() if abbr_tag else ''

            
            team = cols[2].text.strip()
            time = cols[3].text.strip()

            data.append([grand_prix, driver_full_name, driver_abbr, team, time])

    df = pd.DataFrame(data, columns=['Grand Prix', 'Driver', 'Driver Abbreviation', 'Car', 'Time'])

    output_path = os.path.join('data', 'raw', 'fastest_laps_2025.csv')
    df.to_csv(output_path, index=False)
    print(f"[OK] Fastest laps salvo em {output_path}")

if __name__ == "__main__":
    run_scraper()
