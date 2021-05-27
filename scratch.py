from Keys import *
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

#quotes = pd.DataFrame(client.get_orderbook_tickers())
#print(quotes)
#quotes.to_csv('binance_snap_quotes.csv', index=False, header=True)

CAKE_BNB = '0x0eD7e52944161450477ee417DE9Cd3a859b14fD0'

CAKEBALANCE = bsc.get_acc_balance_by_token_contract_address(contract_address='0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82', address=CAKE_BNB)
print('Contract Balance CAKE: ' + CAKEBALANCE)

#CAKELAST = dft.geckoPrice('bitcoin', 'usd')
#print(CAKELAST)

BNBBALANCE = bsc.get_acc_balance_by_token_contract_address(contract_address='0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c', address=CAKE_BNB)
print('Contract Balance BNB: ' + BNBBALANCE)

total_supply_CAKE_BNB = float(bsc.get_total_supply_by_contract_address(contract_address=CAKE_BNB)) / 1000000000000000000
print('Total Supply CAKE_BNB: ' + str(total_supply_CAKE_BNB))


#if __name__ == '__main__':
    #print('Total Supply CAKE_BNB: ' + total_supply_CAKE_BNB)
    #print('Total Supply CAKE_HOTCROSS: ' + total_supply_CAKE_HOTCROSS)
    #print('Total Supply BANANA_BNB: ' + total_supply_BANANA_BNB)
    #print('My Balance: ' + str(mybalancebnb))

#pancakepairs = dft.pcsPairs(as_df=True)
#pancakepairs.to_csv(r'Z:\Python\DeFI\pancakepairs.csv')

#pancakeprices = dft.pcsTokens()
#pancakeprices.to_csv(r'Z:\Python\DeFI\pancakeprices.csv')

#trend reddit, coingecko, poocoin, telegram
#market cap
#circulating supply/total supply
#number of holders
#change in number of holders
#concentration in top accounts
#transactions/average transactions