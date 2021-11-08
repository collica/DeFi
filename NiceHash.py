import requests
import pandas as pd


ck_box = 'https://whattomine.com/asic.json?factor%5Bsha256_hr%5D=70000.0&factor%5Bsha256_p%5D=2800.0&factor%5Bscrypt_hash_rate%5D=1100.0&factor%5Bscrypt_power%5D=1050.0&factor%5Bx11_hr%5D=336000.0&factor%5Bx11_p%5D=1800.0&factor%5Bsia_hr%5D=730.0&factor%5Bsia_p%5D=600.0&factor%5Bqk_hr%5D=56000.0&factor%5Bqk_p%5D=1600.0&factor%5Bqb_hr%5D=56000.0&factor%5Bqb_p%5D=1700.0&factor%5Bmg_hr%5D=56.0&factor%5Bmg_p%5D=700.0&factor%5Bsk_hr%5D=28.0&factor%5Bsk_p%5D=600.0&factor%5Blbry_hr%5D=210.0&factor%5Blbry_p%5D=3300.0&factor%5Bbk14_hr%5D=52000.0&factor%5Bbk14_p%5D=2200.0&factor%5Bx11g_hr%5D=7.0&factor%5Bx11g_p%5D=900.0&factor%5Bcn_hr%5D=360.0&factor%5Bcn_p%5D=720.0&factor%5Beq_hr%5D=135.0&factor%5Beq_p%5D=1420.0&factor%5Blrev2_hr%5D=13.0&factor%5Blrev2_p%5D=1100.0&factor%5Bbcd_hr%5D=185.0&factor%5Bbcd_p%5D=670.0&factor%5Bl2z_hr%5D=62.0&factor%5Bl2z_p%5D=670.0&factor%5Bphi_hr%5D=310.0&factor%5Bphi_p%5D=670.0&factor%5Bkec_hr%5D=29.0&factor%5Bkec_p%5D=430.0&factor%5Bgro_hr%5D=56.0&factor%5Bgro_p%5D=900.0&esg=true&factor%5Besg_hr%5D=1050.0&factor%5Besg_p%5D=0.0&factor%5Btsr_hr%5D=150.0&factor%5Btsr_p%5D=800.0&factor%5Bcost%5D=0.0&sort=Profit24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main'


data = requests.get(ck_box).json()
df = pd.DataFrame(data['coins']).transpose()
df.to_csv(r'Z:\Python\DeFI\whattomine.csv', index=False)



print(df)