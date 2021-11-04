import requests
import pandas as pd

balance = requests.request("GET", "https://api.helium.io/v1/accounts/13o2GPssGJncvv1P8G5gVjrNnpoKXynwAzpRKJbEExEmqXbmXB6").json()['data']['balance']/100000000
price = requests.request("GET", 'https://api.helium.io/v1/oracle/prices/current').json()['data']['price']/100000000

df = pd.DataFrame([[balance, price]], columns=['Balance','Price'])
df.to_csv(r'Z:\Python\DeFI\helium.csv', index=False)

