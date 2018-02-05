# Arduino + Python Sandbox
### These project scripts were built utilizing tutorials from Paul McWhorter
found at http://www.toptechboy.com/using-python-with-arduino-lessons/

Requirements:
- Arduino Uno and assorted inputs/sensors
- Arduino IDE 1.8.5
- Python 2.7* 
- PyCharm (or user preferred IDE)
- Additional Python libraries: VPython, Pyserial v2.7,  

*Paul McWhorter's tutorials provide general install instructions within a Windows OS. I'm using
a Mac and a virtual env so some steps will be slightly different than those spelled out in his guide.
Due to the Python version and dependencies I thought this would be a good opportunity to play around with virtual 
environments on an actual project. I am including notes on my own steps since they are slightly different than those 
provided in McWhorter's tutorial. This assumes Anaconda is already installed.

### Step 1 - Create and Setup Virtual Environment
1. Verify conda is installed. Open Terminal and enter: conda info
- basic info on conda should be output
2. Create an environment named Py27: conda create --name Py27 python=2.7 anaconda
- enter y to proceed
3. Verify creation with list of current environments: conda info --envs
4. Activate environment: source activate Py27
5. Verify correct installation: conda list
6. Install pyserial: conda install -c anaconda pyserial
7. Install VPython: conda install -c mwcraig vpython
8. Verify the libraries have been added: conda list
9. Deactive environment: source deactivate

### Step 2 - Integrate PyCharm with conda Environment
1. Create a new project folder in Pycharm - add to git/github if desired
2. Go to Preferences > Project > Project Interpreter then browse to your anaconda virtual environment installation
it will be something like /anaconda/envs/Py27/python.app/Contents/MacOS/python click Apply

### Step 3 - 'Hello World' from Arduino
1. Write a script within Arduino's void loop to print out an incremental count starting at 0.
2. Test proper output to Arduino's Serial Monitor
3. Close Serial Monitor

### Step 4 - 'Hello World' from Arduino to Python IDE/Console
1. Write a script that uses the readline function to retrieve data sent across the serial port of the Arduino 
and prints it into the Python interpreter.
2. Run code ot test.

### Step 5 - Setup Arduino board
Since I don't have two of the sensors McWhorter has I decided to give his lesson 3 a shot using the potentiometer and 
a servo.
1. Connect Ground on Arduino to ground on bread board
2. Connect 5.5v on Arduino to positive on bread board
3. Connect a power and ground to potentiometer
4. Connect capacitor between pos and negative of potentiometer
5. Connect lead from output of potentiometer to pin A0 on Arduino
5. Connect a power and ground to servo
6. Connect a capacitor between pos and neg of servo
7. Connect an input lead to pin ~9 on the Arduino

### Step 6 - Write Arduino Test Code
1. In Arduino IDE input code to read inputs from the potentiometer and convey any movements to the servo. 
Make sure to Serial.print some data or text 
2. Open Serial monitor in IDE to test proper data output



 