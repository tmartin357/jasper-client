import re, os

WORDS = ["START", "SYSTEM"]


def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone number)
    """
    os.system(r"sshpass -p " + profile['password'] + r" ssh " + profile['username'] + r"@" + profile['hostname'] + r" screen -Dr rcore -X stuff $'roscore\r'")

def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bstart system\b', text, re.IGNORECASE))