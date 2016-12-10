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


def print_range(start_i, end_i):
    for row in table.find_all('tr')[start_i:end_i]:
        col = row.find_all('td')
        name = BeautifulSoup(col[0].string, 'lxml').text
        team = BeautifulSoup(col[1].string, 'lxml').text
        salary = BeautifulSoup(col[2].string, 'lxml').text
        print "name: "+str(name)+" team: "+str(team)+" salary: "+str(salary)

print_range(start_i=2, end_i=22)
print_range(start_i=24, end_i=44)
print_range(start_i=46, end_i=66)
print_range(start_i=68, end_i=88)
print_range(start_i=90, end_i=110)
