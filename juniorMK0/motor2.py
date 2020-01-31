import RPi.GPIO as GPIO
import time
import json
GPIO.setmode(GPIO.BOARD)
pins = {
    'LE': 40,
    'L1': 31,
    'L2': 32,
    'RE': 37,
    'R1': 35,
    'R2': 33
    }

pinlist = list(pins)
for pin in pinlist:
    print("SETTING UP: ",pin,",",pins[pin])
    GPIO.setup(pins[pin],GPIO.OUT)
    GPIO.output(pins[pin], False)
    
'''
pwm = GPIO.PWM(40,100)
pwm.start(0)
GPIO.output(32,True)
pwm.ChangeDutyCycle(100)
time.sleep(1)
pwm.ChangeDutyCycle(50)
time.sleep(1)
pwm.ChangeDutyCycle(25)
time.sleep(1)
pwm.stop()
'''


def move(m1v, m2v, duration):
    
    a = pins["L2"]
    b = pins["R2"]
    
    if m1v < 0:
        m1v *= -1
        a = pins["L1"]
    if m2v < 0:
        m2v *= -1
        b = pins["R1"]
                
    pwmL = GPIO.PWM(pins["LE"],100)
    pwmR = GPIO.PWM(pins["RE"],100)

    pwmL.start(0)
    pwmR.start(0)
    
    GPIO.output(a,True)
    GPIO.output(b,True)
    
    pwmL.ChangeDutyCycle(m1v)
    pwmR.ChangeDutyCycle(m2v)
    
    time.sleep(duration)
    
    pwmL.stop()
    pwmR.stop()

    pinlist = list(pins)
    for pin in pinlist:
        GPIO.output(pins[pin], False)
    
        



