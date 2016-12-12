from bs4 import BeautifulSoup
import pandas as pd
import lxml as lxml
import csv

print "parsing team standings"

f = open('standings.html', 'r')
soup = BeautifulSoup(f, 'lxml')
east_table = soup.find("table", {"id": "confs_standings_E"})
west_table = soup.find("table", {"id": "confs_standings_W"})


def parse_table(table, writer):
    for row in table.find_all('tr')[1:15]:
        col = row.find_all('td')
        team = row.find('th')
        writer.writerow({
            'team': BeautifulSoup(str(team), 'lxml').text.encode('utf8'),
            'wins': BeautifulSoup(str(col[0]), 'lxml').text.encode('utf8'),
            'losses': BeautifulSoup(str(col[1]), 'lxml').text.encode('utf8'),
            'win_percentage': BeautifulSoup(str(col[2]), 'lxml').text
            .encode('utf8')
        })

with open('standings.csv', 'w') as csvfile:
    fieldnames = [
        'team',
        'wins',
        'losses',
        'win_percentage'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    parse_table(east_table, writer)
    parse_table(west_table, writer)
