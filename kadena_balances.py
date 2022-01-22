from Kadena import Kadena
from keys import kda_wallet

client = Kadena('host:443')


await client.get_balances(kda_wallet)

balance = client.get_balances(kda_wallet)

print('balance')