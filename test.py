#!/usr/bin/python
 
import aiml
import yaml
k = aiml.Kernel()
config = yaml.safe_load(open('config.yaml'))
# load the aiml file
from glob import glob
aimllist = glob('./aiml/*.aiml')
for i in aimllist:
    k.learn(i)

k.learn("aiml/c.aiml")
for key, value in config.items():
    print key,value
    k.setPredicate(key, value)
    k.setBotPredicate(key, value)

k.saveBrain('./brain')

while True: print k.respond(raw_input("> "))

