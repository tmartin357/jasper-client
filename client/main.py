import yaml
import sys
import os
from conversation import Conversation


def isLocal():
    return len(sys.argv) > 1 and sys.argv[1] == "--local"

if isLocal():
    from local_mic import Mic
else:
    from mic import Mic

if __name__ == "__main__":

    print "==========================================================="
    print " JASPER The Talking Computer                               "
    print " Copyright 2013 Shubhro Saha & Charlie Marsh               "
    print "==========================================================="

    profile = yaml.safe_load(open("profile.yml", "r"))

    mic = Mic("languagemodel.lm", "dictionary.dic",
              "languagemodel_persona.lm", "dictionary_persona.dic")
    
    mic.say("Setting up for " + profile['username'] + " at " + profile['hostname'])
    res = os.system(r"sshpass -p " + profile['password'] + r" ssh " + profile['username'] + r"@" + profile['hostname'] + r" screen -dmS rcore")
    if res != 0:
      mic.say("I could not connect to " + profile ['hostname'])

    mic.say("How can I be of service?")

    conversation = Conversation("JASPER", mic, profile)

    conversation.handleForever()
