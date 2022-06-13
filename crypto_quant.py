import requests
from keys import crypto_quant_token
import pandas as pd
from functools import reduce

headers = {'Authorization': 'Bearer ' + crypto_quant_token}

test = pd.DataFrame(requests.get('https://api.cryptoquant.com/v1/btc/network-data/fees_reward_percent', headers=headers).json()['result']['data'])
Network_Hashrate_df = pd.DataFrame(requests.get('https://api.cryptoquant.com/v1/btc/network-data/hashrate', headers=headers).json()['result']['data'])
Difficulty_df = pd.DataFrame(requests.get('https://api.cryptoquant.com/v1/btc/network-data/difficulty', headers=headers).json()['result']['data'])
Net_Miner_Position_df = pd.DataFrame(requests.get('https://api.cryptoquant.com/v1/btc/flow-indicator/mpi', headers=headers).json()['result']['data'])
Miner_Reserves_df = pd.DataFrame(requests.get('https://api.cryptoquant.com/v1/btc/miner-flows/reserve?miner=all_miner', headers=headers).json()['result']['data'])

frames = [Network_Hashrate_df, Difficulty_df, Net_Miner_Position_df, Miner_Reserves_df]

Master_df = reduce(lambda left, right: pd.merge(left, right, on=['date'], how='outer'), frames)
Master_df.columns = ['Date', 'Network Hashrate', 'Difficulty', 'Net Miner Position', 'Miner Reserves BTC', 'Miner Reserves USD']

Master_df.to_csv(r'Z:\Python\DeFI\Crypto_Quant_Data.csv', index=False)
print(Master_df)

print(test)
