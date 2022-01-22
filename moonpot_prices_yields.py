import requests
import pandas as pd

url = 'https://api.moonpot.com/apy'

data = pd.DataFrame(requests.get(url).json()['data']).transpose()
data.to_csv(r'Z:\Python\DeFI\moonpot_prices_yields.csv', index=False)
#print(data)