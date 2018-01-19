####################################################
import random
import json
import time
import socket
dataPacket = {"request": 0, "data": {
                   "type": "lights", 
                   "value": 0, 
                   "stringVal":" "}}
def getLights():
    if random.random() > .5: 
        dataPacket["data"]["stringVal"] = "ON"
        dataPacket["data"]["value"] = 1
        return 1
     
    else: 
        dataPacket["data"]["stringVal"] = "OFF"
        dataPacket["data"]["value"] = 0
        return 0
def sendHead(word):
    ip = '192.168.42.114'
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ip, 1138))
    clientsocket.send(word)
    buf = clientsocket.recv(64)
    clientsocket.close()
    return buf
def run():
    while(1):
        getLights()
        result = sendHead(json.dumps(dataPacket))

        time.sleep(.5)

if __name__ == "__main__":
    run()

