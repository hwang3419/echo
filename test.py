#!/usr/bin/python
import aiml #as aiml
import yaml
from aiml import AimlParser

k = aiml.Kernel()
config = yaml.safe_load(open('config.yaml'))
# load the aiml file
'''from glob import glob
aimllist = glob('./aimlv2/*.aiml')


for key, value in config.items():
    k.setPredicate(key, value)
    k.setBotPredicate(key, value)

firstlist = sorted(glob('./aimlv2/reduction*'))
print firstlist
secondlist = sorted(glob('./aimlv2/mp*.aiml'))
print secondlist
for f in firstlist:
    k.learn(f)
    aimllist.remove(f)
for f in secondlist:
    k.learn(f)
    aimllist.remove(f)
for f in aimllist:
    k.learn(f)'''
print dir(k)
k.loadBrain('./brainV2')


from pprint import pprint
#pprint(k._botPredicates)
#while True: print k.respond(raw_input("> "))


while True: print k.respond(raw_input(">"))
