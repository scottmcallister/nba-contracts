import pandas as pd

salaries = pd.read_csv('salaries.csv')
stats = pd.read_csv('stats.csv')
standings = pd.read_csv('standings.csv')

merged = salaries.merge(stats, on='name')
final = merged.merge(standings, on='team')
final = final.sort_values(by="salary_2016-17", ascending=False)

final.to_csv("merged.csv", index=False)
