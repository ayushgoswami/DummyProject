import os

class DummyProject:
  def __init__(self):
    pass
  
  def testme(self):
    return "testing me"
  
  def checklog(self, filename):
    dstdir = os.path.join(os.getcwd(), "Logs")
    if(not os.path.isdir(dstdir)):
      os.mkdir("Logs")
    logfile = os.path.join(dstdir, filename)
    lfile = open(logfile, 'w')
    lfile.write("testing log creation")
    lfile.close()
