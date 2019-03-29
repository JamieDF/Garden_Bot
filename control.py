#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for
import datetime
import moisture_sensor

app = Flask(__name__)

sensorList[24, 25]


def log(info = ""):
    now = datetime.datetime.now()
    return "Event log: " + info + " | time: "+ str(now )

def water():
    print ("im watering now")

def check():
    for sensor in sensorList:
        _is_wet = moisture_sensor.is_wet(sensor)
        if not _is_wet:
            water()
            log("Watering " + str(sensor))

#loop
print ("running")
while True:
    check()
    time.sleep(5)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
