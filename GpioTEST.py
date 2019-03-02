import RPi.GPIO as GPIO
import time
import sys, traceback
pin=5
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT, initial=1)

try:
    while True:
        print(1)
        GPIO.output(pin, False)
        
        time.sleep(2)
        GPIO.output(pin, True)
        time.sleep(1)
except KeyboardInterrupt:
    print("ctrl+c")
except:
    print("other")
    traceback.print_exc(limit=2,file=sys.stdout)  # вывод исключения через traceback
    
finally:
    GPIO.cleanup()
    print("this is the end")