import warnings
warnings.filterwarnings('ignore')  # Hide warnings
import datetime as dt
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import plotly.express as px

start = dt.datetime.now() - dt.timedelta(days=180)
end = dt.datetime.now()

#btc
btc = web.DataReader("BTC-USD", 'yahoo', start, end)  # Collects data
btc.reset_index(inplace=True)
crypto = btc[['Date','Adj Close']]
crypto = crypto.rename(columns = {'Adj Close':'BTC'})
crypto[ 'BTC_7DAY_MA' ] = crypto.BTC.rolling( 7).mean()

#eth
eth = web.DataReader("ETH-USD", 'yahoo', start, end)  # Collects data
eth.reset_index(inplace=True)
crypto["ETH"]= eth["Adj Close"]
crypto[ 'ETH_7DAY_MA' ] = crypto.ETH.rolling( 7).mean()

#sol
sol = web.DataReader("SOL-USD", 'yahoo', start, end)  # Collects data
sol.reset_index(inplace=True)
crypto["SOL"]= sol["Adj Close"]
crypto[ 'SOL_7DAY_MA' ] = crypto.SOL.rolling( 7).mean()

#AVAX
AVAX = web.DataReader("AVAX-USD", 'yahoo', start, end)  # Collects data
AVAX.reset_index(inplace=True)
crypto["AVAX"]= AVAX["Adj Close"]
crypto[ 'AVAX_7DAY_MA' ] = crypto.AVAX.rolling( 7).mean()

#FTM
FTM = web.DataReader("FTM-USD", 'yahoo', start, end)  # Collects data
FTM.reset_index(inplace=True)
crypto["FTM"]= FTM["Adj Close"]
crypto[ 'FTM_7DAY_MA' ] = crypto.FTM.rolling( 7).mean()

#BNB
BNB = web.DataReader("BNB-USD", 'yahoo', start, end)  # Collects data
BNB.reset_index(inplace=True)
crypto["BNB"]= BNB["Adj Close"]
crypto[ 'BNB_7DAY_MA' ] = crypto.BNB.rolling( 7).mean()

#MATIC
MATIC = web.DataReader("MATIC-USD", 'yahoo', start, end)  # Collects data
MATIC.reset_index(inplace=True)
crypto["MATIC"]= MATIC["Adj Close"]
crypto[ 'MATIC_7DAY_MA' ] = crypto.MATIC.rolling( 7).mean()

#ADA
ADA = web.DataReader("ADA-USD", 'yahoo', start, end)  # Collects data
ADA.reset_index(inplace=True)
crypto["ADA"]= ADA["Adj Close"]
crypto[ 'ADA_7DAY_MA' ] = crypto.ADA.rolling( 7).mean()

#AAVE
AAVE = web.DataReader("AAVE-USD", 'yahoo', start, end)  # Collects data
AAVE.reset_index(inplace=True)
crypto["AAVE"]= AAVE["Adj Close"]
crypto[ 'AAVE_7DAY_MA' ] = crypto.AAVE.rolling( 7).mean()

#CRV
CRV = web.DataReader("CRV-USD", 'yahoo', start, end)  # Collects data
CRV.reset_index(inplace=True)
crypto["CRV"]= CRV["Adj Close"]
crypto[ 'CRV_7DAY_MA' ] = crypto.CRV.rolling( 7).mean()

#BIFI
BIFI = web.DataReader("BIFI-USD", 'yahoo', start, end)  # Collects data
BIFI.reset_index(inplace=True)
crypto["BIFI"]= BIFI["Adj Close"]
crypto[ 'BIFI_7DAY_MA' ] = crypto.BIFI.rolling( 7).mean()

#ONE
ONE = web.DataReader("ONE-USD", 'yahoo', start, end)  # Collects data
ONE.reset_index(inplace=True)
crypto["ONE"]= ONE["Adj Close"]
crypto[ 'ONE_7DAY_MA' ] = crypto.ONE.rolling( 7).mean()

#LUNA
LUNA = web.DataReader("LUNA-USD", 'yahoo', start, end)  # Collects data
LUNA.reset_index(inplace=True)
crypto["LUNA"]= LUNA["Adj Close"]
crypto[ 'LUNA_7DAY_MA' ] = crypto.LUNA.rolling( 7).mean()

#CRO
CRO = web.DataReader("CRO-USD", 'yahoo', start, end)  # Collects data
CRO.reset_index(inplace=True)
crypto["CRO"]= CRO["Adj Close"]
crypto[ 'CRO_7DAY_MA' ] = crypto.CRO.rolling( 7).mean()

#ATOM
ATOM = web.DataReader("ATOM-USD", 'yahoo', start, end)  # Collects data
ATOM.reset_index(inplace=True)
crypto["ATOM"]= ATOM["Adj Close"]
crypto[ 'ATOM_7DAY_MA' ] = crypto.ATOM.rolling( 7).mean()

#MOVR
MOVR = web.DataReader("MOVR-USD", 'yahoo', start, end)  # Collects data
MOVR.reset_index(inplace=True)
crypto["MOVR"]= MOVR["Adj Close"]
crypto[ 'MOVR_7DAY_MA' ] = crypto.MOVR.rolling( 7).mean()

#NEAR
NEAR = web.DataReader("NEAR-USD", 'yahoo', start, end)  # Collects data
NEAR.reset_index(inplace=True)
crypto["NEAR"]= NEAR["Adj Close"]
crypto[ 'NEAR_7DAY_MA' ] = crypto.NEAR.rolling( 7).mean()

crypto.set_index("Date", inplace=True)
df = pd.DataFrame(crypto[['BTC', 'ETH', 'SOL', 'AVAX', 'FTM', 'BNB', 'MATIC', 'ADA', 'AAVE', 'CRV', 'BIFI', 'ONE', 'LUNA', 'CRO', 'ATOM', 'MOVR', 'NEAR']].corr())

df.to_csv(r'Z:\Python\DeFI\correlations_6m.csv', index=True)

# plt.figure(figsize = (10,10))
# print(sns.heatmap(crypto[['BTC', 'ETH', 'SOL', 'AVAX', 'FTM', 'BNB', 'MATIC', 'ADA', 'AAVE', 'CRV']].corr(),annot=True, cmap='Blues'))