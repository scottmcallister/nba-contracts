#!/usr/bin/env bash
python scrape_standings.py
python scrape_salaries.py
python scrape_stats.py
python merge.py
