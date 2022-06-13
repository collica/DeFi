import pandas as pd
from keys import bnb_wallet
from keys import bsc_key
from web3 import Web3
from bscscan import BscScan
import requests
import json

bnb = float(BscScan(bsc_key).get_bnb_balance(address=bnb_wallet)) / (10**18)
ftm = float(requests.get('https://api.ftmscan.com/api?module=account&action=balance&address=0xb1f98275C4Ce37F5b180471d311828c420e1DE47&tag=latest&apikey=V4IJCNYTZUA4D2FCDE49M97NRW28D32XAC').json()['result']) / (10**18)
avax = float(requests.get('https://api.snowtrace.io/api?module=account&action=balance&address=0xd4De7994358473D1A91eF25b01908AF72fA6f5E0&tag=latest&apikey=7I37TYGZE6ZAE37CQMN4GBS7YIBR6ZI45W').json()['result']) / (10**18)
poly = float(requests.get('https://api.polygonscan.com/api?module=account&action=balance&address=0xD40929F2e989B0b2b83c873cffc735000885F480&tag=latest&apikey=BEZ7P1BMPS56PHCFEB2PFR1G2XZ3UYAQSE').json()['result']) / (10**18)
#aeth = float(requests.get('https://api.arbiscan.io/api?module=account&action=balance&address=0x71cb1790bff3ad5339982b91efc08ddca958de0c&tag=latest&apikey=EAC2828J6YXVHZBJEMGWC3F4U5PX2JMGZE').json()['result']) / (10**18)

payload = json.dumps({
  "jsonrpc": "2.0",
  "id": 1,
  "method": "hmyv2_getBalance",
  "params": [bnb_wallet]
})
headers = {
  'Content-Type': 'application/json'
}
one = float(requests.request("POST", "https://rpc.s0.t.hmny.io", headers=headers, data=payload).json()['result']) / (10**18)

symbols = ['BNB', 'FTM', 'AVAX', 'MATIC', 'ONE']
qty = [bnb, ftm, avax, poly, one]

df = pd.DataFrame(list(zip(symbols, qty)), columns=['Symbol', 'Qty'])
df.to_csv(r'Z:\Python\DeFI\gas_tokens.csv', index=False)
#print(df)
