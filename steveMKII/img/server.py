#!/usr/bin/python
import socket
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

TCP_IP = '192.168.42.106'
TCP_PORT = 5001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)
conn, addr = s.accept()
while(1):
    length = recvall(conn,16)
    stringData = recvall(conn, int(length))
    data = numpy.fromstring(stringData, dtype='uint8')
    print("RECIEVED") 
    decimg=cv2.imdecode(data,1)
    cv2.imshow('SERVER',decimg)
    char = cv2.waitKey(100)
    cv2.destroyAllWindows()
    print("HELLO")
    
    conn.send("HELLO")

s.close()
cv2.destroyAllWindows() 
