#!/usr/bin/python
 
import aiml
import yaml
k = aiml.Kernel()
config = yaml.safe_load(open('config.yaml'))
# load the aiml file


k.learn("aiml/first.aiml")
k.learn("aiml/bot.aiml")
for key, value in config.items():
    k.setPredicate(key, value)

k.setPredicate("bot_location", 'Chicago')
k.setPredicate("bot_location", 'Chicago')
#k.setBotPredicate("bot_location", 'Irreligion')

while True:
    input = raw_input("> ")

    response = k.respond(input)

    # print out on the shell
    print response
    # and as speech
