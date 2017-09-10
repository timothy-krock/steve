#!/usr/bin/env python
################################################
##  RASPBERRY PI POWERED COFFEE MACHINE
##  WRITTEN AND BUILT BY TIM KROCK
##  TODO:CUE
###############################################
import time
import json
import time
import os
import subprocess
from time import localtime, strftime
import sys
sys.path.append('~/Desktop/coffee/')
import myjson
os.environ['TZ'] = 'US/Central'

steveCommandsURL = "nope"
steveInfoURL = "nopeII"
steveInfoJSON = {
        "status": -1,
        "sound": -1,
        "temp": -1,
        "ip": -1,
        "motion": -1,
        "lights": -1,
        "lastConnected": -1
}
timer = 0
#####################################
## CODE THAT FETCHE'S PI'S IP ADDRESS
## I OPTED TO PUT THIS IN SO THAT
## THE MACHINE CAN SEND IT'S IP TO
## MY HUD FOR EASY SSH ACCESS
#####################################
def getIP():
    proc = subprocess.Popen('hostname -I', shell=True, stdout=subprocess.PIPE)
    output = proc.stdout.read()
    ip = ''
    for i in range(len(output)):
        if output[i] == ' ':
            ip = output[:i]
            break
    print ip
    return ip




while(1):
    ##################################
    ##  DEFINE CURRENT TIME
    ##  USEFUL FOR timetocoffee
    ##  AS WELL AS json.coffee.updated
    ##################################
    currentTime = strftime("%a, %d %b, %Y %X +0000", localtime())[:-6]
    ip = getIP()
    ##################################
    ## UPDATE INFO JSON WITH SENSORY
    ## DATA
    ##################################
    steveInfoJSON['ip'] = ip
    steveInfoJSON['lastConnected'] = currentTime
    steveInfoJSON['sound'] = 1
    steveInfoJSON['temp'] = 1
    steveInfoJSON['lights'] = 1
    steveInfoJSON['status'] = 1
    steveInfoJSON['motion'] = 1
    try:
        ###################################
        ## SUBMIT INFO JSON
        ###################################
        jason = json.loads(myjson.get(steveCommandsURL))
        print jason
        myjson.store(json.dumps({"command":""}), update=steveCommandsURL, id_only=True)
        myjson.store(json.dumps(steveInfoJSON), update=steveInfoURL, id_only=True)
    

            
            


    except:
        print "NO CONNECTION"
    
    time.sleep(4)
