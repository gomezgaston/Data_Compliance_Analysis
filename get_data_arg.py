import requests
import json
import pandas as pd


url = "https://sheets.googleapis.com/v4/spreadsheets/1ssr92BY3h4nBTEaCsdaXTsZByr0W01uHvXvgpr-Yzyk/values/Hoja%202?alt=json&key=AIzaSyCq2wEEKL9-6RmX-TkW23qJsrmnFHFf5tY"


response = requests.get(url)

data = json.loads(response.text)

df = pd.DataFrame(data["values"], columns=["Tipo", "Numero", "Descripcion", "Categoria", "Estado", "Texto", "Misc", "Fecha"])

df.drop(columns=["Misc"], inplace=True)

df = df[df.iloc[:, 3] == 'Datos Personales']

df = df[df.iloc[:, 0] == 'Resolución']

df = df[df.iloc[:, 2].str.startswith("Apl")].reset_index()

df['Monto'] = df['Descripcion'].str.extract(r'\$\s*([0-9,.]+)').replace('[\.,]', '', regex=True).astype(float)

df.dropna(inplace=True)


df.to_csv("clean_data_arg.csv")