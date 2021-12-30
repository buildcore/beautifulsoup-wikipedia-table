from bs4 import BeautifulSoup
import requests
import pandas as pd
html_data=requests.get('https://en.wikipedia.org/wiki/List_of_largest_banks')
data=html_data.text
soup = BeautifulSoup(data,'lxml')
data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[3].find_all('tr'):
    col = row.find_all('td')[1:]
    if len(col)==0:
        continue
    col = [row.text.replace('\n','') for row in col]
    col = pd.Series(col, index=data.columns)
    data = data.append(col, ignore_index=True)
result = data.to_json('bank_market_cap.json',orient="records")
print(data.head())