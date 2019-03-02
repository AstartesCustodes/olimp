import serial
from time import sleep
#port = serial.Serial("/dev/ttyAMA0", baudrate=115200, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)


#port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

ser = serial.Serial ("/dev/ttyS0", 115200)    #Open port with baud rate
while True:
    ser.write('AT')
    sleep(2)
    received_data = ser.read()              #read serial port
    sleep(2)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                   #print received data
    ser.write(received_data)                #transmit data serially 