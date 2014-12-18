import pprint, logging
import requests, time

#Reddit dev keys
CLIENT_ID = "reddit client id"
CLIENT_SECRET = "reddit client secret"
REDIRECT_URI = "http://localhost:666/callback"

#Blocktrail API
BLOCKTRAIL_KEY="blocktrail key"
BLOCKTRAIL_SECRET="blocktrail secret"

#Reddit Account info
botuser = 'botuser'
botpass = 'botpass'

#Reddit inbox feed (see https://www.reddit.com/prefs/feeds/, "your inbox" => "everything"
FEED_URL="http://www.reddit.com/message/unread/.json?feed={key}&user={user}"

headers = {'user-agent': 'Mozilla/5.0',
       'content-type': 'application/x-www-form-urlencoded' }

min_elapsed = 0

class Logger():
  def __init__(self, l):
    self.level = l

  def log(self, m, *args, **kwargs): #m = message
    logging.log(self.l, m, *args, **kwargs)
