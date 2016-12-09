import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.basketball-reference.com/contracts/players.html'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')
