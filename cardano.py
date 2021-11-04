import requests
from keys import ada_wallet
import pandas as pd

raw = requests.get(f'https://api.blockchair.com/cardano/raw/address/{ada_wallet}').json()
balance = float(raw['data'][ada_wallet]['address']['caBalance']['getCoin'])/1000000
price = float(raw['context']['market_price_usd'])

df = pd.DataFrame([[balance, price]], columns=['Balance','Price'])
df.to_csv(r'Z:\Python\DeFI\cardano.csv', index=False)

