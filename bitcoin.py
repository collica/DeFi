import requests


req = requests.get('http://blockexplorer.com/q/getreceivedbyaddress/39YCxEnDuHRLT9v7Cc48zYokRFFQ7otF5S/1').json()

print(req)