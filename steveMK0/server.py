#!/usr/bin/env python

import socket
import time
import signal
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy

####################################################
#  SIGNAL HANDLER
####################################################
def signal_handler(signal, frame):
        print('SIGINT RECIEVED')
        global CONNECTION_MADE
	if CONNECTION_MADE:
		CONNECTION_MADE = 0
		conn.send("close")
		conn.close()
	global RUN_SERVER
	RUN_SERVER  = 0
		

signal.signal(signal.SIGINT, signal_handler)

RUN_SERVER = 1
CONNECTION_MADE = 0
ALERT_PRINTED = 0



####################################################
#  NETWORK SETUP
####################################################
ip = '127.0.0.1'
TCP_IP = ip
TCP_PORT = 5007
BUFFER_SIZE = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
s.bind((TCP_IP, TCP_PORT))

##################################################
#   IMAGE BLACK BOX CODE
##################################################
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

####################################################
#  LISTEN FOR CONNECTIONS NEEDS TO NOT BLOCK FOR
#  THE PURPOSE OF REAL-TIME LOOPING.
####################################################
s.setblocking(0)
i = 0
t = 0
while RUN_SERVER:
	i=i+1
	if not CONNECTION_MADE:	
		s.listen(1)
		try:
			conn, addr = s.accept()
			CONNECTION_MADE = 1
			print 'CONNECTION ADDRESS:', addr
		except (ValueError, socket.error):
			if not ALERT_PRINTED:
				print "No connection"
				ALERT_PRINTED = 1
    	####################################################
	#    WHILE WE HAVE A CONNECTION
	####################################################	
	if CONNECTION_MADE:	
		millis = int(round(time.time() * 1000))
		try:
			data = conn.recv(BUFFER_SIZE)
		except socket.error:
			data = ''
		if data:
                        conn.send(data)  # echo

		if data == "close":
			j = 0
			CONNECTION_MADE = 0	
			conn.close()
        	if data == "img":
            		conn.setblocking(1)
			length = recvall(conn,16)
            		stringData = recvall(conn, int(length))
            		data = numpy.fromstring(stringData, dtype='uint8')
            		decimg=cv2.imdecode(data,1)
            		cv2.imshow('SERVER',decimg)
			cv2.waitKey(1)
            		cv2.destroyAllWindows()
        	if data == "shutdown":
			conn.send("close")
			RUN_SERVER = 0	
	
		millis = int(round(time.time() * 1000)) - millis
		print millis
	data = ''
