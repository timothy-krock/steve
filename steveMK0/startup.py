#!/usr/bin/env python
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import time
import os
import socket
import signal
import sys
from threading import Thread
import LCD1602
import math
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import PCF8591 as ADC
import motion
##################
#  SIGNAL HANDLER
##################
resultstring = ''
def signal_handler(signal, frame):
        print('SIGINT RECIEVED')
        LCD1602.write(0, 0, '                ')
        LCD1602.write(1, 1, '                ')
        motion.stop()
        disp = Adafruit_SSD1306.SSD1306_128_32(0)
        disp.clear()
        setColor(0xff0000)
        global CONNECTION_MADE
        if CONNECTION_MADE:
                CONNECTION_MADE = 0
                conn.send("close")
                conn.close()
        global RUN_SERVER
        exit(0)
        RUN_SERVER  = 0


signal.signal(signal.SIGINT, signal_handler)
#################
#  NETWORK SETUP
#################


SERVER = 0
CONNECTION_MADE = 0
ALERT_PRINTED = 0


################
#  OLED DISPLAY
################
time.sleep(1)
disp = Adafruit_SSD1306.SSD1306_128_32(0)
disp.clear()
disp.display()
disp.begin()
width = disp.width
height = disp.height
image = Image.new('1',(width, height))
font = ImageFont.load_default()
resultstring = resultstring + 'Signal Handler Started'

##################
# OFF BUTTON CODE
##################
def shutdown():
        LCD1602.write(0, 0, '                ')
        LCD1602.write(1, 1, '                ')
        disp.clear()
        setColor(0x000000)
        os.system("rm ip")
        os.system("rm .ip.swp")
        os.system("sudo shutdown -h now")

GPIO.setup(31,GPIO.IN)
GPIO.add_event_detect(31, GPIO.FALLING, callback = shutdown, bouncetime = 2000)

##################
# BLUE LCD DISPLAY
##################
LCD1602.init(0x27, 1)

################
#  SETUP MOTION
################
motion.setup_motion_bcm()

################
#  SETUP TURRET
################
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
rotate = GPIO.PWM(10, 50)
tilt = GPIO.PWM(9, 50)
rotate.start(7.5)
tilt.start(3)
time.sleep(.1)

GPIO.cleanup(9)
GPIO.cleanup(10)

#######################
#  PHOTORESISTOR SETUP
#######################
photoresistor_pin = 11
ADC.setup(0x48)
GPIO.setup(photoresistor_pin, GPIO.IN)

def LightsOn():
    value = ADC.read(1)
    if value < 200:
        return True
    else:
        return False

###########################################
# FIND OUR IP ADDRESS, OR WAIT IF WE DON'T
# HAVE ONE
###########################################
os.system("hostname -I > ip")
while not os.path.isfile("ip"):
        setColor(0xff0000)
        time.sleep(.1)
        os.system("hostname -I > ip")


################################################
## PIN NUMBERS FOR THE LED INPUTS
################################################
R = 17
G = 22
B = 27

def setup(Rpin, Gpin, Bpin):

    global pins
    global p_R, p_G, p_B
    pins = {'pin_R': Rpin, 'pin_G': Gpin, 'pin_B': Bpin}

    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i], GPIO.HIGH)

    p_R = GPIO.PWM(R, 2000)
    p_G = GPIO.PWM(G, 1999)
    p_B = GPIO.PWM(B, 5000)

    p_R.start(100)
    p_G.start(100)
    p_B.start(100)

################################################
## MAP HEX TO 0-255 (RGB)
################################################
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col): # For example : col = 0x112233
    R_val = (col & 0xff0000) >> 16
    G_val = (col & 0x00ff00) >> 8
    B_val = (col & 0x0000ff) >> 0
    R_val = map(R_val, 0, 255, 0, 100)
    G_val = map(G_val, 0, 255, 0, 100)
    B_val = map(B_val, 0, 255, 0, 100)

    p_R.ChangeDutyCycle(100-R_val)
    p_G.ChangeDutyCycle(100-G_val)
    p_B.ChangeDutyCycle(100-B_val)


################################################
#  rotate = 19
#  tilt = 21
################################################
f = open("ip", "r");
ip_address = f.read()
i = 0
lights = "OFF"
setup(R,G,B)
time_sound_last_heard = -1000;
def GetIP():
        os.system('rm ip')
        os.system("hostname -I > ip")
        f = open("ip", "r");
        ip_address = f.read()
        return ip_address


################################################
## Thermistor function (returns in C)
################################################
def getTemp():
    analogVal = ADC.read(2)
    Vr = 5 * float(analogVal) / 255
    Rt = 10000 * Vr / (5 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    temp = temp - 273.15
    return temp



###############################################
## PARSER FUNCTION FOR SERVER DATA
###############################################

def parseServerData(data):
        #####################################
        # TCP NETWORK SIGNALS
        #####################################
        if data:
                if data != "env":
                        conn.send(data)  # echo
                if data == "close":
                    CONNECTION_MADE = 0
                    conn.close()
                if data == "shutdown":
                    conn.send("close")
                    conn.close()
                    shutdown()
                ##################################
                # OTHER COMMANDS
                ##################################


                if data == "snap":
                    os.system("raspistill -o test.jpg")
                if data == "env":
                    STR='IP: '+ ip_address +'Lights are ' + lights+ "\n"+'Temperature:'+str(int(temp))+ 'C'+ "\n"+'Status: '+STATUS
                    conn.send(STR)
                if data == "a":
                        motion.left()
                if data == "d":
                        motion.right()
                if data == "w":
                        motion.forward()
                if data == "s":
                        motion.backward()
                if data == "x":
                        motion.stop()
                if data:
                        if data[0] == 'r':
                                GPIO.setup(10, GPIO.OUT)
                                rotate = GPIO.PWM(10, 50)
                                rotate.start(float(data[1:]))
                                time.sleep(1)
                                GPIO.cleanup(10)
                        if data[0] == 't':
                                GPIO.setup(9, GPIO.OUT)
                                tilt = GPIO.PWM(9, 50)
                                tilt.start(float(data[1:]))
                                time.sleep(1)
                                GPIO.cleanup(9)
                if data == "cool":
                        disp.begin()

                        disp.clear()
                        disp.display()

                        image = Image.open('test.jpg').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

                        disp.image(image)
                        disp.display()
                        time.sleep(5)




################################################
################################################
## FOREVER: LOOP
################################################
################################################
STATUS = "idle"
while True:
    global SERVER, CONNECTION_MADE, ALERT_PRINTED


    #IP ADDRESS
    if i %500 == 60:
        ip_address = GetIP()

    ############
    #LIGHT INFO
    ############
    if LightsOn():
        lights = "ON"
        setColor(0xfff000)

    else:
        lights = "OFF"
        setColor(0x000fff)

    ###########
    #TEMP INFO
    ###########
    temp = getTemp()

    ####################################
    # CONFIGURE IMAGE FOR SMALL DISPLAY
    ####################################
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((3, -1), 'IP: '+ ip_address, font=font, fill=255)
    draw.text((3, 6),    'Lights are ' + lights,  font=font, fill=255)
    draw.text((3, 14), 'Temperature:'+str(int(temp))+ 'C', font=font, fill=255)
    draw.text((3, 22), 'Status: '+STATUS, font=font, fill=255)
    ##########
    # Display.
    ##########
    disp.image(image)
    disp.display()
    i = i + 1

    ###############
    # BLUE DISPLAY
    ###############
    if time_sound_last_heard > i-15:
        LCD1602.write(0, 0, 'Voice Heard')
        LCD1602.write(1, 1, 'Hello!')
    else:
        LCD1602.clear()
    #################
    # .01 Second Loop
    #################
    for j in range(10):
        ###############
        # SOUND SENSOR
        ###############
        soundVal = ADC.read(0)
        if soundVal <100:
                time_sound_last_heard = i
        #time.sleep(.01)
        if not SERVER:
            #ip  = '10.200.17.88'
            ip = '127.0.0.1'
            TCP_IP = ip
            TCP_PORT = 5007
            BUFFER_SIZE = 2048

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            s.bind((TCP_IP, TCP_PORT))
            s.setblocking(0)
            global SERVER
            SERVER = 1
        if SERVER:

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
                conn.setblocking(0)
                setColor(0xffffff)
                try:
                    data = conn.recv(BUFFER_SIZE)
                except socket.error:
                    data = ''
                parseServerData(data)



                STATUS = "CONNECTED"
            else:
                 STATUS = "IDLE"


