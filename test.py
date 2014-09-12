#!/usr/bin/python
 
import aiml
import yaml
k = aiml.Kernel()
config = yaml.safe_load(open('config.yaml'))
# load the aiml file
from glob import glob
k.learn("aiml/c.aiml")
aimllist = glob('./aiml/*.aiml')
for i in aimllist:
    k.learn(i)

k.learn("aiml/c.aiml")
for key, value in config.items():
    k.setPredicate(key, value)

k.saveBrain('./brain')

while True:
    input = raw_input("> ")

    response = k.respond(input)

    # print out on the shell
    print response
    # and as speech
