import ckb_toolkit.address.address
import requests


test = requests.get('https://explorer.nervos.org/address/ckb1qyqty50wzy30wltyr2y0wpu92yvt8zn62fjqj3m4tj.html').text
print(test)

