import praw

class RedditClient():
  def __init__(self, b, i, s, u, l): #b = botname,i = client_id,s = client_secret,u = redirect_uri, l = logger
    self.client = praw.Reddit(b)
    self.client.set_oauth_app_info(i, s, u)
    self.log = l

  def getinfo(self, t): #t = thing_id
    return self.client.get_info(thing_id=t)

  def login(self, u, p): #u = user, p = pass
    self.log('attempting login')
    self.client.login(u,p)
    self.bLogged() #check that we are logged in

  def bLogged(self): #is the user logged in?
    self.loggedin = self.client.is_logged_in()
    self.log( ['loggedin?', self.loggedin] )

  def refresh(self): #refresh access token
    self.log('refreshing access token')
    return self.client.refresh_access_information()

class RedditFeed():
  def __init__(self, u, h, l): #u = feed url, h = headers, l = logger
    self.url = u
    self.headers = h
    self.log = l

  def refresh(self):
    self.log('getting feed data.')

    self.data = requests.get(self.u, headers=self.h).json()
    self.children = [ RedditThing( t, self.log ) for t in self.data['data']['children'] ] 

    self.log('got feed data.')

class RedditThing():
  def __init__(self, t, l): #t = thing, l = logger
    self.log = l
    self.body = t['data']['body'].split(' ') #split sentence into words
    self.was_comment = bool(t['data']['was_comment'])
    self.thread = t['data']['name']
    self.task = ''
    self.log('thing: ',t)

