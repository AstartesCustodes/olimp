#!/usr/bin/python
import sys
import Adafruit_DHT
from time import sleep, strftime, time
import matplotlib.pyplot as plt

plt.ion()
x = []
y = []

def write_temp(temp):
    
    #%Y-%m-%d 
    with open("/home/pi/finalLog.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y:%m:%d:%H:%M:%S"),str(temp)))
        
def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()



while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    temp = temperature
    write_temp(temp)
    graph(temp)
    print ('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))
    
#!/usr/bin/python
