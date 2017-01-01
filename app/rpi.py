import sys
import json
import RPi.GPIO as GPIO
import time

pinTypes = { -2: "NA",
             -1: "UNKNOWN",
              0: "OUT",
              1: "IN",
             40: "SERIAL",
             41: "SPI",
             42: "I2C",
             43: "HARD_PWM" }


class PinIO:
    def __init__(self, addr, typ, val):
        self.addr= addr
        self.typ = typ
        self.typName = pinTypes[typ]
        self.val = val

    def toString(self):
        return str(self.addr) + ": " + self.typName + ", func=" + str(self.typ) + ", value=" + str(self.val) 

        
class Rpi:
    def __init__(self, firstPin, lastPin):
        self.pins = []
        for p in range(firstPin, lastPin + 1):
            func = ""
            try:
                func = GPIO.gpio_function(p)
            except ValueError:
                func = -2
            self.pins.append(PinIO(p, func, False))
        
        print("RPi constructor")


    def loadSchema(self, schema):
        del self.pins[:]
        self.pins = schema[:]  


    def setupGPIO(self):
        for pin in self.pins:
            if pin.typ == 1:
                #print("set GPIO.PUD_UP channel: " + str(pin.addr))
                GPIO.setup(pin.addr, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        print("GPIO.setup") 

    def readPinsState(self):
        for pin in self.pins:
            if pin.typ == 1:
                pin.val = GPIO.input(pin.addr)
   
    def toJSON(self):
        result1 = json.dumps([x.__dict__ for x in self.pins])
        result2 = json.dumps([x.__dict__ for x in self.pins], sort_keys=True, indent=2)
        return result1


    def toString(self):
        for pin in self.pins:
            print(pin.toString())
        

