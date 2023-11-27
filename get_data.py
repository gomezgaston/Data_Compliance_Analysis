#import libraries
import requests
import pandas as pd
import json
import numpy as np
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

#naming columns
df = pd.DataFrame(data["data"], columns=['id','id_case', 'country', 'authority', 'date', 
                                        'penalty_fee', 'subjet','subjet_industry', 'law', 
                                        'summary_law', 'summary_case', 'court_file', 'see_more'])

#parsing data
df['country'] = df['country'].apply(lambda x: country_parser(x))
df['court_file'] = df['court_file'].apply(lambda x: link_parser(x))
df.drop(columns=["see_more", "id"], inplace=True)


#transforming data
df["date"] = df['date'].replace("Unknown",np.nan).astype('category').fillna(method='ffill')

df['penalty_fee'].replace(['Only intention to issue fine', 
                           'Unknown',
                           'Fine in three-digit amount',
                           'Fine in six-digit amount',
                           'Fine in four-digit amount',
                           'Fine in five-digit amount',
                           'Fine amount between EUR 50 and EUR 800',
                           'Fine amount between EUR 50 and EUR 100',
                           'Fine amount between EUR 400 and EUR 600',
                           'Fine amount between EUR 350 and EUR 1000',
                           'Fine amount between EUR 300 and EUR 400',
                           'Fine amount between EUR 200 and EUR 1000',
                           'Fine amount between EUR 100 and EUR 1,000',],
                          [0,np.nan, 500, 500000, 5000, 50000,400,75,500,600,350,500,500], inplace=True)

df['penalty_fee'] = df['penalty_fee'].str.replace(',', '', regex=True).astype('float32')

df.to_excel('clean_data.xlsx', index=False)




url = "https://sheets.googleapis.com/v4/spreadsheets/1ssr92BY3h4nBTEaCsdaXTsZByr0W01uHvXvgpr-Yzyk/values/Hoja%202?alt=json&key=AIzaSyCq2wEEKL9-6RmX-TkW23qJsrmnFHFf5tY"


response = requests.get(url)

data = json.loads(response.text)

df = pd.DataFrame(data["values"], columns=["Tipo", "Numero", "Descripcion", "Categoria", "Estado", "Texto", "Misc", "Fecha"])

df.drop(columns=["Misc"], inplace=True)

df = df[df.iloc[:, 3] == 'Datos Personales']

df = df[df.iloc[:, 0] == 'Resolución']

df = df[df.iloc[:, 2].str.startswith("Apl")].reset_index()

df['Monto'] = df['Descripcion'].astype(str).str.extract(r'\$\s*([0-9,.]+)')

df.dropna(inplace=True)

df['Monto'] = df['Monto'].str.replace('.', '').str.replace(',', '.') 

df['Estado'] = df['Estado'].str.capitalize().str.strip()


df.to_csv("clean_data_arg.csv")


df.to_csv("clean_data_arg.csv")