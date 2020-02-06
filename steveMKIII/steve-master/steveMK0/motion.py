# -*- coding: utf-8 -*-
#!/usr/bin/env python
import LCD1602
import sys
import string
import RPi.GPIO as GPIO
#########################################
#  ONLY HERE FOR REFERENCE USE setup()
#  INSTEAD
#########################################

def setup_motion_board():
        GPIO.setmode(GPIO.BOARD)
        global  Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E

        Motor1A =36
        Motor1B =38
        Motor1E =40

        Motor2A =37
        Motor2B =35
        Motor2E =33

        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)

        GPIO.setup(Motor2A,GPIO.OUT)
        GPIO.setup(Motor2B,GPIO.OUT)
        GPIO.setup(Motor2E,GPIO.OUT)

def setup_motion_bcm():
        GPIO.setmode(GPIO.BCM)
        global  Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E
        Motor1A =16
        Motor1B =20
        Motor1E =21

        Motor2A =26
        Motor2B =19
        Motor2E =13

        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)

        GPIO.setup(Motor2A,GPIO.OUT)
        GPIO.setup(Motor2B,GPIO.OUT)
        GPIO.setup(Motor2E,GPIO.OUT)

def forward():
        global  Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E
        print "Going forwards"
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)

        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)


def backward():
        global  Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E
        print "going backwards"
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.HIGH)

        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.HIGH)


def left():
        global  Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E
        print "zero turn left"
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)

        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.HIGH)


def right():
        global  Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E
        print "Zero Turn right"

        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)

        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.HIGH)

def stop():
        global  Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E
        print "stop"
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.LOW)

        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.LOW)
