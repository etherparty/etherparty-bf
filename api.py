import praw

class RedditClient():
  def __init__(self, b, i, s, u): #b = botname,i = client_id,s = client_secret,u = redirect_uri
    self.client = praw.Reddit(b)
    self.client.set_oauth_app_info(i, s, u)

  def getinfo(self, t): #t = thing_id
    return self.client.get_info(thing_id=t)

  def login(self, u, p): #u = user, p = pass
    return self.client.login(u,p)

  def bLogged(self): #is the user logged in?
    return self.client.is_logged_in()

  def refresh(self): #refresh access token
    return self.client.refresh_access_information()

class RedditFeed():
  def __init__(self, u, h, l): #u = feed url, h = headers, l = logger
    self.url = u
    self.headers = h
    self.log = l

  def refresh(self):
    self.log('getting feed data.')

    self.data = requests.get(self.u, headers=self.h).json()

    self.children = self.data['data']['children'] 

    self.log('got feed data.')

  def 

