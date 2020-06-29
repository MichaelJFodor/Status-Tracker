import csv
import RPi.GPIO as GPIO
from barGraphStack import BarGraph
from csvTool import csvColorTool
from userIO import rpiIO, uIO

class Driver():
    def __init__(self, io, ct):
        self.io = io
        self.ct = ct
    
    def runRed(self):
        # Inititalize buttonPressed to false
        buttonPressed = 0        
        # While another button is not pressed
        while buttonPressed == 0:
            # Print for debugging purposes
            print('red', self.ct.red.time)
            
            # Make LED blink
            self.io.ledBlink(self.io.buttonPin1)
            
            # Increment color's time (time that it is on)
            self.ct.red.time += self.io.sleepTime
            
            # Check if a different button is pressed
            buttonPressed = self.io.otherPinPressed(io.buttonPin1)
            
            # if a button is pressed and it is a color, return 0
            # or if a button is pressed and it is a STOP, then return -1
            # otherwise, continue to loop
            if buttonPressed == 1:
                return 0
            elif buttonPressed == -1:
                return -1
                
                
    def runBlue(self):
        buttonPressed = 0 
        while buttonPressed == 0:
            print('blue', self.ct.blue.time)
            self.io.ledBlink(self.io.buttonPin2)
            self.ct.blue.time += self.io.sleepTime
            buttonPressed = self.io.otherPinPressed(io.buttonPin2)
            if buttonPressed == 1:
                return 0
            elif buttonPressed == -1:
                return -1


    def runWhite(self):
        buttonPressed = 0      
        while buttonPressed == 0:
            print('white', self.ct.white.time)
            self.io.ledBlink(self.io.buttonPin3)
            self.ct.white.time += self.io.sleepTime
            buttonPressed = self.io.otherPinPressed(io.buttonPin3)        
            if buttonPressed == 1:
                return 0
            elif buttonPressed == -1:
                return -1


    def runGreen(self):
        buttonPressed = 0         
        while buttonPressed == 0:
            print('green', self.ct.green.time)
            self.io.ledBlink(self.io.buttonPin4)
            self.ct.green.time += self.io.sleepTime
            buttonPressed = self.io.otherPinPressed(io.buttonPin4)
            if buttonPressed == 1:
                return 0
            elif buttonPressed == -1:
                return -1


    def runYellow(self):
        buttonPressed = 0         
        while buttonPressed == 0:
            print('yellow', self.ct.yellow.time)
            self.io.ledBlink(io.buttonPin5)
            self.ct.yellow.time += self.io.sleepTime
            buttonPressed = self.io.otherPinPressed(io.buttonPin5)
            if buttonPressed == 1:
                return 0
            elif buttonPressed == -1:
                return -1


    # Drives all color collection and button pressing
    def checkInput(self, csvwriter):
        # While pin of button is still active
        while not GPIO.input(io.buttonPin1):
            status = self.runRed()
            # If red's button is 0 (different color pressed), break to different color 
            if status == 0:
                break
            # or if red's button is -1 (STOP is pressed), end program with -1
            elif status == -1:
                return -1
        while not GPIO.input(io.buttonPin2):
            status = self.runBlue()
            if status == 0:
                break
            elif status == -1:
                return -1 
        while not GPIO.input(io.buttonPin3):
            status = self.runWhite()
            if status == 0:
                break
            elif status == -1:
                return -1
        while not GPIO.input(io.buttonPin4):
            status = self.runGreen()
            if status == 0:
                break
            elif status == -1:
                return -1           
        while not GPIO.input(io.buttonPin5):
            status = self.runYellow()
            if status == 0:
                break
            elif status == -1:
                return -1
        return 1   

    #Heart beat of program
    def beginCollection(self, csvwriter):
        drive = 1
        # While drive, read if checkInput gets STOP signal
        # If drive is -1 (STOP), then break out program
        # Otherwise keep checking for user input
        print("Ready for collection")
        while(drive == 1):
            drive = self.checkInput(csvwriter)
            #if  drive == -1:
            #    return                
           
    
    
# Function to start the program

ct = csvColorTool()
uio = uIO(ct)
io = rpiIO()
bg = BarGraph()
d = Driver(io, ct)
def run():
    uio.updateCategory()
    with open(ct.filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(ct.fields)
        try:
            io.setupPins()
            GPIO.input(io.buttonPin6)
            d.beginCollection(csvwriter)
        finally:
            ct.updateRows()
            csvwriter.writerows(ct.rows)
            io.cleanUp()
           
run()
bg.drawPlot()

#end statusTracker