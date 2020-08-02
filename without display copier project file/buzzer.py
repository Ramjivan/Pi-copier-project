import RPi.GPIO as GPIO ## Import GPIO library
import time

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(13, GPIO.OUT) ## Setup GPIO Pin 7 to OUT ## Turn on GPIO pin 7print("Hello World")

while True:
    GPIO.output(13,True)
    time.sleep(.5)
    GPIO.output(13,False)
    time.sleep(.5)