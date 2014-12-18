import blockchain, api, bot
from config import *

bot_logger = Logger(666) #Init logger

blocktrail_client = blockchain.Blocktrail(BLOCKTRAIL_KEY, BLOCKTRAIL_SECRET, "BTC", False) #Init blocktrail API

reddit_client = api.RedditClient("vanbexlabs-bot", CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, bot_logger) #Init Reddit API
reddit_msgs = api.RedditFeed(FEED_URL, headers, bot_logger) #Init Reddit Feed

def examine(*args):
  ''' Examine address using blocktrail'''
  address = args[0][1:]

  thread=reddit_client.getinfo(args[1].thread)

  print pprint.pprint([thread.reply, thread.__dict__]) 

  d = blocktrail_client.info(address)
  print 'got address data.', [d, address]

  try:
    reddit_client.login(botuser, botpass)

    if reddit_client.loggedin:
      bot_logger('submitting comment.')
      thread.reply(address + '\'s balance is currently: ' + blocktrail_client.toBTC(d['balance']) + 'BTC. API provided by www.blocktrail.com' )
      #replystr = template.generate('t1', address, blocktrail_client.toBTC(d['balance'])
      #c.reply( replystr )
      thread.mark_as_read()

    if min_elapsed > 3000:
      reddit_client.refresh();

  except Exception, e:
    bot_logger(['error', e])
  
  min_elapsed += 600

  bot_logger('done')
  
  #TODO 
  #POST TO BLOCKCHAIN VIA XCP FEED
  #FORMAT:
  #"REQ: command[0] \n"
  #"REPLY: c.reply()"

def runloop(self)
  '''Default run loop for blocktrailbot'''
  reddit_msgs.refresh() #refresh feed with new data 

  for thing in reddit_msgs.children:
    if thing.was_comment: #if the current thing is a comment get ready to reply
      self.parsecmd( thing.body , '@@' ) #commands are prefixed with '@@' and parsed from comment body
      self.parseargs( thing.body, '@') #args are prefixed with '@' and parsed from comment body 
      self.runtask( self.command , self.args + [thing] ) 

bot = bot.BasicBot(600, runloop, parser ) #create bot
bot.register('examine', examine) #register task to run

while True:
  bot.run() #Run one iteration
  bot.sleep() #Sleep
