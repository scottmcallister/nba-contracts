import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml as lxml
import csv

url = 'http://www.basketball-reference.com/contracts/players.html'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

player_names = []
teams = []
season_salaries = []
contract_type = []

table = soup.find(class_='stats_table')


def print_range(start_i, end_i):
    for row in table.find_all('tr')[start_i:end_i]:
        col = row.find_all('td')
        name = BeautifulSoup(col[0].string, 'lxml').text
        team = BeautifulSoup(col[1].string, 'lxml').text
        salary = BeautifulSoup(col[2].string, 'lxml').text
        contract = BeautifulSoup(col[8].string, 'lxml').text
        print "name: "+str(name)+" team: "+str(team)+" salary: "+str(salary)
        player_names.append(name)
        teams.append(team)
        season_salaries.append(salary)
        contract_type.append(contract)

print_range(start_i=2, end_i=22)
print_range(start_i=24, end_i=44)
print_range(start_i=46, end_i=66)
print_range(start_i=68, end_i=88)
print_range(start_i=90, end_i=110)

with open('salaries.csv', 'w') as csvfile:
    fieldnames = ['player_name', 'team', 'salary', 'contract_type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for index in range(0, 99):
        writer.writerow({
            'player_name': player_names[index],
            'team': teams[index],
            'salary': season_salaries[index],
            'contract_type': contract_type[index]
        })
