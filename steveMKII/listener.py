####################################################
import random
import json
import time
import socket
import head

data = {}

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
        data = head.request(conn)
        print data 
        time.sleep(.01)
