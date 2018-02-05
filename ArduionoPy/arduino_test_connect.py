# This script takes input from the potentiometer on an Arduino Uno board to manipulate a cylinder length in VPython
# This requires upload of sketch_feb04a_pot_servo to the Arduino before running

import serial
from visual import *

# upload sketch_feb04a_pot_servo to Arduino before running

arduinoSerialData = serial.Serial('/dev/cu.usbmodem1411', 9600)  # set input from Arduino serial port
measuringRod = cylinder(title="MyCyli", radius =.5, length=1, color=color.magenta, pos=(-10,-2,0))  # define cylinder visual python
lengthlabel = label(pos=(0, 0, 0), text='Cyli length is: ', box=True, height=20)


while 1 == 1:  # Loop FOREVER
    rate(20)  # tell vpython to run this loop 20x/sec
    if (arduinoSerialData.inWaiting() > 0):  # check if data available from Arduino
        myData = arduinoSerialData.readline()  # read the data from serial connection
        print myData
        distance = float(myData)  # convert myData to float type
        measuringRod.length=distance  # change the length of the cylinder based on input from potentiometer
        myLabel = "Adjust the Cyli's length. The length is now: " + myData
        lengthlabel.text = myLabel

