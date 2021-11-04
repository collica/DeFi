import time
from datetime import datetime

print('*********************************************')

while True:
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
    try:
        exec(open('cardano.py').read())
    except:
        print("***Cardano Fail*** " + datetime.now().strftime("%H:%M:%S"))
    else:
        print("Cardano Success: " + datetime.now().strftime("%H:%M:%S"))

    print('*********************************************')
    time.sleep(1000)






