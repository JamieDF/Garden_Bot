#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for
import datetime
import RPi.GPIO as GPIO
import time

app = Flask(__name__)



def log(info = ""):
    now = datetime.datetime.now()
    return "Event log: " + info + " | time: "+ str(now )


#GPIO SETUP
channel = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print(log("Water detected"))
    else:
        print(log("No water detected"))


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) #event when pin goes high or low
GPIO.add_event_callback(channel, callback)

#loop
while True:
    time.sleep(1)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)