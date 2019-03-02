# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'

#Libraries
import datetime
import sys
import Adafruit_DHT
import DistTest
import json
import paho.mqtt.client as mqtt
#import timmy
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
global PIR_PIN
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

#import paho.mqtt.publish as publish
def MOTION(PIR_PIN):
    s=2
    client.publish("s1.alarm_state" , s)
    print("motion")
  
    
    
def start():
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)

def end():
    GPIO.remove_event_detect(PIR_PIN)
    
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sound_sys")
    clint.loop()
    client.subscribe("time_sys")
    client.subscribe("dist_sys")
    client.subscribe("clim_sys")
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("buzzer")
  #  client.subscribe("getclimat")
    #client.subscribe("rain")


    #client.subscribe("CoreElectronics/topic")
 
# The callback for when a PUBLISH message is received from the server.
global time_first_it 
global time_second_it 

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    #int_msg = int(msg.payload)   
    if msg.topic == "sound_sys":
        if int(msg.payload) == 1:
            print("Received message #1, turn buzzer on")
        elif int(msg.payload) == 0:
            print("Received message #2, turn buzzer oFF")
            client.publish("sensors" , json_data)
        elif int(msg.payload) == 3:
            start()
        elif int(msg.payload) == 4:
            end()
            #print ('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature1, humidity1))
                        
    if msg.topic == "clim_sys":
        if int(msg.payload) == 1:
            print("Received message #3, clim_sys")
            humidity, temperature = Adafruit_DHT.read_retry(11, 4)
            json_data = json.dumps({"temperature":temperature, "humidity":humidity})
            client.publish("sensors" , json_data)
            
    if msg.topic == "dist_sys":
        print("Received message #4, dist_sys")
        dist =DistTest.distance()
        client.publish("s1.distance" , dist)
        #dist = DistTest.distance
        print ("Measured Distance = %.1f cm" % dist)
        
        
    if msg.topic == "time_sys":
        if int(msg.payload) == 1:
            global time_first_it
            time_first_it = datetime.datetime.now()
            print("time_first_it",time_first_it)
            
        if int(msg.payload) == 0:          
            time_second_it = datetime.datetime.now()
            print("time_second_it",time_second_it)
            print("time_first_it",time_first_it)
            dif = time_second_it - time_first_it
            print("dif",dif)
            print("Секунды = ", dif.seconds)
            client.publish("s1.time_past" , dif.seconds)
            #print(timmi.raznos(time_second_it,time_first_it))
            #diff = timmi.raznos(time_second_it,time_first_it)
            #client.publish("s1.time_past" , diff)
            #dif = time_second_it - time_first_it
            #print("dif",dif)
            #print("Секунды = ", diff)
            
        
        
           
        
   # if int_msg == 0:
    #    print("Received message #1, turn sound on")
     #   client.publish("s1.humidity","60")
        
        # Do something


    #if msg.payload == "World!":
      #  print("Received message #2, do something else")
        # Do something else
 
# Create an MQTT client and attach our routines to it.
try:
    client = mqtt.Client(client_id="prefmyModel123")
    client.username_pw_set(username="12345",password="12345") 
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("sandbox.rightech.io", 1883, 60)
    client.loop_forever()
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Measurement stopped by User")
    


