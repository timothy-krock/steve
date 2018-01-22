#!/usr/bin/env python
import signal
import sys
import socket
import time
import json
import os
import math
import json
import time
import subprocess
import thread
##########################
## MY CODE
import sensors

import listener
SERVER_STARTED = 0
reply = "hello!"
ip = "localhost"
data = {}
port = 1141
#########################################
## SIGNAL HANDLER CODE
def signalHandler(signal, frame):
        print('You pressed Ctrl+C!')
        if SERVER_STARTED:
            serversocket.close()
        sys.exit(0)
signal.signal(signal.SIGINT, signalHandler)


#########################################
## TCP CONNECTION WRAPPER
def connectToHead(ip, port):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ip, port))
    return clientsocket
def sendUp(word,connection):
    connection.send(word)
    buf = connection.recv(1024)
    return buf
    
def sensorShutdown(conn):
    conn.close()

##########################################
## NOTE: NOT USED IN THIS FUNCTION
## CODE TO REQUEST INFORMATION FROM SERVER
def request(conn):
     return sendUp(json.dumps({"request": 1, "data":{}}), conn)
def getIp():
    return ip
def getPort():
    return port



###########################################
## HELPER FUNCTION STARTS SERVER
def startServer():
    print "STARTING SERVER"
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind((ip, port))
    serversocket.listen(10) # become a server socket, maximum 5 connections
    SERVER_STARTED = 1
    return serversocket



def fireSensors(ip):
    threads = {}
    threads['lights'] = thread.start_new_thread(sensors.run,(ip,port,sensors.lights,.5))
    threads['sound'] = thread.start_new_thread(sensors.run,(ip,port,sensors.sound,.01))
    threads['temp'] = thread.start_new_thread(sensors.run,(ip,port,sensors.temp,.5))
    threads['ip'] = thread.start_new_thread(sensors.run,(ip,port,sensors.ip,.01))

    return threads
if __name__ == "__main__":
    serversocket = startServer()
    threads = fireSensors(ip)
    connections = []
    for thread in threads:
        connection, address = serversocket.accept()
        connection.setblocking(0)
        connections.append(connection)
    while True:
        time.sleep(.2)
        print "DATA: ", data
        for connection in connections:

            try:
                buf = connection.recv(1024)
            except:
                buf = ''
            if len(buf) > 0:
                packet = json.loads(buf)
                if packet["request"]:
                    connection.send(json.dumps(data))
                    print "REQUEST RECIEVED: ", data
                else:
                    print buf
                    connection.send("reply")

                    data[packet["data"]["type"]] = packet["data"]
