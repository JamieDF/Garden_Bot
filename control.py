#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for
import datetime
import time
import moisture_sensor
import json

app = Flask(__name__)

sensorList = [25, 24]


def log(sensor, is_wet):
    now = datetime.datetime.now()
    
    jsonResponse = {'Event log time:': now,
                'Sensor': sensor,
                'Is wet' : is_wet}

    return jsonResponse

def water():
    return "Needs watering now"

@app.route("/moistureCheck")
def check():
    response = []    
    for sensor in sensorList:
        _is_wet = moisture_sensor.is_wet(sensor)
        response.append(log(sensor, _is_wet))
        
    return jsonify({"data": response})

@app.route("/test")
def outside_check():
    return "this worked?"

#loop
print ("running")
while True:
    print (str(check()))
    time.sleep(60)
