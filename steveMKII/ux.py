from curses import wrapper
import curses
import time
from curses import *
import sys
import head
import json
width = 60
ip = head.getIp()
port = head.getPort()
##################################################
## CLEAN CLEANUP CODE
## TODO: SERVER CLOSE SERVER CONNECTIONS
def shutdown():
    conn.close()
    sys.exit()

##################################################
## CREATES STRING OF SPACES TO 
## EXTEND STRING TO width CHARACTERS
def buffer(string): 
    buffer = ''
    try: 
         for i in range(width - len(string)):
             buffer = buffer + ' ' 
    except: 
         pass
    return buffer

##################################################
## TODO: GET SENSOR DATA AND PARSE INTO A READABLE
## LIST OF ATTRIBUTES
def getArray(conn):
    arr = []
    while(not len(arr)):
        try:
            retval = head.request(conn)
            server_json = json.loads(retval)
            for key in server_json.keys():
                arr.append( json.dumps(server_json[key] ))
            for string_no in range(len(arr)):
                arr[string_no] = arr[string_no] + buffer(arr[string_no])
        except:
             pass
    return arr

##################################################
## PARSE INPUT FROM GUI
def parse_key(key): 
    if key == 'q':
         shutdown()
def main(stdscr):
    # Clear screen
    stdscr.nodelay(True)
    stdscr.clear()
    curses.init_pair(1, COLOR_MAGENTA, COLOR_WHITE);
    curses.init_pair(2, COLOR_BLACK, COLOR_GREEN);
    # This raises ZeroDivisionError when i == 10.
    conn = head.connectToHead(ip, port)
    conn.setblocking(0)
    array = []
    while(1):
        try:
            array = getArray(conn)
        except: 
            pass
        for line_no in range(len(array)):
             stdscr.addstr(line_no,0,array[line_no], color_pair(1))
        try:
            key = stdscr.getkey()
            parse_key(key) 
            stdscr.addstr(line_no+1, 0, key + buffer(key),curses.color_pair(2))
        except:
            pass
        stdscr.refresh()
#wrapper(main)
conn = head.connectToHead(ip, port)
conn.setblocking(0)

while(1):
    time.sleep(.1)
    print getArray(conn)
