import pandas as pd
from keys import bnb_wallet
from keys import avax_wallet
from keys import ftm_wallet
from keys import matic_wallet
from keys import one_wallet
from web3 import Web3
from bscscan import BscScan
import requests
import json

bnb_checksum = Web3.toChecksumAddress(bnb_wallet)
avax_checksum = Web3.toChecksumAddress(avax_wallet)
ftm_checksum = Web3.toChecksumAddress(ftm_wallet)
matic_checksum = Web3.toChecksumAddress(matic_wallet)
one_checksum = Web3.toChecksumAddress(one_wallet)

bsc_web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed3.binance.org/'))
ftm_web3 = Web3(Web3.HTTPProvider('https://rpcapi.fantom.network'))
avax_web3 = Web3(Web3.HTTPProvider('https://api.avax.network/ext/bc/C/rpc'))
poly_web3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))
arb_web3 = Web3(Web3.HTTPProvider('https://arb1.arbitrum.io/rpc'))
one_web3 = Web3(Web3.HTTPProvider('https://api.harmony.one'))

beefy_bsc_abi = json.loads('[{"inputs":[{"internalType":"contract IStrategy","name":"_strategy","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint256","name":"_approvalDelay","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"implementation","type":"address"}],"name":"NewStratCandidate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"implementation","type":"address"}],"name":"UpgradeStrat","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"approvalDelay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"available","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"balance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"depositAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"earn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getPricePerFullShare","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"inCaseTokensGetStuck","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_implementation","type":"address"}],"name":"proposeStrat","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"stratCandidate","outputs":[{"internalType":"address","name":"implementation","type":"address"},{"internalType":"uint256","name":"proposedTime","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"strategy","outputs":[{"internalType":"contract IStrategy","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"upgradeStrat","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"want","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_shares","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdrawAll","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
beefy_ftm_abi = json.loads('[{\"inputs\":[{\"internalType\":\"contract IStrategy\",\"name\":\"_strategy\",\"type\":\"address\"},{\"internalType\":\"string\",\"name\":\"_name\",\"type\":\"string\"},{\"internalType\":\"string\",\"name\":\"_symbol\",\"type\":\"string\"},{\"internalType\":\"uint256\",\"name\":\"_approvalDelay\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"Approval\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"implementation\",\"type\":\"address\"}],\"name\":\"NewStratCandidate\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"previousOwner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"OwnershipTransferred\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"Transfer\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"implementation\",\"type\":\"address\"}],\"name\":\"UpgradeStrat\",\"type\":\"event\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"}],\"name\":\"allowance\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"approvalDelay\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"approve\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"available\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"balance\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"}],\"name\":\"balanceOf\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"decimals\",\"outputs\":[{\"internalType\":\"uint8\",\"name\":\"\",\"type\":\"uint8\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"subtractedValue\",\"type\":\"uint256\"}],\"name\":\"decreaseAllowance\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"}],\"name\":\"deposit\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"depositAll\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"earn\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"getPricePerFullShare\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"}],\"name\":\"inCaseTokensGetStuck\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"addedValue\",\"type\":\"uint256\"}],\"name\":\"increaseAllowance\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"name\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"owner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_implementation\",\"type\":\"address\"}],\"name\":\"proposeStrat\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"stratCandidate\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"implementation\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"proposedTime\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"strategy\",\"outputs\":[{\"internalType\":\"contract IStrategy\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"symbol\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"totalSupply\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"recipient\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"transfer\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"sender\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"recipient\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"transferFrom\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"transferOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"upgradeStrat\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"want\",\"outputs\":[{\"internalType\":\"contract IERC20\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"_shares\",\"type\":\"uint256\"}],\"name\":\"withdraw\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"withdrawAll\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"}]')
beefy_avax_abi = json.loads('[{"type":"constructor","stateMutability":"nonpayable","inputs":[{"type":"address","name":"_strategy","internalType":"contract IStrategy"},{"type":"string","name":"_name","internalType":"string"},{"type":"string","name":"_symbol","internalType":"string"},{"type":"uint256","name":"_approvalDelay","internalType":"uint256"}]},{"type":"event","name":"Approval","inputs":[{"type":"address","name":"owner","internalType":"address","indexed":true},{"type":"address","name":"spender","internalType":"address","indexed":true},{"type":"uint256","name":"value","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"NewStratCandidate","inputs":[{"type":"address","name":"implementation","internalType":"address","indexed":false}],"anonymous":false},{"type":"event","name":"OwnershipTransferred","inputs":[{"type":"address","name":"previousOwner","internalType":"address","indexed":true},{"type":"address","name":"newOwner","internalType":"address","indexed":true}],"anonymous":false},{"type":"event","name":"Transfer","inputs":[{"type":"address","name":"from","internalType":"address","indexed":true},{"type":"address","name":"to","internalType":"address","indexed":true},{"type":"uint256","name":"value","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"UpgradeStrat","inputs":[{"type":"address","name":"implementation","internalType":"address","indexed":false}],"anonymous":false},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"allowance","inputs":[{"type":"address","name":"owner","internalType":"address"},{"type":"address","name":"spender","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"approvalDelay","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"approve","inputs":[{"type":"address","name":"spender","internalType":"address"},{"type":"uint256","name":"amount","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"available","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"balance","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"balanceOf","inputs":[{"type":"address","name":"account","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint8","name":"","internalType":"uint8"}],"name":"decimals","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"decreaseAllowance","inputs":[{"type":"address","name":"spender","internalType":"address"},{"type":"uint256","name":"subtractedValue","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"deposit","inputs":[{"type":"uint256","name":"_amount","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"depositAll","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"earn","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"getPricePerFullShare","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"inCaseTokensGetStuck","inputs":[{"type":"address","name":"_token","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"increaseAllowance","inputs":[{"type":"address","name":"spender","internalType":"address"},{"type":"uint256","name":"addedValue","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"name","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"owner","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"proposeStrat","inputs":[{"type":"address","name":"_implementation","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"renounceOwnership","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"implementation","internalType":"address"},{"type":"uint256","name":"proposedTime","internalType":"uint256"}],"name":"stratCandidate","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"contract IStrategy"}],"name":"strategy","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"symbol","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"totalSupply","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"transfer","inputs":[{"type":"address","name":"recipient","internalType":"address"},{"type":"uint256","name":"amount","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"transferFrom","inputs":[{"type":"address","name":"sender","internalType":"address"},{"type":"address","name":"recipient","internalType":"address"},{"type":"uint256","name":"amount","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"transferOwnership","inputs":[{"type":"address","name":"newOwner","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"upgradeStrat","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"contract IERC20"}],"name":"want","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"withdraw","inputs":[{"type":"uint256","name":"_shares","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"withdrawAll","inputs":[]}]')
beefy_poly_abi = json.loads('[{"inputs":[{"internalType":"contract IStrategy","name":"_strategy","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint256","name":"_approvalDelay","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"implementation","type":"address"}],"name":"NewStratCandidate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"implementation","type":"address"}],"name":"UpgradeStrat","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"approvalDelay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"available","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"balance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"depositAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"earn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getPricePerFullShare","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"inCaseTokensGetStuck","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_implementation","type":"address"}],"name":"proposeStrat","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"stratCandidate","outputs":[{"internalType":"address","name":"implementation","type":"address"},{"internalType":"uint256","name":"proposedTime","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"strategy","outputs":[{"internalType":"contract IStrategy","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"upgradeStrat","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"want","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_shares","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdrawAll","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
#beefy_arb_abi = json.loads('')

beefy_bsc_contracts = [
    '0xd411121c948cff739857513e1adf25ed448623f8', #belt btc
    '0xf2064c230b285aa6cf45c6267da86a8e3505d0aa', #belt eth
    '0x15396d3bd9338a14ae90613fc2b85c5f7b5621cf', #banana-bnb
    '0x651b496bce2c184282a2b9aef3f8badbac36dd7f', #banana-busd
    '0xb26642b6690e4c4c9a6dad6115ac149c700c7dfe', #cake-bnb
    '0x190dd361ee7edb1801d66e9e957c5cdf1e7be75b', #belt-bnb
    '0xc259D613510A70A92DcDd43F8ecED2F2143758cE', #eth-bnb
    '0xb8e6a5edbc8ae71f74fd02f65e95ba0a8733c5a1', #ada-bnb
    '0x97697d89e490196ee7dbf6660424b80d276ae7d9', #avax-bnb
    '0xd6d138fb65c2a68e728d70efbaa54c794b73b6a0', #ada-eth
    '0xb61fa9e4548f0d3e1405cfba7a12de8ff11c0e4b', #ftm-bnb
    '0x59960d624600ae1669584bb504a5f4f2e90ebf46', #bifi-bnb pcs
    '0x6eba4a31c46937b42e66f44a0a1165a08495a38f', #bifi-bnb apeswap

                ]

beefy_ftm_contracts = [
    '0xEe3a7c885Fd3cc5358FF583F2DAB3b8bC473316f', #boo-ftm
    '0xa3e3af161943cfb3941b631676134bb048739727', #btc-ftm
    '0x2a30c5e0d577108f694d2a96179cd73611ee069b', #eth-ftm
    '0x41d44b276904561ac51855159516fd4cb2c90968', #ftm-usdc
    '0x5d89017d2465115007aba00da1e6446df2c19f34', #usdt-ftm
    '0x0a03d2c1cfca48075992d810cc69bd9fe026384a', #scream eth
    '0x49c68eDb7aeBd968F197121453e41b8704AcdE0C', #scream ftm
    '0x97927abfe1abbe5429cbe79260b290222fc9fbba', #scream btc
    '0xf782e675b93d22fd810dca4149d29ab32e5b2972', #scream-ftm
    '0xeee5ea8949f622090cfc16d141305d5120df8da4', #tricrypto
    '0xda3c57a81ace16b2cc34e8872e886575f8ccf672', #renBTC
    '0x0ab24bfc2503bb536ad667c00685bbb70fa90433', #ftm-btc-eth (grand orchestra)
    '0x7fed554476b64b41cbd9d3fa1c38cd781ee701b6', #ftm-btc-eth-usdc (late quartet)
    '0x0139c853539bf1edf221cf9d665f282c2701335a', #ftm-matic-avax-sol-luna-bnb (battle of the bands)
    '0xdf68bf80d427a5827ff2c06a9c70d407e17dc041', #ftm-crv
    '0xc5b2a6ab801e74f098acc8bb62b786b47319c4d9', #ftm-bnb
    '0x6e08721ce0eb1a6776e7965beb5441267d1742c7', #ftm-avax
    '0x6709b167f862e2aed920c2d98bc89e976dbd0615', #ftm-matic
                ]

beefy_avax_contracts = [
    '0x3D81A269E05e6057e4dF9E2D76E254E65a65Eb66', #joe-avax
    '0x68866acc5C940938B373F55F7009f824c7662F5B', #eth-avax
    '0x2b7066770EF90eb7faCFB6cbe6A975C91FA13151', #bnb-avax
    '0xdD63306A9792Ecbd1cd6baED3f1b18BEA638aaCe', #usdc-avax
    '0x8eb23a3010795574eE3DD101843dC90bD63b5099', #usdc-avax
    '0xb1e29194d90d67b8d1c4104FDf6DaF0F7d3344D5', #bifi-avax
    '0xe1a8EeA58D63Ea64d00365531D266C2AD1f62FC4', #tricrypto
    '0xDc5e537764F5Ad0f51Bf52CCF0767083bb4565EC', #eth (aave)
    '0xD0e4b0B711A5296a8D72EB8B2a9Cb0F3f7A4211d', #btc (aave)
    '0x1b156c5c75e9df4caab2a5cc5999ac58ff4f9090', #avax (aave)
    '0xf32e23eb10350e381aa8b775d381e27c50a9195f', #btc-avax
                ]

beefy_poly_contracts = [
    '0x6888f67662d1f442c4428129e0bdb27a275e0a65', #matic-bnb
    '0xc24cf5fa29e619f2d5ccbec46f2295876c3722ff', #matic-eth
    '0x3e9c032052e774b85cbf5f1d6382be06144e1bac', #pear-usdc
    '0xc1a2e8274d390b67a7136708203d71bf3877f158', #matic-usdc
    '0x5a0801bad20b6c62d86c566ca90688a6b9ea1d3f', #tricrypto
    '0xada7f98fb2594e76914eb593e74b348a498ea5bd',#banana-matic
    '0x764b2aacfde7e33888566a6d44005dc982f02031', #matic-avax
    '0x6efbc871323148d9fc34226594e90d9ce2de3da3', #matic-cro
                ]

beefy_one_contracts = [

                ]

########################################### BSC ###########################################
bsc_chain_list = []
bsc_name_list = []
bsc_symbol_list = []
bsc_moo_balance_list = []
bsc_decimal_list = []
bsc_fpps_list = []
bsc_lp_qty_list = []

for x in beefy_bsc_contracts:
    contract = bsc_web3.eth.contract(address=Web3.toChecksumAddress(x), abi=beefy_bsc_abi)
    name = contract.functions.name().call()
    symbol = contract.functions.symbol().call()
    decimals = contract.functions.decimals().call()
    balance = contract.functions.balanceOf(bnb_checksum).call() / float(10**decimals)
    fpps = contract.functions.getPricePerFullShare().call() / float(10**decimals)
    lps = balance * fpps

    bsc_chain_list.append('BSC')
    bsc_name_list.append(name)
    bsc_symbol_list.append(symbol)
    bsc_decimal_list.append(decimals)
    bsc_moo_balance_list.append(balance)
    bsc_lp_qty_list.append(lps)

bsc_df = pd.DataFrame(list(zip(beefy_bsc_contracts, bsc_chain_list, bsc_name_list, bsc_symbol_list, bsc_decimal_list, bsc_moo_balance_list, bsc_lp_qty_list)), columns=['Contract', 'Chain', 'Name', 'Symbol', 'Decimals', 'MooToken Qty', 'LP Qty'])


########################################### FANTOM ###########################################
ftm_chain_list = []
ftm_name_list = []
ftm_symbol_list = []
ftm_moo_balance_list = []
ftm_decimal_list = []
ftm_fpps_list = []
ftm_lp_qty_list = []

for x in beefy_ftm_contracts:
    contract = ftm_web3.eth.contract(address=Web3.toChecksumAddress(x), abi=beefy_ftm_abi)
    name = contract.functions.name().call()
    symbol = contract.functions.symbol().call()
    decimals = contract.functions.decimals().call()
    balance = contract.functions.balanceOf(ftm_checksum).call() / float(10**decimals)
    fpps = contract.functions.getPricePerFullShare().call() / float(10**decimals)
    lps = balance * fpps

    ftm_chain_list.append('Fantom')
    ftm_name_list.append(name)
    ftm_symbol_list.append(symbol)
    ftm_decimal_list.append(decimals)
    ftm_moo_balance_list.append(balance)
    ftm_lp_qty_list.append(lps)

ftm_df = pd.DataFrame(list(zip(beefy_ftm_contracts, ftm_chain_list, ftm_name_list, ftm_symbol_list, ftm_decimal_list, ftm_moo_balance_list, ftm_lp_qty_list)), columns=['Contract', 'Chain', 'Name', 'Symbol', 'Decimals', 'MooToken Qty', 'LP Qty'])

########################################### AVALANCHE ###########################################
avax_chain_list = []
avax_name_list = []
avax_symbol_list = []
avax_moo_balance_list = []
avax_decimal_list = []
avax_fpps_list = []
avax_lp_qty_list = []

for x in beefy_avax_contracts:
    contract = avax_web3.eth.contract(address=Web3.toChecksumAddress(x), abi=beefy_avax_abi)
    name = contract.functions.name().call()
    symbol = contract.functions.symbol().call()
    decimals = contract.functions.decimals().call()
    balance = contract.functions.balanceOf(avax_checksum).call() / float(10**decimals)
    fpps = contract.functions.getPricePerFullShare().call() / float(10**decimals)
    lps = balance * fpps

    avax_chain_list.append('Avalanche')
    avax_name_list.append(name)
    avax_symbol_list.append(symbol)
    avax_decimal_list.append(decimals)
    avax_moo_balance_list.append(balance)
    avax_lp_qty_list.append(lps)

avax_df = pd.DataFrame(list(zip(beefy_avax_contracts, avax_chain_list, avax_name_list, avax_symbol_list, avax_decimal_list, avax_moo_balance_list, avax_lp_qty_list)), columns=['Contract', 'Chain', 'Name', 'Symbol', 'Decimals', 'MooToken Qty', 'LP Qty'])

########################################### POLYGON ###########################################
poly_chain_list = []
poly_name_list = []
poly_symbol_list = []
poly_moo_balance_list = []
poly_decimal_list = []
poly_fpps_list = []
poly_lp_qty_list = []

for x in beefy_poly_contracts:
    contract = poly_web3.eth.contract(address=Web3.toChecksumAddress(x), abi=beefy_poly_abi)
    name = contract.functions.name().call()
    symbol = contract.functions.symbol().call()
    decimals = contract.functions.decimals().call()
    balance = contract.functions.balanceOf(matic_checksum).call() / float(10**decimals)
    fpps = contract.functions.getPricePerFullShare().call() / float(10**decimals)
    lps = balance * fpps

    poly_chain_list.append('Polygon')
    poly_name_list.append(name)
    poly_symbol_list.append(symbol)
    poly_decimal_list.append(decimals)
    poly_moo_balance_list.append(balance)
    poly_lp_qty_list.append(lps)

poly_df = pd.DataFrame(list(zip(beefy_poly_contracts, poly_chain_list, poly_name_list, poly_symbol_list, poly_decimal_list, poly_moo_balance_list, poly_lp_qty_list)), columns=['Contract', 'Chain', 'Name', 'Symbol', 'Decimals', 'MooToken Qty', 'LP Qty'])

########################################### CONCAT & EXPORT ###########################################
master_lp_df = pd.concat([bsc_df, ftm_df, avax_df, poly_df], ignore_index=True)
#print(master_lp_df)
master_lp_df.to_csv(r'Z:\Python\DeFI\beefy_positions.csv', index=False)