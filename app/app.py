from flask import Flask, render_template, Response

import datetime
import RPi.GPIO as GPIO
import sys
import time
import getpass
import rpi as RPI
#import threading

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

global rpi
rpi = RPI.Rpi(1, 40)
rpi.setupGPIO()
rpi.readPinsState()

#def input_polling():
#    for i in range(120):
#        time.sleep(1)
#        addr = 11
#        rpi.pins[addr-1].val = GPIO.input(addr)
#        print(rpi.pins[addr-1].val) 

#inThread = threading.Thread(target = input_polling, args=[])
#outThread=threading.Thread(target = output_update, args=[])
#logicThread=threading.Thread(target = logic,args=[])

#inThread.start()

#initEvents()
def input_callback(channel):
    value = GPIO.input(channel) 
    print("input callback: (" + str(channel) + ") " + str(value))
    rpi.pinns[channel].val = value

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
        'title' : 'HELLO! User: ' + str(getpass.getuser()),
        'time': timeString
      }
   return render_template('main.html', **templateData)

@app.route("/getpins")
def getPins():
    resp = Response(response=rpi.toJSON(), status=200, mimetype="application/json")
    return(resp)

@app.route("/boardstat")
def getBoardStatus():
    #rpi.readPinsState()
    templateData = {
        'rpi': rpi
    }
    return render_template("boardstat.html", **templateData)

@app.route("/readPin/<pin>")
def readPin(pin):
   try:
      pinn = int(pin)
      GPIO.setup(7, GPIO.OUT)
      GPIO.output(7, GPIO.HIGH)
      time.sleep(1)
      GPIO.output(7, GPIO.LOW)

      response = "Pin (ok): " + pin 
      GPIO.setup(pinn, GPIO.IN)
      if GPIO.input(pinn):
        response = "Pin number " + pin + " is high!"
      else:
         response = "Pin number " + pin + " is low!"
   except:
      response = "There was an error reading pin " + pin + ". " \
        + str(sys.exc_info()[0]) \
        + str(sys.exc_info()[1]) \
        + str(sys.exc_info()[2]) 


   templateData = {
      'title' : 'Status of Pin' + pin,
      'response' : response
      }

   return render_template('pin.html', **templateData)
    
def initEvents():
    for pin in rpi.pins:
        if pin.typ == 1:
            GPIO.add_event_detect(pin.addr, GPIO.RISING, bouncetime=200)
            GPIO.add_event_callback(pin.addr, input_callback)
            print("add_event_callback ti channel: " + str(pin.addr))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
