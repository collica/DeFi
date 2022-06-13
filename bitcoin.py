import requests
import pandas as pd

balance = requests.get('https://api.blockcypher.com/v1/btc/main/addrs/bc1qpszyk7r82w9pvvxdtezplg9hlep532w2jc0303/full?limit=50').json()['balance'] / 100000000
df = pd.DataFrame([balance])
df.to_csv(r'Z:\Python\DeFI\Bitcoin.csv', index=False)
