import pandas as pd
import requests
import pandas

url = 'https://api.llama.fi/protocols'

data = requests.get(url).json()
df = pd.DataFrame(data)
df.to_csv(r'Z:\Python\DeFI\defi_llama_stats.csv', index=False)
print(df)