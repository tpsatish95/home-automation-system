import RPi.GPIO as GPIO
import time

### Init() Pi Board 
GPIO.setmode(GPIO.BOARD)

CLOCK = 24

GPIO.setup(CLOCK, GPIO.OUT)

def genClockInput():
    GPIO.output(CLOCK,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(CLOCK,GPIO.HIGH)
    return

while 1:
	genClockInput()
	time.sleep(0.5)