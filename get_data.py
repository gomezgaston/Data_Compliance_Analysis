#import libraries
import requests
import pandas as pd
import json
from bs4 import BeautifulSoup

#aux functions
def country_parser(column):
    soup = BeautifulSoup(column, "html.parser")
    clean_value = soup.get_text()
    return clean_value

def link_parser(column):
    soup = BeautifulSoup(column, 'html.parser')
    clean_value = soup.find('a', href=True)   
    if clean_value is not None:
        return clean_value['href']
    else:
        return "No Link"
    
#get data from source
response = requests.get('https://www.enforcementtracker.com/data.json')
data = json.loads(response.text)
df = pd.DataFrame(data["data"], columns=['id','id_case', 'country', 'authority', 'date', 
                                        'penalty_fee', 'subjet','subjet_industry', 'law', 
                                        'summary_law', 'summary_case', 'court_file', 'see_more'])


df['country'] = df['country'].apply(lambda x: country_parser(x))
df['court_file'] = df['court_file'].apply(lambda x: link_parser(x))
df.drop(columns=["see_more", "id"], inplace=True)

df.to_csv('clean_data.csv', index=False)


