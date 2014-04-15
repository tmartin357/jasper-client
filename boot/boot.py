#!/usr/bin/env python

import os, json
#import subprocess - Not needed?

import vocabcompiler

def say(phrase, OPTIONS = " -vdefault+m3 -p 40 -s 160 --stdout > say.wav"):
  os.system("espeak " + json.dumps(phrase) + OPTIONS)
  os.system("aplay -D hw:1,0 say.wav")

def configure():
  print "COMPILING DICTIONARY"
  vocabcompiler.compile()

  print "STARTING CLIENT PROGRAM"

  try:
    os.system("/home/pi/jasper/client/start.sh")
  finally:
    say("I experienced a FATAL ERROR.")

if __name__ == "__main__":
  print "==========STARTING JASPER CLIENT=========="
  print "=========================================="
  print "COPYRIGHT 2013 SHUBHRO SAHA, CHARLIE MARSH"
  print "=======Under The MIT License (MIT)========"
  print "=========================================="
  say("Hello.... I am Jasper... Please wait one moment.")
  configure()
