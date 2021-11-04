import requests
import json

prices = json.loads(requests.get('https://api.pancakeswap.info/api/tokens').content)
pairs = json.loads(requests.get('https://api.pancakeswap.info/api/pairs').content)

data = pairs['data']
keys = dict.keys(data)
#print(data)

baselist = []
quotelist = []
liquiditylist = []

for x in keys:
    liquidity = float(data[x]['liquidity'])
    liquiditylist.append(liquidity)

totalliquidity = sum(liquiditylist)
print('Total Pancakeswap Liquidity: ' + str(totalliquidity))





