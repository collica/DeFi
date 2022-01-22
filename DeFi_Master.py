import time
from datetime import datetime

print('*********************************************')

while True:
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
        print("***Gas Tokens Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("Gas Tokens Success: " + datetime.now().strftime("%H:%M:%S"))
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
    # try:
    #     exec(open('moonpot.py').read())
    # except:
    #     print("***Moonpot Positions Fail*** " + datetime.now().strftime("%H:%M:%S"))
    # else:
    #     print("Moonpot Positions Success: " + datetime.now().strftime("%H:%M:%S"))
    # try:
    #     exec(open('moonpot_prices_yields.py').read())
    # except:
    #     print("***Moonpot Prices & Yields Fail*** " + datetime.now().strftime("%H:%M:%S"))
    # else:
    #     print("Moonpot Prices & Yields Success: " + datetime.now().strftime("%H:%M:%S"))
    try:
        exec(open('helium.py').read())
    except:
        print("***Helium Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("Helium Success: " + datetime.now().strftime("%H:%M:%S"))
    try:
        exec(open('ltc_doge.py').read())
    except:
        print("***LTC/Doge Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("LTC/Doge Success: " + datetime.now().strftime("%H:%M:%S"))
    try:
        exec(open('cardano.py').read())
    except:
        print("***Cardano Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("Cardano Success: " + datetime.now().strftime("%H:%M:%S"))
    # try:
    #     exec(open('wonderland.py').read())
    # except:
    #     print("***Wonderland Fail*** " + datetime.now().strftime("%H:%M:%S"))
    # else:
    #     print("Wonderland Success: " + datetime.now().strftime("%H:%M:%S"))
    # try:
    #     exec(open('hector.py').read())
    # except:
    #     print("***Hector Fail*** " + datetime.now().strftime("%H:%M:%S"))
    # else:
    #     print("Hector Success: " + datetime.now().strftime("%H:%M:%S"))
    print('*********************************************')
    time.sleep(1000)






