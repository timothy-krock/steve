####################################################
import random
import json
import time
import socket
import head
dataPacket = {"request": 0, "data": {
                   "type": "sound",
                   "value": 0,
                   "stringVal":" "}}
def getSound():
    if random.random() > .5:
        dataPacket["data"]["stringVal"] = "SILENT"
        dataPacket["data"]["value"] = 1
        return 1

    else:
        dataPacket["data"]["stringVal"] = "SOUND HEARD"
        dataPacket["data"]["value"] = 0
        return 0



def run(ip,port):
    conn = head.connectToHead(ip, port)
    while(1):
        getSound()
        result = head.sendUp(json.dumps(dataPacket),conn)
        
        time.sleep(.01)

