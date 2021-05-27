import pandas as pd
import requests
import json

Prices = requests.get('https://farm.army/api/v0/prices')
Farms = requests.get('https://farm.army/api/v0/farms/0x71cb1790bff3ad5339982b91efc08ddca958de0c')

#PriceFrame = pd.DataFrame.transpose(pd.json_normalize(json.loads(Prices.text)))
#print(PriceFrame)
#PriceFrame.to_csv(r'Z:\Python\DeFI\farmarmy_prices.csv')

RawFarmFrame = json.loads(Farms.content)
FarmSummary = pd.DataFrame(RawFarmFrame['platforms'])
#FarmSummary.to_csv(r'Z:\Python\DeFI\farmarmy_farm summary.csv')

Platform = (RawFarmFrame['platforms'])

Name = ((RawFarmFrame['platforms'][0]['farms'])[0]['farm'])['name']

dict1 = (RawFarmFrame['platforms'][0]['farms'])[0]['farm']

dict2 = (RawFarmFrame['platforms'][0]['farms'])

keys = dict1.keys()
keys2 = dict2
values = dict1.values()
items = dict1.items()

# print(keys)
# print(values)
# print(items)

dictMaster = {}
count = 0

print(Platform)
for x in Platform['farms']:
    for y in x['farm']:
        dictMaster[y['name']] = y['provider']

# dictMaster = {}
# count = 0
#
# for x in dict2:
#     print(x['farm']['name'])
#     dictMaster[x['farm']['name']] = x['farm']['provider']
#     count = count + 1
#
# print('NEW DICT:')
print(dictMaster)
#
#
# Deposit = ((RawFarmFrame['platforms'][0]['farms'])[0]['deposit'])['usd']
# print(Deposit)
#
# Yield = ((RawFarmFrame['platforms'][0]['farms'])[0]['farm'])['yield']['apy']
# print(Yield)
#
# Rewards = ((RawFarmFrame['platforms'][0]['farms'])[0]['rewards'])[0]['usd']
# print(Rewards)
#
# TVL = ((RawFarmFrame['platforms'][0]['farms'])[0]['farm'])['tvl']['usd']
# print(TVL)


Headers = ['Name', 'Deposit', 'Yield', 'Rewards', 'TVL']
NameList = []
DepositList = []
RewardsList = []
TVLList = []

test = pd.DataFrame(list(zip(NameList, DepositList, RewardsList, TVLList)), columns = Headers)
#print(test)

#ApeSwap = pd.DataFrame(Farms)
#ApeSwap.to_csv(r'Z:\Python\DeFI\apeswap.csv')
#print(ApeSwap)