import solana
from solana.publickey import PublicKey
from solana.rpc.api import Client
from keys import sol_wallet
import base64, base58

sol = Client('https://api.mainnet-beta.solana.com')
program_id = '7vxeyaXGLqcp66fFShqUdHxdacp4k4kwUpRSSeoZLCZ4' #ray-sol

test = sol.get_account_info(program_id)


print(test)
