import requests
from requests import Session
from keys import cmc
import pandas as pd

symbols = ['BTC,ETH,BNB,MATIC,FTM,KDA,AVAX,CKB,HNT,AETH,HNS,DOGE,LTC,ATOM,ALGO,DOT,HEC,WSHEC,TIME,SOL,ONE,WAGMI,mSOL']

parameters = {
  'symbol': symbols,
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': cmc,
}

session = Session()
session.headers.update(headers)

quotes_dict = session.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest', params=parameters).json()['data']

keys = list(dict.keys(quotes_dict))
name_list = []
price_list = []
circulating_supply_list = []
total_supply_list = []
max_supply_list = []
mkt_cap_list = []
diluted_cap_list = []

for x in keys:
    name = quotes_dict[x]['name']
    price = quotes_dict[x]['quote']['USD']['price']
    circulating = quotes_dict[x]['circulating_supply']
    total = quotes_dict[x]['total_supply']
    max = quotes_dict[x]['max_supply']
    mktcap = quotes_dict[x]['quote']['USD']['market_cap']
    diluted = quotes_dict[x]['quote']['USD']['fully_diluted_market_cap']

    name_list.append(name)
    price_list.append(price)
    circulating_supply_list.append(circulating)
    total_supply_list.append(total)
    max_supply_list.append(max)
    mkt_cap_list.append(mktcap)
    diluted_cap_list.append(diluted)

df = pd.DataFrame(list(zip(keys, name_list, price_list, circulating_supply_list, total_supply_list, max_supply_list, mkt_cap_list, diluted_cap_list)), columns=['Symbol', 'Name', 'Price', 'Circulating Supply', 'Total Supply', 'Max Supply', 'Market Cap', 'Fully Diluted Market Cap'])
df.to_csv(r'Z:\Python\DeFI\cmc.csv', index=False)
#print(df)






