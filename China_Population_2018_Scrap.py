import requests
from bs4 import BeautifulSoup
import pandas as pd

df_Pop = pd.DataFrame(columns= ['City_Name', 'Population'], index = [0])
index = 0

china_Dict = dict()

web_Url = requests.get('http://worldpopulationreview.com/countries/china-population/cities/')

soup = BeautifulSoup(web_Url.text, 'lxml')

# print(soup.prettify())

find_Table = soup.find('table',{'class':'table table-striped'})

tr = find_Table.findAll('tr')

for cell in tr:
    
    city = cell.findAll('td')[0].text
    population = cell.findAll('td')[1].text
    
    df_Pop.loc[index, 'City_Name'] = city
    df_Pop.loc[index, 'Population'] = population

    index  += 1
    china_Dict[city] = population
    
    print(china_Dict)
