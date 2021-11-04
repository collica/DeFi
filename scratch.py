from keys import *
from bscscan import BscScan
from pycoingecko import CoinGeckoAPI
from binance.client import Client
import pandas as pd
import requests
import defi.defi_tools as dft
import json
import csv

bsc = BscScan(bsc_key)
cg = CoinGeckoAPI()
client = Client(api_key, secret_key)

CAKE_BNB = '0x0eD7e52944161450477ee417DE9Cd3a859b14fD0'
CAKE = '0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82'
BNB = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'



CAKEBALANCE = bsc.get_acc_balance_by_token_contract_address(contract_address=CAKE, address=CAKE_BNB)
print('Contract Balance CAKE: ' + CAKEBALANCE)

BNBBALANCE = bsc.get_acc_balance_by_token_contract_address(contract_address=BNB, address=CAKE_BNB)
print('Contract Balance BNB: ' + BNBBALANCE)

total_supply_CAKE_BNB = float(bsc.get_total_supply_by_contract_address(contract_address=CAKE_BNB)) / 1000000000000000000
print('Total Supply CAKE_BNB: ' + str(total_supply_CAKE_BNB))



#trend reddit, coingecko, poocoin, telegram
#market cap
#circulating supply/total supply
#number of holders
#change in number of holders
#concentration in top accounts
#transactions/average transactions