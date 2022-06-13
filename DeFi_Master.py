import time
from datetime import datetime

print('*********************************************')

while True:
    try:
        exec(open('bitcoin.py').read())
    except:
        print("***Bitcoin Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("Bitcoin Success: " + datetime.now().strftime("%H:%M:%S"))
    try:
        exec(open('cmc.py').read())
    except:
        print("***CMC Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("CMC Success: " + datetime.now().strftime("%H:%M:%S"))
    try:
        exec(open('sha256.py').read())
    except:
        print("***SHA 256 Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("SHA 256 Success: " + datetime.now().strftime("%H:%M:%S"))
    try:
        exec(open('gas_tokens.py').read())
    except:
        print("***L1 Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("L1 Success: " + datetime.now().strftime("%H:%M:%S"))
    try:
        exec(open('correlations 6m.py').read())
    except:
        print("***Correlations 6m Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("Correlations 6m Success: " + datetime.now().strftime("%H:%M:%S"))
    try:
        exec(open('correlations 12m.py').read())
    except:
        print("***Correlations 12m Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("Correlations 12m Success: " + datetime.now().strftime("%H:%M:%S"))
    try:
        exec(open('beefy_positions.py').read())
    except:
        print("***Beefy Positions Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("Beefy Positions Success: " + datetime.now().strftime("%H:%M:%S"))
    try:
        exec(open('beefy_prices_yields.py').read())
    except:
        print("***Beefy Prices & Yields Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("Beefy Prices & Yields Success: " + datetime.now().strftime("%H:%M:%S"))
    try:
        exec(open('helium.py').read())
    except:
        print("***Helium Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("Helium Success: " + datetime.now().strftime("%H:%M:%S"))
    # try:
    #     exec(open('ltc_doge.py').read())
    # except:
    #     print("***LTC/Doge Fail*** " + datetime.now().strftime("%H:%M:%S"))
    # else:
    #     print("LTC/Doge Success: " + datetime.now().strftime("%H:%M:%S"))
    # try:
    #     exec(open('cardano.py').read())
    # except:
    #     print("***Cardano Fail*** " + datetime.now().strftime("%H:%M:%S"))
    # else:
    #     print("Cardano Success: " + datetime.now().strftime("%H:%M:%S"))
    print('*********************************************')
    time.sleep(1000)






