import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

red = 6
GPIO.setup(red,GPIO.OUT)



def checkStatus(pin):

    GPIO.setup(pin,GPIO.OUT)

    state = int(GPIO.input(pin))
    return state

def switchState(pin,device_state):

    if device_state =="On":
        device_state = 1
    else:
        device_state = 0

    GPIO.setup(pin,GPIO.OUT)

   

    if device_state==1:
        GPIO.output(pin,0)
    else :
        GPIO.output(pin,1)






