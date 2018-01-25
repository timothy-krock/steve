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
    sensor["init"]()
    ip = head.getIp()
    port = head.getPort()
    conn = head.connectToHead(ip, port)
    while(1):
        result = head.sendUp(json.dumps(sensor["fetch"]()),conn)
        sensor["response"](result)
        time.sleep(sensor["delay"])
 



##################################################
## FUNCTION HOME FOR SOUND SENSOR DATA
def initSound():
    return

def getSound():
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

def replySound(data):
    return

soundObj = {
    "init": initSound,
    "fetch": getSound,
    "delay": .01,
    "response": replySound 
}






##################################################
## FUNCTION HOME FOR LIGHT SENSOR DATA
def initLights():
    return

def getLights():
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

def replyLights(data):
    return 

lightsObj = {
    "init": initLights,
    "fetch": getLights,
    "delay": .01,
    "response": replySound
}







##################################################
## FUNCTION HOME FOR THERMOMETER SENSOR DATA
def initTemp():
    return

def getTemp():
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
def replyTemp(data):
    return 0

tempObj = {
    "init": initTemp,
    "fetch": getTemp,
    "delay": .01,
    "response": replyTemp
}








##################################################
## FUNCTION HOME FOR IP ADDRESS MONITOR
def initIp():
    return

def getIp():
    dataPacket = prototype
    dataPacket["request"] = 0
    dataPacket["data"]["type"] = "ip"
    dataPacket["data"]["value"] = head.getIp()
    dataPacket["data"]["stringVal"] = "IP"
    return dataPacket
def replyIp(data):
    return


ipObj = {
    "init": initIp,
    "fetch": getIp,
    "delay": 1, 
    "response": replyIp
}






##################################################
## FUNCTION HOME FOR UX PORT
def initServer():
    print "STARTING UX SERVER"
    ip = head.getIp2()
    if ip == '':# or ip == 'localhost':
        print "RESTARTING UX SERVER"
        time.sleep(.5)
        initServer()
    else:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.bind(head.getIp2(), head.getPort2())
   
    return
def getServer():
    return {"request": 1, "data": {}}
def replyServer(data):
    print data

serverObj = {
    "init": initServer,
    "fetch": getServer,
    "delay": 1,
    "response": replyServer
}













