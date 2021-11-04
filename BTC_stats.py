from keys import *
import quandl
import pandas as pd
from functools import reduce

quandl.ApiConfig.api_key = quandlkey

price = quandl.get('BCHAIN/MKPRU').reset_index().rename(columns={'Date': 'Date', 'Value': 'BTC Price'})
mkt_cap = quandl.get('BCHAIN/MKTCP').reset_index().rename(columns={'Date': 'Date', 'Value': 'BTC Market Cap USD'})
exchange_USD_volume = quandl.get('BCHAIN/TRVOU').reset_index().rename(columns={'Date': 'Date', 'Value': 'Exchange Volume USD'})
est_transaction_vol_usd = quandl.get('BCHAIN/ETRVU').reset_index().rename(columns={'Date': 'Date', 'Value': 'Est Trans Vol USD'})
est_transaction_vol_btc = quandl.get('BCHAIN/ETRAV').reset_index().rename(columns={'Date': 'Date', 'Value': 'Est Trans Vol BTC'})
total_transaction_fees_USD = quandl.get('BCHAIN/TRFUS').reset_index().rename(columns={'Date': 'Date', 'Value': 'Total Transaction Fees USD'})
total_transaction_fees_BTC = quandl.get('BCHAIN/TRFEE').reset_index().rename(columns={'Date': 'Date', 'Value': 'Total Transaction Fees BTC'})
cost_percent_transaction_volume = quandl.get('BCHAIN/CPTRV').reset_index().rename(columns={'Date': 'Date', 'Value': 'Cost % of Transaction Volume'})
network_hash_rate = quandl.get('BCHAIN/HRATE').reset_index().rename(columns={'Date': 'Date', 'Value': 'Network Hashrate'})
difficulty = quandl.get('BCHAIN/DIFF').reset_index().rename(columns={'Date': 'Date', 'Value': 'Difficulty'})
network_deficit = quandl.get('BCHAIN/NETDF').reset_index().rename(columns={'Date': 'Date', 'Value': 'Network Deficit'})
btc_number_trans_block = quandl.get('BCHAIN/NTRBL').reset_index().rename(columns={'Date': 'Date', 'Value': 'Bitcoin Total Transactions Per Block'})
avg_block_size = quandl.get('BCHAIN/AVBLS').reset_index().rename(columns={'Date': 'Date', 'Value': 'Avg Block Size'})
med_conf_time = quandl.get('BCHAIN/ATRCT').reset_index().rename(columns={'Date': 'Date', 'Value': 'Median Confirmation Time'})
blockchain_size = quandl.get('BCHAIN/BLCHS').reset_index().rename(columns={'Date': 'Date', 'Value': 'Blockchain Size'})
miners_revenue = quandl.get('BCHAIN/MIREV').reset_index().rename(columns={'Date': 'Date', 'Value': 'Miner Revenue'})
miners_op_margin = quandl.get('BCHAIN/MIOPM').reset_index().rename(columns={'Date': 'Date', 'Value': 'Miner Margin'})
number_wallets = quandl.get('BCHAIN/MWNUS').reset_index().rename(columns={'Date': 'Date', 'Value': 'Total Wallets'})
unique_addresses_used = quandl.get('BCHAIN/NADDU').reset_index().rename(columns={'Date': 'Date', 'Value': 'Unique Addresses Used'})
number_transactions = quandl.get('BCHAIN/NTRAN').reset_index().rename(columns={'Date': 'Date', 'Value': 'Number Transactions'})
number_transactions_excl_pop_addresses = quandl.get('BCHAIN/NTREP').reset_index().rename(columns={'Date': 'Date', 'Value': 'Number Transactions Excl Popular Addresses'})
cumulative_transactions = quandl.get('BCHAIN/NTRAT').reset_index().rename(columns={'Date': 'Date', 'Value': 'Cumulative Transactions'})
btc_total_output_vol = quandl.get('BCHAIN/TOUTV').reset_index().rename(columns={'Date': 'Date', 'Value': 'Bitcoin Total Output Volume'})
btc_circulating = quandl.get('BCHAIN/TOTBC').reset_index().rename(columns={'Date': 'Date', 'Value': 'BTC Circulating'})

data_frames = [price, mkt_cap, exchange_USD_volume, est_transaction_vol_usd, est_transaction_vol_btc, total_transaction_fees_USD, total_transaction_fees_BTC, cost_percent_transaction_volume,
               network_hash_rate, difficulty, network_deficit, btc_number_trans_block, avg_block_size, med_conf_time, blockchain_size, miners_revenue, miners_op_margin, number_wallets, unique_addresses_used,
               number_transactions, number_transactions_excl_pop_addresses, cumulative_transactions, btc_total_output_vol, btc_circulating]

merged = reduce(lambda left, right: pd.merge(left, right, on=['Date'], how='outer'), data_frames)
merged.to_csv(r'Z:\Python\DeFI\blockchain_stats.csv', index=False)
print(merged)


# Exhausive List
# bitcoin market price USD
# bitcoin USD exchange trade volume
# bitcoin difficulty
# bitcoin wallet number of users
# bitcoin average block size
# bitcoin blockchain size
# bitcoin median transaction confirmation time
# bitcoin miners revenue
# bitcoin hash rate
# bitcoin cost per transaction
# bitcoin cost % of transaction volume
# bitcoin estimated transaction volume USD
# bitcoin estimated transaction volume
# bitcoin total output volume
# bitcoin number of transactions per block
# bitcoin number of unique addresses used
# bitcoin total number of transactions
# bitcoin number of transactions
# bitcoin total transaction fees USD
# bitcoin total transaction fees
# bitcoin market cap
# total bitcoins
# bitcoin number of transactions per day
# bitcoin transaction volume
# bitcoin days destroyed
# bitcoin days destroyed cumulative
# bitcoin trade volume vs transaction volume ratio
# bitcoin network deficit
# bitcoin mining operating margin

