from bscscan import BscScan
from pycoingecko import CoinGeckoAPI
import pandas as pd
import defi.defi_tools as dft

bsc = BscScan('INBSQ8WQ1IJB1UGZHNB6H4KMSV5Q983N8U')
cg = CoinGeckoAPI()

trending = pd.DataFrame(cg.get_search_trending()['coins'])['item']
trending.to_csv(r'Z:\Python\DeFI\cg_trending.csv')
print(trending)