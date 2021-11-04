import requests
import pandas as pd

#Beefy Docs
#https://github.com/beefyfinance/beefy-api

token_prices_url = 'https://api.beefy.finance/prices'
lp_prices_url = 'https://api.beefy.finance/lps'
yields_url = 'https://api.beefy.finance/apy' #this is being deprecated, check for /apy/breakdown
vaults_url = 'https://api.beefy.finance/vaults'

token_prices = requests.get(token_prices_url).json()
price_frame = pd.DataFrame(token_prices.items(), columns=['Symbol', 'Price'])
price_frame.to_csv(r'Z:\Python\DeFI\beefy_prices.csv', index=False)
#print(price_frame)

lp_prices = requests.get(lp_prices_url).json()
lp_frame = pd.DataFrame(lp_prices.items(), columns=['Beefy Symbol', 'Price'])
lp_frame.to_csv(r'Z:\Python\DeFI\beefy_lp_prices.csv', index=False)
#print(lp_frame)

yields = requests.get(yields_url).json()
yield_frame = pd.DataFrame(yields.items(), columns=['Beefy Symbol', 'Yield'])
yield_frame.to_csv(r'Z:\Python\DeFI\beefy_yields.csv', index=False)
#print(yield_frame)

vaults = requests.get(vaults_url).json()
vaults_frame = pd.DataFrame(vaults)
vaults_frame.to_csv(r'Z:\Python\DeFI\beefy_vaults.csv', index=False)
#print(vaults_frame)