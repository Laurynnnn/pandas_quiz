#question 2 - Download a csv file from https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip 
# and load it into a pandas dataframe. 
# How many rows and columns are there?
import requests
import pandas as pd
import os

# Load CSV
def download_csv(url):
    r = requests.get(url)
    with open('business.csv', 'wb') as f:
        f.write(r.content)

if not os.path.exists('business.csv'):
    download_csv('https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip')

df = pd.read_csv('business.csv')

print(df)
row_count = len(df)
print("Number of rows:", row_count)
col_count = len(df.columns)
print("Number of columns:", column_count)
