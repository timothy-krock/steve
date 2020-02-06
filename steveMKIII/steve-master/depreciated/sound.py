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
def sound():
    dataPacket = {"request": 0, "data": {
                   "type": "sound",
                   "value": 0,
                   "stringVal":" "}}
    if random.random() > .5:
        dataPacket["data"]["stringVal"] = "SILENT"
        dataPacket["data"]["value"] = 1
        return dataPacket

    else:
        dataPacket["data"]["stringVal"] = "SOUND HEARD"
        dataPacket["data"]["value"] = 0
        return dataPacket



def run(ip,port,sensor,delay):
    conn = head.connectToHead(ip, port)
    while(1):
        result = head.sendUp(json.dumps(sensor()),conn)
        
        time.sleep(delay)

