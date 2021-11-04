import pandas as pd
from keys import _0x_wallet
from web3 import Web3
from bscscan import BscScan
import requests
import json

bsc = BscScan()

wallet = Web3.toChecksumAddress(_0x_wallet)

bsc_web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
ftm_web3 = Web3(Web3.HTTPProvider('https://rpcapi.fantom.network'))
avax_web3 = Web3(Web3.HTTPProvider('https://api.avax.network/ext/bc/C/rpc'))
poly_web3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))
arb_web3 = Web3(Web3.HTTPProvider('https://arb1.arbitrum.io/rpc'))

bsc_tokens = [
    '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c' #BNB
    #'0x55d398326f99059ff775485246999027b3197955' #USDT
                ]

















ftm_tokens = [
    '0x21be370d5312f44cb42ce377bc9b8a0cef1a4c83' #FTM
    #'0xd67de0e0a0fd7b15dc8348bb9be742f3c5850454' #BNB
                ]

avax_tokens = [
    '0x264c1383EA520f73dd837F915ef3a732e204a493' #BNB
    '0x49D5c2BdFfac6CE2BFdB6640F4F80f226bc10bAB' #ETH
                ]

poly_tokens = [
    '0x7ceb23fd6bc0add59e62ac25578270cff1b9f619' #ETH
    #'0x8f3cf7ad23cd3cadbd9735aff958023239c6a063' #DAI
    #'0x0000000000000000000000000000000000001010' #MATIC
                ]

arb_tokens = [
    '' #
                ]

