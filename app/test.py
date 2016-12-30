import sys

class PinIO:
    def __init__(self, addr, typ, val):
        self.addr= addr
        self.typ = typ
        self.val = val

    def toString(self):
        return str(self.addr) + ", " + str(self.typ) + ", value=" + str(self.val) 

        
class Rpi:
    def __init__(self, schema):
        self.pins = []
        self.pins = schema[:]  
        self.pins[0].val = True

def readIO():
    a = 1

rpiSchema = [
    PinIO(1,  "GPIO.IN",     False),
    PinIO(2,  "GPIO.IN",     False),
    PinIO(3,  "GPIO.IN",     False),
    PinIO(4,  "GPIO.IN",     False),
    PinIO(5,  "GPIO.IN",     False),
    PinIO(6,  "GPIO.IN",     False),
    PinIO(7,  "GPIO.IN",     False),
    PinIO(8,  "GPIO.IN",     False),
    PinIO(9,  "GPIO.IN",     False),
    PinIO(10, "GPIO.IN",     False),
    PinIO(11, "GPIO.IN",     False)
]

def main():
    print("Hej Ove! =)")
    rpi = Rpi(rpiSchema)
    
    for x in rpi.pins:
        print(x.toString())

    print("------------------")
    print(rpi.pins[0].typ)

if __name__ == "__main__":
    main()
