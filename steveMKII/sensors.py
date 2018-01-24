####################################################
import random
import json
import time
import socket
import head
##################################################
## PROTOTYPE FOR A DATAPACKET
prototype = {"request": 0, "data": {
                   "type": "sound",
                   "value": 0,
                   "stringVal":" "}}
#################################################
## SORRY THIS IS WIERD. THIS IS GOING TO BE 
funcPrototype = {
    "submit": time.sleep(0),
    "delay": 0, 
    "response": time.sleep(0)
}
##################################################
## THREAD LOOP FOR EACH SENSOR
## IT WORKS FOR EACH SENSOR, HOW NEAT IS THAT!
def initIO(sensor,x):
    ip = head.getIp()
    port = head.getPort()
    conn = head.connectToHead(ip, port)
    while(1):
        result = head.sendUp(json.dumps(sensor["submit"]()),conn)

        time.sleep(sensor["delay"])







##################################################
## FUNCTION HOME FOR SOUND SENSOR DATA
def initSound():
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



sound = {
    "submit": initSound,
    "delay": .01,
    "response": time.sleep(0)
}




##################################################
## FUNCTION HOME FOR LIGHT SENSOR DATA
def initLights():
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



lights = {
    "submit": initLights,
    "delay": .01,
    "response": time.sleep(0)
}







##################################################
## FUNCTION HOME FOR THERMOMETER SENSOR DATA
def initTemp():
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


temp = {
    "submit": initTemp,
    "delay": .01,
    "response": time.sleep(0)
}





##################################################
## FUNCTION HOME FOR IP ADDRESS MONITOR
def initIp():
    dataPacket = prototype
    dataPacket["request"] = 0
    dataPacket["data"]["type"] = "ip"
    dataPacket["data"]["value"] = random.random() * 30
    dataPacket["data"]["stringVal"] = "IP"
    return dataPacket



ip = {
    "submit": initIp,
    "delay": .01,
    "response": time.sleep(0)
}




