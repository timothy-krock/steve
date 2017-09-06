#!/usr/bin/env python
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import socket
import time
import signal
import cv2
import numpy

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        s.send("close")
        s.close()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)




TCP_IP = '127.0.0.1'
TCP_PORT = 5007
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
        s.connect((TCP_IP, TCP_PORT))
except socket.error:
        print "CONNECTION REUSED"
        sys.exit(0)
i = 1
data = ''
sent = ''
while i:
        
	sent = 'img'
        if sent:
                s.send(sent)
                data = s.recv(BUFFER_SIZE)
        if sent == "img":
                capture = cv2.VideoCapture(0)
                ret, frame = capture.read()
                encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
                result, imgencode = cv2.imencode('.jpg', frame, encode_param)
                data = numpy.array(imgencode)
                stringData = data.tostring()
                s.send( str(len(stringData)).ljust(16));
                s.send( stringData );

        sent = ''
        data = ''
	
s.close()


