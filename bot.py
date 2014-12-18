import blockchain, api
from config import *

bot_logger = Logger(666) 

blocktrail_client = blockchain.Blocktrail(BLOCKTRAIL_KEY, BLOCKTRAIL_SECRET, "BTC", False)

reddit_client = api.RedditClient("vanbexlabs-bot", CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
reddit_msgs = api.RedditFeed(FEED_URL, headers, bot_logger)

#class Template():
#  t1 = '%s\'s balance is currently: %sBTC. API provided by www.blocktrail.com'  #TODO add link to addr on bt.info
#  def generate(self, t, kwargs**)
#    return self[t] % kwargs

class Bot():
  def __init__(self):
    pass

  def run(self)
    while True:
      self.sleep(600)

      #print pprint.pprint(r['data']['children'])
      reddit_msgs.refresh()

      for e in reddit_msgs.children:
        #print e
        if e['data']['was_comment']:
          command = e['data']['body'].split(' ')  
          print 'got feed, parsed command...', command
          if 'examine' in command:
            command.remove('examine')
            command.remove('/u/' + botuser)
            if len(command) != 1:
              raise "err"
            else:
              address = command[0].replace('\n','').replace('\r','')

              c=reddit_client.getinfo(e['data']['name'])

              print pprint.pprint([c.reply, c.__dict__]) 

              print 'got address data.', [address]
              d = blocktrail_client.info(address)

              try:
                print 'attempting login.'
                reddit_client.login(botuser, botpass)

                if reddit_client.bLogged():
                  print 'logged in, submitting comment.'
                  c.reply(address + '\'s balance is currently: ' + blocktrail_client.toBTC(d['balance']) + 'BTC. API provided by www.blocktrail.com' )
                  #replystr = template.generate('t1', address, blocktrail_client.toBTC(d['balance'])
                  #c.reply( replystr )
                  c.mark_as_read()

                if min_elapsed > 3000:
                  print 'refreshing access.'
                  reddit_client.refresh();
              except Exception, e:
                print 'error', e
              
              min_elapsed += 600
              print 'done.'
              
              #POST TO BLOCKCHAIN VIA XCP FEED
              #FORMAT:
              #"REQ: command[0] \n"
              #"REPLY: c.reply()"

  def log(self, m, *args, **kwargs): #l = level, m = message
    logging.log(LOGLEVEL, m, *args, **kwargs)

  def sleep(self, t) #t = time
    self.log('sleeping...')
    time.sleep(t)

bot = 
