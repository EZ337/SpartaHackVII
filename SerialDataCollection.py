import serial
import time

ser = serial.Serial('COM4', 9600)# this line is for setting up the serial connection

data =[]                       # this array stores the data
for i in range(30):           # the loop can be run infinitely, but for test purposes we are running the loop for 30 times
    b = ser.readline()         # this is reading the byte of string
    string_n = b.decode()
    string = string_n.rstrip()

    data.append(string)           # adds elements to the list
    print(string)
    time.sleep(0.1)            # wait time

ser.close()

file1=open('savedata.txt',"w")
for element in data:
    print(element,file=file1)