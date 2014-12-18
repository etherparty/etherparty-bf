import blocktrail

class Blocktrail():
  def __init__(self, k, s, n, t): #k=key,s=secret,n=network,t=testnet
    self.client = blocktrail.APIClient(api_key=k, api_secret=s, network=n, testnet=t)

  def info(self, a): #a = address
    return self.client.address(a)

  #rest of API goes here
  def toBTC(self, b): #b = balance
    return self.client.to_btc(b)
