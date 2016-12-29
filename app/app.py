from flask import Flask, render_template

import datetime
import RPi.GPIO as GPIO
import sys
import time
import getpass

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO! User: ' + str(getpass.getuser()),
      'time': timeString
      }
   return render_template('main.html', **templateData)

@app.route("/readPin/<pin>")
def readPin(pin):
   try:
      pinn = int(pin)
      GPIO.setup(7, GPIO.OUT)
      GPIO.output(7, GPIO.HIGH)
      time.sleep(1)
      GPIO.output(7, GPIO.LOW)

      #GPIO.setup(pinn, GPIO.IN)
      #if GPIO.input(pinn):
      #   response = "Pin number " + pin + " is high!"
      #else:
      #   response = "Pin number " + pin + " is low!"
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


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
