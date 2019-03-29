#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for
import datetime
import time
import moisture_sensor

app = Flask(__name__)

sensorList = [25, 24]


def log(info = ""):
    now = datetime.datetime.now()
    print( "Event log: " + info + " | time: "+ str(now ))

def water():
    return "Needs watering now"

def check():
    for sensor in sensorList:
        _is_wet = moisture_sensor.is_wet(sensor)
        if not _is_wet:
            log("Sensor " + str(sensor) + " is not wet, " + water())
        else:
            log("Sensor " + str(sensor) + " is wet")

#loop
print ("running")
while True:
    check()
    time.sleep(60)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
