import requests
from bs4 import BeautifulSoup
import pandas as pd

column_List = ['Population, thousands','Area, sq. km','Population density, persons per sq. km','Birth rate, per 1000 population','Death Rate, Per 1000 population',
               'Natural growth rate of population, Per 1000 population','GRP Index','Consumer Price Index','Floor Space under Construction, 10000 sq.km',
               'Number of Employed Persons','Unemployment rate in urban areas (%)','Average Wage (yuan)','Possession of private passenger vehicles',
               'Number of health care institutions']

province_List = ['Anhui','Beijing','Chongqing','Fujian','Gansu','Guangdong','Guangxi','Guizhou','Hainan','Hebei','Heilongjiang','Henan','Hubei','Hunan',
                 'Inner-Mongolia','Jiangsu','Jiangxi','Jilin','Liaoning','Ningxia','Qinghai','Shaanxi','Shandong','Shanghai','Shanxi','Sichuan','Tianjin','Tibet',
                 'Xinjiang','Yunnan','Zhejiang']

df_Pop = pd.DataFrame(columns= column_List, index = [0])

index_Df = 0

for province in province_List:
    
    for i in range(9000000):
        
        delay = 0
    
    
    url = requests.get('https://knoema.com/atlas/China/' + province)
    
    soup = BeautifulSoup(url.text,'lxml')
    
    df_Pop.loc[index_Df,'Name'] = province
    
    province_Dict = dict()
    
    fact_Table = soup.find('div',{'class':'facts'})
    
    ul = fact_Table.findAll('ul')
    
    for lst in ul:
        
        li = lst.findAll('li')
        
        for row in li :
            
            
            row = row.text.replace('\n','')
            row = row.split(':')
            
            try: 
                
                df_Pop.loc[index_Df, row[0] ] = row[1].split()[0]
                
            except : 
                
                continue
            
    index_Df += 1    
        
    



