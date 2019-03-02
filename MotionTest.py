import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)
def MOTION(PIR_PIN):
    print("Motion Detected!")
    print("PIR Module Test (CTRL+C to exit)")
    time.sleep(2)
    print("Ready")
    
def start():
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)

def end():
    PIO.remove_event_detect(PIR_PIN)
   
#GPIO.remove_event_detect(channel)

if __name__ == '__main__':    
    try:
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Quit")
        GPIO.cleanup()