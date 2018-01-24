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
CONTINUE = 1
READING = 0
STRING = ''
##################################################
## CLEAN CLEANUP CODE
## TODO: SERVER CLOSE SERVER CONNECTIONS
def shutdown():
    CONTINUE = False
    curses.endwin()
    sys.exit(0)
    print "SHUTTING DOWN"
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
server_json = {"line1": ["LINE1"], "line2": ["LINE2"]}
##################################################
## TODO: GET SENSOR DATA AND PARSE INTO A READABLE
## LIST OF ATTRIBUTES
def getArray(conn):
    arr = []
    while(not len(arr)):
        try:
            for key in server_json.keys():
                arr.append( json.dumps(server_json[key] ))
            for string_no in range(len(arr)):
                arr[string_no] = arr[string_no] + buffer(arr[string_no])
        except:
             pass
    return arr

##################################################
## PARSE INPUT FROM GUI
def parse_key(stdscr, key, line_no): 
    global READING
    global STRING
    global server_json
    ############################################
    ## OPTION FOR USER ENTERED MESSAGE
    if READING:
        if key == "\n":
            server_json["Message"] = STRING
            STRING = ''
            READING = False
            stdscr.addstr(line_no + 1, 0, 
                buffer(''),curses.color_pair(2))
            stdscr.refresh()
            return
        elif str(key) == chr(127):
            STRING = STRING[:-1] 
        else:
            STRING = STRING + key
        stdscr.addstr(line_no + 1, 0, 
            "Enter Message " + STRING + buffer("Enter Message " + STRING),curses.color_pair(2))
        stdscr.refresh()

    elif key == "\n":
        READING = True
        stdscr.addstr(line_no+1, 0, 
             "Enter Message" + buffer("Enter Message"),curses.color_pair(2))

    ############################################
    ## TYPE q TO QUIT
    elif key == ('q'):
        stdscr.addstr(line_no+1, 0, 
             "SHUTTING DOWN" + buffer("SHUTTING DOWN"),curses.color_pair(2)) 
        shutdown()



    ############################################
    ## CHASSIS MOTION
    elif key == 'KEY_RIGHT':
        stdscr.addstr(line_no + 1, 0, "RIGHT" + buffer("RIGHT"),curses.color_pair(2))
    elif key == 'KEY_LEFT':
        stdscr.addstr(line_no + 1, 0, "LEFT" + buffer("LEFT"),curses.color_pair(2))
    elif key == 'KEY_UP':
        stdscr.addstr(line_no + 1, 0, "UP" + buffer("UP"),curses.color_pair(2))
    elif key == 'KEY_DOWN':
        stdscr.addstr(line_no + 1, 0, "DOWN" + buffer("DOWN"),curses.color_pair(2)) 
    else:
        stdscr.addstr(line_no + 1, 0, key + buffer(key),curses.color_pair(2))
    stdscr.refresh()
def main(stdscr):
    # Clear screen
    stdscr.nodelay(True)
    stdscr.clear()
    stdscr.keypad(True)
    curses.init_pair(1, COLOR_MAGENTA, COLOR_WHITE);
    curses.init_pair(2, COLOR_BLACK, COLOR_GREEN);
    array = []
    while(CONTINUE):
        key = ''
        try:
            array = getArray(1)
        except: 
            pass
        for line_no in range(len(array)):
             stdscr.addstr(line_no,0,array[line_no], color_pair(1))
        
        try:
            key = stdscr.getkey()
        except: 
            pass
        if key:
            parse_key(stdscr, key, line_no)
wrapper(main)


