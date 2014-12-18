from config import *

#class Template():
#  t1 = '%s\'s balance is currently: %sBTC. API provided by www.blocktrail.com'  #TODO add link to addr on bt.info
#  def generate(self, t, kwargs**)
#    return self[t] % kwargs

class BasicBot():
  def __init__(self, t, r, l): #t = time to loop, r = run loop, l = logger
    self.time = t
    self.loop = r
    self.log = l
    self.tasks = {}

  def run(self):
    self.log('looping...')
    self.loop()

  def sleep(self):
    self.log('sleeping...')
    time.sleep( self.time )

  def register(self, c, t): #c = command, t = task
    self.log('registered task', c)
    self.tasks[ c ] = t

  def parsecmd(self, m, p): #m = message, p = parse character
    command = [ word for word in m if word[:2] == p ]
    self.log('parsed command', command)
    #TODO error checking?
    #if len(command) != 1:
    #  raise "err"
    #else:
    self.command = command

  def parseargs(self, m, p): #m = message, p = parse character
    args = [ word for word in m.split(' ') if word[:2] == '@' ]
    self.log('parsed args', args)
    #TODO error checking?
    self.args = args

  def runtask(self, c, a): #c = command, a = args
    if c in self.tasks:
      self.log('running task', t)
      self.tasks[ t ](*a)

