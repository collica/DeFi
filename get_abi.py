import pandas as pd
from keys import _0x_wallet
from keys import bsc_key
from web3 import Web3
from bscscan import BscScan
import requests
import json

bnb = float(BscScan(bsc_key).get_bnb_balance(address=_0x_wallet)) / (10**18)
ftm = float(requests.get('https://api.ftmscan.com/api?module=account&action=balance&address=0x71cb1790bff3ad5339982b91efc08ddca958de0c&tag=latest&apikey=V4IJCNYTZUA4D2FCDE49M97NRW28D32XAC').json()['result']) / (10**18)
avax = float(requests.get('https://api.snowtrace.io/api?module=account&action=balance&address=0x71cb1790bff3ad5339982b91efc08ddca958de0c&tag=latest&apikey=7I37TYGZE6ZAE37CQMN4GBS7YIBR6ZI45W').json()['result']) / (10**18)
poly = float(requests.get('https://api.polygonscan.com/api?module=account&action=balance&address=0x71cb1790bff3ad5339982b91efc08ddca958de0c&tag=latest&apikey=BEZ7P1BMPS56PHCFEB2PFR1G2XZ3UYAQSE').json()['result']) / (10**18)
aeth = float(requests.get('https://api.arbiscan.io/api?module=account&action=balance&address=0x71cb1790bff3ad5339982b91efc08ddca958de0c&tag=latest&apikey=EAC2828J6YXVHZBJEMGWC3F4U5PX2JMGZE').json()['result']) / (10**18)


