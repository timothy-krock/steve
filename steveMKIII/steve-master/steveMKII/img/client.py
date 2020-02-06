#!/usr/bin/python
import socket
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy
import time

#TCP_IP = 'localhost'
TCP_IP = '192.168.42.106'
TCP_PORT = 5001

sock = socket.socket()
#sock.connect((TCP_IP, TCP_PORT))
sock.connect((TCP_IP, TCP_PORT))
for i in range(40):
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()

    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data = numpy.array(imgencode)
    stringData = data.tostring()

    sock.send( str(len(stringData)).ljust(16));
    sock.send( stringData );
    time.sleep(.1)
    print(sock.recv(100))
sock.close()

decimg=cv2.imdecode(data,1)
cv2.imshow('CLIENT',decimg)
cv2.waitKey(0)
cv2.destroyAllWindows() 
