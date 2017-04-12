
import datetime

class MyParent(object):
    def mymsg(self, message):
        print (message)

class MyChild(MyParent):
    def mymsg(self, message):
        message = "{ts} {msg}".format(ts=datetime.datetime.now().isoformat(),msg=message)
        super(MyChild, self).mymsg(message)
    


ob=MyChild()
ob.mymsg("Hello All")

