mport RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
print "Motor on"
GPIO.output(23,GPIO.HIGH)
GPIO.output(24,GPIO.HIGH)
time.sleep(1)
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)

