import rpi as RPI
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP);

def event_handler(channel):
    print("event detected: (" + str(channel) + ") " + str(GPIO.input(channel)))

def my_callback(channel):
    print("my callback: (" + str(channel) + ") " + str(GPIO.input(channel)))

def main():
    print("Hej Ove! =)")
    print("------------------")

    # setup board and pins func
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(7, GPIO.OUT)
    #GPIO.setup(5, GPIO.IN)
    
    #rpi = RPI.Rpi(1, 40)
    #print(rpi.toString())
    #print(rpi.toJSON())

    time.sleep(60)

if __name__ == "__main__":
    #GPIO.add_event_detect(11, GPIO.FALLING, callback = event_handler, bouncetime = 1000)
    channel = 11
    GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=500)
    GPIO.add_event_callback(channel, my_callback)
    main()
