import serial
from time import sleep as sleep

ser = serial.Serial('',19200)
while True:
    #print ser.readline()
    ser.write(b'up')
    sleep(0.5)
    ser.write(b'center')
    sleep(0.5)
    ser.write(b'down')
    sleep(0.5)
    ser.write(b'center')
    sleep(0.5)
    ser.write(b'left')
    sleep(0.5)
    ser.write(b'center')
    sleep(0.5)
    ser.write(b'right)
    sleep(0.5)
    ser.write(b'center')
