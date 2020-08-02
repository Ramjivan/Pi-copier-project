import RPi.GPIO as GPIO ## Import GPIO library
import time
import subprocess

buttonPin = 11
ledPin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.output(ledPin,True) ## Turn on GPIO pin 7print("Hello World")

while True:
    input_state = GPIO.input(buttonPin)
    time.sleep(.5)
    if input_state == False:
        subprocess.call(['./copy.sh'])
        break
    
