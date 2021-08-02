from bs4 import BeautifulSoup
import pandas as pd
import requests

URL = 'https://en.wikipedia.org/wiki/Road_safety_in_Europe'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable sortable'}).tbody

rows = table.find_all('tr')

columns = [v.text.replace('\n', '').split('[')[0] for v in rows[0].find_all('th')]

df = pd.DataFrame(columns=columns)

for i in range(1, len(rows) - 1):
    tds = rows[i].find_all('td')

    if len(tds) == len(columns):
        values = [
            v.text.replace('\n', '').replace('†b', '').replace('â€“', '-').replace('â€ a', '').replace('â€ c', '')
            for v in tds
        ]
        df = df.append(pd.Series(values, index=columns), ignore_index=True)


df = df.drop(columns=[
    'Number of Seriously Injured in 2017/2018',
    'Number of People Killedper Billion km',
    'Road Network Length(in km) in 2013'
])

df = df.rename(columns=
               {'Area(thousands of km2)': 'Area',
                'Population in 2018': 'Population',
                'GDP per capita in 2018': 'GDP per capita',
                'Population density(inhabitants per km2) in 2017': 'Population density',
                'Vehicle ownership(per thousand inhabitants) in 2016': 'Vehicle Ownership',
                'Total Road Deaths in 2018': 'Total Road Deaths',
                'Road deathsper Million Inhabitants in 2018': 'Road deaths per Million Inhabitants'
                })


df = df.sort_values(['Road deaths per Million Inhabitants'], ascending=True)

df.insert(1, "Year", '2018')

df.to_csv('data.csv', index=False)
