####################################################
import random
import json
import time
import socket
import head
prototype = {"request": 0, "data": {
                   "type": "sound",
                   "value": 0,
                   "stringVal":" "}}


##################################################
## THREAD LOOP FOR EACH SENSOR
## IT WORKS FOR EACH SENSOR, HOW NEAT IS THAT!
def run(ip,port,sensor,delay):
    conn = head.connectToHead(ip, port)
    while(1):
        result = head.sendUp(json.dumps(sensor()),conn)

        time.sleep(delay)


##################################################
## FUNCTION HOME FOR SOUND SENSOR DATA
def sound():
    dataPacket = prototype
    dataPacket["request"] = 0
    dataPacket["data"]["type"] = "sound"
    if random.random() > .5:
        dataPacket["data"]["stringVal"] = "SILENT"
        dataPacket["data"]["value"] = 1
        return dataPacket

    else:
        dataPacket["data"]["stringVal"] = "SOUND HEARD"
        dataPacket["data"]["value"] = 0
        return dataPacket
##################################################
## FUNCTION HOME FOR LIGHT SENSOR DATA
def lights():
    dataPacket = prototype
    dataPacket["request"] = 0
    dataPacket["data"]["type"] = "lights"
    if random.random() > .5:
        dataPacket["data"]["stringVal"] = "ON"
        dataPacket["data"]["value"] = 1
        return dataPacket

    else:
        dataPacket["data"]["stringVal"] = "OFF"
        dataPacket["data"]["value"] = 0
        return dataPacket


##################################################
## FUNCTION HOME FOR THERMOMETER SENSOR DATA
def temp():
    dataPacket = prototype
    dataPacket["request"] = 0
    dataPacket["data"]["type"] = "temperature"
    dataPacket["data"]["value"] = random.random() * 30
    if random.random() > .5:
        dataPacket["data"]["stringVal"] = "HOT"
        return dataPacket

    else:
        dataPacket["data"]["stringVal"] = "COLD"
        return dataPacket

##################################################
## FUNCTION HOME FOR IP ADDRESS MONITOR
def ip():
    dataPacket = prototype
    dataPacket["request"] = 0
    dataPacket["data"]["type"] = "ip"
    dataPacket["data"]["value"] = random.random() * 30
    dataPacket["data"]["stringVal"] = "IP"
    return dataPacket

