import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.LOW)


GPIO.setup(21, GPIO.IN)


print(GPIO.input(21))
