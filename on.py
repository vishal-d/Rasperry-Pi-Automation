import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [2]


for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 

try:
  GPIO.output(2, GPIO.LOW)
  print "Turn On"


except KeyboardInterrupt:
  print "Closing Closing"

  GPIO.cleanup()

