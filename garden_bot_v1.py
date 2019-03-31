#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for, jsonify
import datetime
import time
import moisture_sensor
import json
import store_to_csv
from threading import Thread

app = Flask(__name__)

sensorList = [25, 24]

global run_auto_water
run_auto_water = False


@app.route("/beginAutoWater")
def begin_auto_water():
    global run_auto_water
    
    if run_auto_water:
        return "Auto water already running"
    else:
        try:
            run_auto_water = True
            auto_thread = Thread(target=auto_water)
            auto_thread.start()
            return "Auto water thread started"
        except Exception as err:
            return "Error starting thread: " + str(err)


@app.route("/stopAutoWater")
def stop_auto_water():
    global run_auto_water
    if run_auto_water:
        try:
            run_auto_water = False
            return "Auto water thread stopped"
        except Exception as err:
            return "Error stopping thread: " + str(err)
    else:
        return "Auto water already stopped"


def auto_water():
    run_auto_water
    #loop
    print ("running")
    while run_auto_water:
        time.sleep(60)
        print("Auto water active")
        


@app.route("/test")
def outside_check():
    return "did this work?"

if __name__ == '__main__':
    app.run()
