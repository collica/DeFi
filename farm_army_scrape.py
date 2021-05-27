import pandas as pd
import requests
import json

Prices = requests.get('https://farm.army/api/v0/prices')
Farms = requests.get('https://farm.army/api/v0/farms/0x71cb1790bff3ad5339982b91efc08ddca958de0c')

PriceFrame = pd.DataFrame.transpose(pd.json_normalize(json.loads(Prices.text)))
PriceFrame.to_csv(r'Z:\Python\DeFI\farmarmy_prices.csv')

RawFarmFrame = json.loads(Farms.content)
Platform = (RawFarmFrame['platforms'])
Name = ((RawFarmFrame['platforms'][0]['farms'])[0]['farm'])['name']

def GetKeySafely(dict, key1, key2):
    key1Obj = dict.get(key1, "not available")
    if key1Obj == "not available":
        returnString = "not available"
    else:
        returnString = key1Obj.get(key2, "not available")

    return returnString

dictMaster = {}
count = 0
farmPrint = {}

for x in Platform:
    tempDict = x['farms']
    count = count + 1

    for y in tempDict:
        deposit = y['deposit']['usd']
        farm = y.get('farm', "not available")
        tvl = farm.get('tvl', "not available")
        farmPrint = farm
        yieldsApy = GetKeySafely(farm, "yield", "apy")
        tvlUsd = GetKeySafely(farm, "tvl", "usd")
        rewards = y.get('rewards', "not available")

        if rewards == "not available":
            reward = "not available"
        else:
            if not rewards:
                reward = "not available"
            else:
                reward = rewards[0].get('usd', "not available")
        dictMaster[count] = {
            'provider': y['farm']['provider'],
            'name': farm['name'],
            'yieldsApy': yieldsApy,
            'tvlUSD': tvlUsd,
            'depositUSD': deposit,
            'reward': reward,
        }
        count = count + 1

FinalFrame = pd.DataFrame(dictMaster).transpose()
FinalFrame.to_csv(r'Z:\Python\DeFI\farm_master.csv')
print(FinalFrame)