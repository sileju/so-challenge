"""

Data collection module for the SO challenge.

This module handles fetching data from various sources.

"""

import requests
import pandas as pd
import os
import time
from datetime import datetime

CACHE_FILE = 'so_data_cache.csv'

def fetch_so_data():
    """
    Fetch monthly Stack Overflow question counts from 2008 to 2024.
    Returns a pandas DataFrame with columns: year_month, question_count.
    Caches results locally as CSV.
    """
    if os.path.exists(CACHE_FILE):
        return pd.read_csv(CACHE_FILE)

    data = []
    for year in range(2008, 2025):
        for month in range(1, 13):
            start = datetime(year, month, 1)
            if month == 12:
                end = datetime(year + 1, 1, 1)
            else:
                end = datetime(year, month + 1, 1)
            fromdate = int(start.timestamp())
            todate = int(end.timestamp())
            count = get_question_count(fromdate, todate)
            data.append({'year_month': f"{year}-{month:02d}", 'question_count': count})

    df = pd.DataFrame(data)
    df.to_csv(CACHE_FILE, index=False)
    return df

def get_question_count(fromdate, todate, retries=3):
    """
    Get the total number of questions for a given date range with retry logic.
    """
    url = f"https://api.stackexchange.com/2.3/questions?site=stackoverflow&fromdate={fromdate}&todate={todate}&order=desc&sort=activity&filter=default"
    total = 0
    page = 1
    for attempt in range(retries):
        try:
            while True:
                response = requests.get(url + f"&page={page}")
                response.raise_for_status()
                data = response.json()
                total += len(data['items'])
                if not data.get('has_more', False):
                    break
                page += 1
            return total
        except requests.RequestException:
            if attempt < retries - 1:
                time.sleep(1)
            else:
                raise