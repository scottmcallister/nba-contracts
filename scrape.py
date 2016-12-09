import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml as lxml

url = 'http://www.basketball-reference.com/contracts/players.html'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

rank = []
player_name = []
team = []
season_salary = []
contract_type = []

table = soup.find(class_='stats_table')

for row in table.find_all('tr')[2:9]:
    col = row.find_all('td')
    print col
    # rank.append(col[0].string.strip())
