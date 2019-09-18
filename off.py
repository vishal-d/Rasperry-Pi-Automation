import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


pinList = [2]


for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 

SleepTimeS = 0.2
SleepTimeL = 0.5


try:
  GPIO.output(2, GPIO.HIGH)
  print "TURN OFF"


except KeyboardInterrupt:
  print "Closing"

  GPIO.cleanup()
