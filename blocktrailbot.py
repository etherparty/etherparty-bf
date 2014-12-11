#!/usr/bin/env python

import praw, requests, time, pprint, blocktrail

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

r2 = praw.Reddit('blocktrailbot')
r2.set_oauth_app_info(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

headers = {'user-agent': 'Mozilla/5.0',
       'content-type': 'application/x-www-form-urlencoded' }

client = blocktrail.APIClient(api_key=BLOCKTRAIL_KEY, api_secret=BLOCKTRAIL_SECRET, network="BTC", testnet=False)


min_elapsed = 0

while True:
  print 'sleeping...'
  time.sleep(600)
  r=requests.get(FEED_URL, headers=headers).json()
  #print pprint.pprint(r['data']['children'])
  print 'got feed data.'
  for e in r['data']['children']:
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

          c=r2.get_info(thing_id=e['data']['name'])

          print pprint.pprint([c.reply, c.__dict__]) 

          print 'got address data.', [address]
          d = client.address(address)

          try:
            print 'attempting login.'
            r2.login(botuser, botpass)

            if r2.is_logged_in():
              print 'logged in, submitting comment.'
              c.reply(address + '\'s balance is currently: ' + blocktrail.to_btc(d['balance']) + 'BTC. API provided by www.blocktrail.com' )
              c.mark_as_read()

            if min_elapsed > 3000:
              print 'refreshing access.'
              r2.refresh_access_information();
          except Exception, e:
            print 'error', e
          
          min_elapsed += 600
          print 'done.'
          
          #POST TO BLOCKCHAIN VIA XCP FEED
          #FORMAT:
          #"REQ: command[0] \n"
          #"REPLY: c.reply()"
