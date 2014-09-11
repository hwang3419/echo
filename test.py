#!/usr/bin/python
 
import aiml
import yaml
import glob
k = aiml.Kernel()
config = yaml.safe_load(open('config.yaml'))
# load the aiml file

aiml_list = glob.glob('aiml/*.aiml')
print aiml_list
for i in aiml_list:
    k.learn(i)
k.learn('aiml/c.aiml')

for key, value in config.items():
    k.setPredicate(key, value)
#k.setBotPredicate("bot_location", 'Irreligion')
k.saveBrain('./brain')

k.loadBrain('./brain')
while True:
    input = raw_input("> ")

    response = k.respond(input)

    # print out on the shell
    print response
    # and as speech
