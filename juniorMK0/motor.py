import RPi.GPIO as GPIO
import time
import json
GPIO.setmode(GPIO.BOARD)
pins = {
    'LE': 40,
    'L1': 36,
    'L2': 32,
    'RE': 37,
    'R1': 35,
    'R2': 33
    }
def setup(pins):
    pinlist = list(pins)
    for pin in pinlist:
        
        print("SETTING UP: ",pin,",",pins[pin])
        GPIO.setup(pins[pin],GPIO.OUT)

    
def go(pinlist):
#pinlist looks like ["LE","L1","RE","R4"]
    for pin in pinlist:
        GPIO.output(pin,True)

def goPWM(pinlist):
#pinlist looks like ["LE","L1","RE","R4"]
    for pin in pinlist:
        pwm = GPIO.PWM(pin,100)
        pwm.start(0)
        GPIO.output(32,True)
        pwm.ChangeDutyCycle(50)
        time.sleep(1)
        pwm.stop()

def stop(pinlist):
    for pin in pinlist:
        GPIO.output(pin,GPIO.LOW)
        



if __name__ == "__main__":
    setup(pins)
    #go([pins['L2']])

    goPWM([pins['LE']])

    time.sleep(1)
    stop([pins['LE'],pins['L1'],pins['RE'],pins['R1']])
    
    #go([pins['LE'],pins['L2'],pins['RE'],pins['R2']])
    #time.sleep(1)
    #stop([pins['LE'],pins['L2'],pins['RE'],pins['R2']])
    GPIO.cleanup()