#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for
import datetime
import time
import moisture_sensor

app = Flask(__name__)

sensorList = [25, 24]


def log(sensor = "", is_wet):
    now = datetime.datetime.now()
    return("Event log time: "+ str(now ) + " | Sensor: " + sensor + " | Is wet: " + str(is_wet))

def water():
    return "Needs watering now"

@app.route("/moistureCheck")
def check():
    for sensor in sensorList:
        _is_wet = moisture_sensor.is_wet(sensor)
        return log(sensor)
        

@app.route("/test")
def outside_check():
    return "this worked?"

#loop
print ("running")
while True:
    print (check())
    time.sleep(60)
