import requests

test = requests.get('https://www.dxpool.com/pool/hns/profit?observer_token=W-oeKfM40RhfGmiJTp4d7Gsd8Mwk-efA').text()

print(test)