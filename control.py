#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for, jsonify
import datetime
import time
import moisture_sensor
import json
import store_to_csv

app = Flask(__name__)

sensorList = [25, 24]

@app.route("/")
def outside_check():
    return "did this work?"

def log(sensor, is_wet):
    
    now = datetime.datetime.now()
    
    jsonResponse = {'Event log time:': str(now),
                'Sensor': sensor,
                'Is wet' : is_wet}

    store_to_csv.log(str(now), "sensor " + str(sensor), "is wet = " + str(is_wet))
    return jsonResponse

def water():
    return "Needs watering now"

@app.route("/check")
def check():
    response = []    
    for sensor in sensorList:
        _is_wet = moisture_sensor.is_wet(sensor)
        response.append(log(sensor, _is_wet))
        
    return str({"data": response})

#loop
print ("running")
while True:
    print (str(check()))
    time.sleep(60)

if __name__ == '__main__':
    app.run()
