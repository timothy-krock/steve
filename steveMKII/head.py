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
import lights
SERVER_STARTED = 0
reply = "hello!"

#########################################
## SIGNAL HANDLER CODE
def signalHandler(signal, frame):
        print('You pressed Ctrl+C!')
        if SERVER_STARTED:
            serversocket.close()
        sys.exit(0)
signal.signal(signal.SIGINT, signalHandler)





###########################################
## HELPER FUNCTION STARTS SERVER
def startServer():
    ip = '192.168.42.114'
    print "STARTING SERVER"
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind((ip, 1138))
    serversocket.listen(10) # become a server socket, maximum 5 connections
    SERVER_STARTED = 1
    return serversocket
def fireSensors():
    thread.start_new_thread(lights.run,())

if __name__ == "__main__":
    serversocket = startServer()
    fireSensors()

    while True:
        connection, address = serversocket.accept()
        buf = connection.recv(256)
        if len(buf) > 0:
            packet = json.loads(buf)
            print buf
            connection.send(reply)
