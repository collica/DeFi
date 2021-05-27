import pandas as pd
import requests
import json

Prices = requests.get('https://farm.army/api/v0/prices')
Farms = requests.get('https://farm.army/api/v0/farms/0x71cb1790bff3ad5339982b91efc08ddca958de0c')


def GetKeySafely(dict, key1, key2):
    # returnString = ""
    # print(key1 + " searching")
    # print(key1)
    # print("in dict")
    # print(dict)
    key1Obj = dict.get(key1, "not available")
    # print('Key1OIbj::')
    # print(key1Obj)
    if key1Obj == "not available":
        returnString = "not available"
    else:
        returnString = key1Obj.get(key2, "not available")

    return returnString;

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

dictMaster = {}
count = 0
farmPrint = {}

# print(Platform)
for x in Platform:
    # tempDict = [500]
    tempDict = x['farms']
    count = count + 1

    for y in tempDict:
        deposit = y['deposit']['usd']
        farm = y.get('farm', "not available")
        tvl = farm.get('tvl', "not available")
        farmPrint = farm
        yieldsApy = GetKeySafely(farm, "yield", "apy")
        tvlUsd = GetKeySafely(farm, "tvl", "usd")
        # reward = GetKeySafely(y, "rewards", "usd")
        rewards = y.get('rewards', "not available")

        if rewards == "not available":
            reward = "not available"
        else:
            if not rewards:
                reward = "not available"
            else:
                reward = rewards[0].get('usd', "not available")
        dictMaster[count] = {
            'name': farm['name'],
            'yieldsApy': yieldsApy,
            'tvlUSD': tvlUsd,
            'reward': reward,
            'provider': y['farm']['provider'],
            'depositUSD': deposit
        }
        count = count + 1



print(dictMaster)
# print(farmPrint)
# for x in Platform:
#     tempDict = x['name']
#     dictMaster[count] = tempDict
#     count = count + 1
    # for y in tempDict:
        # dictMaster[count] = y
        # count = count + 1
        # temp = {}
        # temp = {
        #     "provider" : y['provider']
        # }
        # dictMaster[count] = temp
        # count = count + 1



# dictMaster = {}
# count = 0
#
# for x in dict2:
#     print(x['farm']['name'])
#     dictMaster[x['farm']['name']] = x['farm']['provider']
#     count = count + 1
#
# print('NEW DICT:')
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