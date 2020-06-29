import RPi.GPIO as GPIO
from time import sleep

class uIO:
    def __init__(self, ct):
        self.colorList = []
        self.ct = ct
        
    def updateCategory(self):       
        done = False
        while not done:
            print 'If done, type "done"'
            color = raw_input('Enter the lowercase color you would like to change:\n')
            if color == 'done' or color == '':
                done = True
            elif not(color == 'red') and not(color == 'blue') and not(color == 'white') and not(color == 'green') and not(color == 'yellow'):
                 print '\nPlease enter a valid color\n'
            else:
                prompt = 'What category will be assigned to ' + color + ':\n'
                cat = raw_input(prompt)
                if color == 'red':                    
                    self.ct.red.setCategory(cat)
                elif color == 'blue':                    
                    self.ct.blue.setCategory(cat)
                elif color == 'white':                    
                    self.ct.white.setCategory(cat)
                elif color == 'green':                    
                    self.ct.green.setCategory(cat)
                elif color == 'yellow':                    
                    self.ct.yellow.setCategory(cat)
                
    
    
class rpiIO:
    def __init__(self):
        self.inputDelay = 0.1
        self.sleepTime = 0.5
        # LEDs
        self.redLed, self.blueLed, self.whiteLed, self.greenLed, self.yellowLed = 4, 17, 27, 22, 24
        self.leds = [self.redLed, self.blueLed, self.whiteLed, self.greenLed, self.yellowLed]
        # Buttons
        self.buttonPin1, self.buttonPin2, self.buttonPin3, self.buttonPin4, self.buttonPin5, self.buttonPin6 = 5, 6, 13, 19, 26, 16
        self.buttons = [self.buttonPin1, self.buttonPin2, self.buttonPin3, self.buttonPin4, self.buttonPin5, self.buttonPin6]
        #Dict of buttons --> LEDs
        self.buttonsToLeds = {self.buttonPin1:self.redLed, self.buttonPin2:self.blueLed, self.buttonPin3:self.whiteLed, self.buttonPin4:self.greenLed, self.buttonPin5:self.yellowLed}
    
    
    # Setup LED and Button pins
    def setupPins(self):
        GPIO.setmode(GPIO.BCM)
        for led in self.leds:
            GPIO.setup(led, GPIO.OUT)
        for button in self.buttons:
            GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        return


    # Power off LEDS and clean up GPIO
    def cleanUp(self):
        for led in self.leds:
            GPIO.output(led, GPIO.LOW)
        GPIO.cleanup()
        return
    

    def ledSleep(self):
        sleep(self.sleepTime)
        return


    def ledBlink(self, pin):
        GPIO.output(self.buttonsToLeds[pin], GPIO.HIGH)
        self.ledSleep()
        GPIO.output(self.buttonsToLeds[pin], GPIO.LOW)
        self.ledSleep()


    def otherPinPressed(self, pin):
        if pin == self.buttonPin1: #red
            if not GPIO.input(self.buttonPin6):
                return -1
            elif GPIO.input(self.buttonPin2) and GPIO.input(self.buttonPin3) and GPIO.input(self.buttonPin4) and GPIO.input(self.buttonPin5):
                return 0            
            else:
                return 1
 
        elif pin == self.buttonPin2: #blue
            if not GPIO.input(self.buttonPin6):
                return -1
            elif GPIO.input(self.buttonPin1) and GPIO.input(self.buttonPin3) and GPIO.input(self.buttonPin4) and GPIO.input(self.buttonPin5):
                return 0
            else:
                return 1
        elif pin == self.buttonPin3: #white
            if not GPIO.input(self.buttonPin6):
                return -1
            elif GPIO.input(self.buttonPin1) and GPIO.input(self.buttonPin2) and GPIO.input(self.buttonPin4) and GPIO.input(self.buttonPin5):
                return 0
            else:
                return 1
        elif pin == self.buttonPin4:#green
            if not GPIO.input(self.buttonPin6):
                return -1
            elif GPIO.input(self.buttonPin1) and GPIO.input(self.buttonPin2) and GPIO.input(self.buttonPin3) and GPIO.input(self.buttonPin5):
                return 0
            else:
                return 1
        elif pin == self.buttonPin5: #yellow
            if not GPIO.input(self.buttonPin6):
                return -1
            elif GPIO.input(self.buttonPin1) and GPIO.input(self.buttonPin2) and GPIO.input(self.buttonPin3) and GPIO.input(self.buttonPin4):
                return 0
            else:
                return 1
# end IO

