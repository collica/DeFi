import requests
import pandas as pd

url = 'https://whattomine.com/coins/1.json?hr=1000.0&p=0.0&fee=0.0&cost=0.0&hcost=0.0&span_br=1h&span_d='

data = requests.get(url).json()
keys = dict.keys(data)
values = dict.values(data)

df = pd.DataFrame(zip(keys,values))
df.to_csv(r'Z:\Python\DeFI\sha256.csv', index=False)
#print(df)
