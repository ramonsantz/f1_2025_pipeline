import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.formula1.com/en/results/2025/fastest-laps'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')