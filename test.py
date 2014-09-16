#!/usr/bin/python
 
import aiml
import yaml
_globalSessionID = "_global"
def getBotPredicate(self,name):
    """Retrieve the value of the specified bot predicate.

    If name is not a valid bot predicate, the empty string is returned.        

    """
    try: return self._botPredicates[name]
    except KeyError,e:
        print 'error',e
        return ""
def getPredicate(self, name, sessionID = _globalSessionID):
    """Retrieve the current value of the predicate 'name' from the
    specified session.

    If name is not a valid predicate in the session, the empty
    string is returned.

    """
    try: return self._sessions[sessionID][name]
    except KeyError, e:
        print 'error',e
        return ""
aiml.Kernel.getBotPredicate = getBotPredicate
aiml.Kernel.getPredicate = getPredicate
k = aiml.Kernel()
config = yaml.safe_load(open('config.yaml'))
# load the aiml file
from glob import glob
aimllist = glob('./aiml/*.aiml')
#for i in aimllist:
#    k.learn(i)
k.loadBrain('./brain')
k.learn("aiml/c.aiml")
for key, value in config.items():
    #print key,value
    k.setPredicate(key, value)
    k.setBotPredicate(key, value)

#k.saveBrain('./brain')
print dir(k)
print k.getBotPredicate('master')
print k.respond('tell me about yourself')
from pprint import pprint
#pprint(k._botPredicates)
#while True: print k.respond(raw_input("> "))

