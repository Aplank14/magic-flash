import RPI.GPIO as GPIO
import random
import time

#Function to turn the red led on
def redOn():
    GPIO.output(20, GPIO.HIGH)
    return

#Function to turn the redled on
def greenOn():
    GPIO.output(26, GPIO.HIGH)
    return

#Function to turn the redled on
def blueOn():
    GPIO.output(21, GPIO.HIGH)
    return

#Function to turn the redled on
def allOff():
    GPIO.output(21, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    return

#Write the function to turn a random color on
def randomColorOn( number ):
    
    return

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

print random.randInt(1,10)
