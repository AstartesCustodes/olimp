import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
value = GPIO.input(7)
print(value)
