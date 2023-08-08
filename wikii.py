from typing import List, Any
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_unicorn_startup_companies'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table')[3]

titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]

df = pd.DataFrame(columns=table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    # Print the lengths for debugging
   # print(f"Length of row data: {len(individual_row_data)}, Length of table titles: {len(table_titles)}")

    if len(individual_row_data) == len(table_titles):
        df.loc[len(df)] = individual_row_data

print(df)
df.to_csv('unicorn_startup_data.csv', index=False)




