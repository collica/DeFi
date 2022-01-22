import requests
import pandas as pd

doge_balance = requests.get('https://dogechain.info/api/v1/address/balance/DKJmLiotaQaTa7WEyxW9xezYgehDLPtmBW').json()['balance']
ltc_balance = requests.get('https://chainz.cryptoid.info/ltc/api.dws?q=getbalance&a=ltc1q4qyepm5wuagxx669vmsgj9t0nhu0syfsvtt0ky').json()

df = pd.DataFrame((doge_balance, ltc_balance)).transpose()
df.columns = ['DOGE', 'LTC']
df.to_csv(r'Z:\Python\DeFI\ltc_doge.csv', index=False)
#print(df)

# url = 'https://e.hnsfans.com/address/hs1qdvjml202vmt8gprs5ca7ux6zyuuvp7x4hjnuju'
# hns = requests.get(url).text
# print(hns)
