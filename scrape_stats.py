from bs4 import BeautifulSoup
import pandas as pd
import lxml as lxml
import csv

f = open('stats_2015-16.html', 'r')
soup = BeautifulSoup(f, 'lxml')
table = soup.find(class_='stats-table')

with open('stats.csv', 'w') as csvfile:
    fieldnames = [
        'name',
        'games_played',
        'minutes',
        'points',
        'field_goal_made',
        'field_goad_attempted',
        'field_goal_percentage',
        '3_point_made',
        '3_point_attempted',
        '3_point_percentage',
        'free_throw_made',
        'free_throw_attempted',
        'free_throw_percentage',
        'offensive_rebounds',
        'defensive_rebounds',
        'total_rebounds',
        'assists',
        'steals',
        'blocks',
        'turnovers',
        'efficiency',
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in table.find_all('tr')[1:270]:
        col = row.find_all('td')
        writer.writerow({
            'name': BeautifulSoup(str(col[1]), 'lxml').text,
            'games_played': BeautifulSoup(str(col[2]), 'lxml').text,
            'minutes': BeautifulSoup(str(col[3]), 'lxml').text,
            'points': BeautifulSoup(str(col[4]), 'lxml').text,
            'field_goal_made': BeautifulSoup(str(col[5]), 'lxml').text,
            'field_goad_attempted': BeautifulSoup(str(col[6]), 'lxml').text,
            'field_goal_percentage': BeautifulSoup(str(col[7]), 'lxml').text,
            '3_point_made': BeautifulSoup(str(col[8]), 'lxml').text,
            '3_point_attempted': BeautifulSoup(str(col[9]), 'lxml').text,
            '3_point_percentage': BeautifulSoup(str(col[10]), 'lxml').text,
            'free_throw_made': BeautifulSoup(str(col[11]), 'lxml').text,
            'free_throw_attempted': BeautifulSoup(str(col[12]), 'lxml').text,
            'free_throw_percentage': BeautifulSoup(str(col[13]), 'lxml').text,
            'offensive_rebounds': BeautifulSoup(str(col[14]), 'lxml').text,
            'defensive_rebounds': BeautifulSoup(str(col[15]), 'lxml').text,
            'total_rebounds': BeautifulSoup(str(col[16]), 'lxml').text,
            'assists': BeautifulSoup(str(col[17]), 'lxml').text,
            'steals': BeautifulSoup(str(col[18]), 'lxml').text,
            'blocks': BeautifulSoup(str(col[19]), 'lxml').text,
            'turnovers': BeautifulSoup(str(col[20]), 'lxml').text,
            'efficiency': BeautifulSoup(str(col[21]), 'lxml').text,
        })
