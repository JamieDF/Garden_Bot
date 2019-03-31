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

global auto_thread
auto_thread = None


@app.route("/beginAutoWater")
def begin_auto_water():
    global auto_thread
    
    if auto_thread:
        return "Auto water already running"
    else:
        try:
            auto_thread = Thread(target=auto_water)
            auto_thread.start()
            return "Auto water thread started"
        except Exception as err:
            return "Error starting thread: " + str(err)


@app.route("/stopAutoWater")
def stop_auto_water():
    global auto_thread
    if auto_thread:
        try:
            auto_thread.join()
            auto_thread = None
            return "Auto water thread stopped"
        except Exception as err:
            return "Error stopping thread: " + str(err)
    else:
        return "Auto water already not running"


def auto_water():
    #loop
    print ("running")
    while True:
        #print (str(check()))
        print("Auto water active")
        time.sleep(60)


@app.route("/test")
def outside_check():
    return "did this work?"

if __name__ == '__main__':
    app.run()