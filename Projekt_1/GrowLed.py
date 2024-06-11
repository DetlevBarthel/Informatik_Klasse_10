from machine import Pin
from time import sleep


class GrowLed:
    def __init__(self):
        self.LED    = Pin("LED",Pin.OUT)                       # use GP25 as an ouput for the Onboard LED
        self.led_extern = Pin(15, Pin.OUT)
        
    def blinkLed(self):
        #LED.value(1)
        self.led_extern.value(1)
        sleep(1)
        #LED.value(0)
        self.led_extern.value(0)
        sleep(1)
