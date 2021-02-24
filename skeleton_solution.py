from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from time import time, ctime
from datetime import datetime

rpcuser='quaker_quorum'
rpcpassword='franklin_fought_for_continental_cash'
rpcport=8332
rpcip='3.134.159.30'

rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, rpcip, rpcport))


def run():
  count = 0
  commands = [ [ "getblockhash", height] for height in range(800) ]
  block_hashes = rpc_connection.batch_(commands)
  blocks = rpc_connection.batch_([ [ "getblock", h ] for h in block_hashes ])
  block_times = [ block["time"] for block in blocks ]
  print(block_hashes[0])
  print(datetime.utcfromtimestamp(block_times[0]))
  for block in blocks:
      count = count + 1
      if block["time"] > 1232100000:
          print(block["height"])
          break

run()