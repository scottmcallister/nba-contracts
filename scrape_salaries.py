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
season_salaries_2016 = []
season_salaries_2017 = []
season_salaries_2018 = []
season_salaries_2019 = []
season_salaries_2020 = []
season_salaries_2021 = []
contract_type = []

table = soup.find(class_='stats_table')


def print_range(start_i, end_i):
    for row in table.find_all('tr')[start_i:end_i]:
        col = row.find_all('td')
        name = BeautifulSoup(str(col[0]), 'lxml').text
        team = BeautifulSoup(str(col[1]), 'lxml').text
        salary_2016 = BeautifulSoup(str(col[2]), 'lxml').text
        salary_2017 = BeautifulSoup(str(col[3]), 'lxml').text
        salary_2018 = BeautifulSoup(str(col[4]), 'lxml').text
        salary_2019 = BeautifulSoup(str(col[5]), 'lxml').text
        salary_2020 = BeautifulSoup(str(col[6]), 'lxml').text
        salary_2021 = BeautifulSoup(str(col[7]), 'lxml').text
        contract = BeautifulSoup(str(col[8]), 'lxml').text
        print "name: "+str(name)+" team: "+str(team)+" salary: " + \
            str(salary_2016)+" type: "+contract
        player_names.append(name)
        teams.append(team)
        season_salaries_2016.append(salary_2016)
        season_salaries_2017.append(salary_2017)
        season_salaries_2018.append(salary_2018)
        season_salaries_2019.append(salary_2019)
        season_salaries_2020.append(salary_2020)
        season_salaries_2021.append(salary_2021)
        contract_type.append(contract)

print_range(start_i=2, end_i=22)
print_range(start_i=24, end_i=44)
print_range(start_i=46, end_i=66)
print_range(start_i=68, end_i=88)
print_range(start_i=90, end_i=110)

with open('salaries.csv', 'w') as csvfile:
    fieldnames = [
        'player_name',
        'team',
        'salary_2016-17',
        'salary_2017-18',
        'salary_2018-2019',
        'salary_2019-2020',
        'salary_2020-21',
        'salary_2021-22',
        'contract_type'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for index in range(0, 99):
        writer.writerow({
            'player_name': player_names[index],
            'team': teams[index],
            'salary_2016-17': season_salaries_2016[index],
            'salary_2017-18': season_salaries_2017[index],
            'salary_2018-2019': season_salaries_2018[index],
            'salary_2019-2020': season_salaries_2019[index],
            'salary_2020-21': season_salaries_2020[index],
            'salary_2021-22': season_salaries_2021[index],
            'contract_type': contract_type[index]
        })
