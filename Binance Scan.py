from keys import api_key
from keys import secret_key
# from binance.client import Client
# import pandas as pd
#
# client = Client(api_key=api_key, api_secret=secret_key, tld='us')
#
# test = client.get_asset_details()
# print(test)
#
# # balance_list = pd.DataFrame(client.get_account()['balances'])
# # balance_list.sort_values(by=['free'], inplace=True, ascending=False)
# # print(balance_list)

import urllib.parse
import hashlib
import hmac
import base64
import requests
import time

api_url = "https://api.binance.us"

# get binanceus signature
def get_binanceus_signature(data, secret):
    postdata = urllib.parse.urlencode(data)
    message = postdata.encode()
    byte_key = bytes(secret, 'UTF-8')
    mac = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
    return mac

# Attaches auth headers and returns results of a POST request
def binanceus_request(uri_path, data, api_key, api_sec):
    headers = {}
    headers['X-MBX-APIKEY'] = api_key
    signature = get_binanceus_signature(data, api_sec)
    params={
        **data,
        "signature": signature,
        }
    req = requests.get((api_url + uri_path), params=params, headers=headers)
    return req.text

api_key=api_key
secret_key=secret_key

uri_path = "/sapi/v1/capital/config/getall"
data = {
    "timestamp": int(round(time.time() * 1000))
}

result = binanceus_request(uri_path, data, api_key, secret_key)
print("GET {}: {}".format(uri_path, result))