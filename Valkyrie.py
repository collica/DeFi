import requests
import pandas as pd

v = requests.get('https://valkyrie-funds.com/wgmi-holdings/').content()
print(v)