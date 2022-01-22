import requests
from keys import crypto_quant_token
import pandas as pd

headers = {'Authorization': 'Bearer ' + crypto_quant_token}
url = "https://api.cryptoquant.com/v1/btc/network-data/fees?limit=100000"
result = requests.get(url, headers=headers).json()['result']['data']
df = pd.DataFrame(result)
df.to_csv(r'Z:\Python\DeFI\btc_network_fee.csv', index=False)
print(df)