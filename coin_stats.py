from keys import *
from bscscan import BscScan

btc = ''
bsc = BscScan(bsc_key)
ada = ''
eth = ''
sol = ''

bnb_circulating = bsc.get_circulating_supply_by_contract_address(contract_address='0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c')
bnb_total = bsc.get_total_supply_by_contract_address(contract_address='0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c')

print(bnb_circulating)
print(bnb_total)