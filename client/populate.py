import re
from getpass import getpass
import yaml

def run():
    profile = {}

    print "Welcome to the profile populator. If, at any step, you'd prefer not to enter the requested information, just hit 'Enter' with a blank field to continue."

    def simple_request(var, cleanVar, cleanInput=None):
        input = raw_input(cleanVar + ": ")
        if input:
            if cleanInput:
                input = cleanInput(input)
            profile[var] = input

    simple_request("hostname", "HOSTname")
    simple_request("username", "USERname")
    simple_request("password", "password [WILL PRINT]")

    # write to profile
    print("Writing to profile...")
    outputFile = open("profile.yml", "w")
    yaml.dump(profile, outputFile, default_flow_style=False)
    #print profile
    print("Done.")

if __name__ == "__main__":
    run()
