#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for, jsonify
import datetime
import time
import json
from apscheduler.schedulers.background import BackgroundScheduler
from threading import Thread
from requests import get

import store_to_csv
import csv2json
import gitUpload
import sensors
import pump

app = Flask(__name__)


plants = {
            'Tomatoes' :  {
                                'pumpGPIO' : 22,
                                'waterTime' :70
                            }
         }


datetimeFormat = '%Y-%m-%d %H:%M:%S'
@app.route("/waterRoutine")
def water_routine():
    global plants
    now = datetime.datetime.now()
    print("\nAuto water routine called at " + now.strftime("%c"))
    
    for key, value in plants.items():
        print("Watering " + str(key) + " : pin=" + str(value['pumpGPIO']) + ", time=" + str(value['waterTime']))       
        pump.water(pin = value['pumpGPIO'], time = value['waterTime'])
        time.sleep(1)
        pump.clean()

    
    print("End Of Auto water routine event")
    return("Auto water routine concluded")

@app.route("/sensor")
def sensor_routine():
    sensorData = sensors.get_data()
    now = datetime.datetime.now()
    sensorData['Time'] = now.strftime("%c")
    print(sensorData)
    store_to_csv.log(sensorData)
    return str(sensorData)

def uploadData():
    try:
        csv2json.parseAndWrite()	
        gitUpload.git_push()
    except Exception as e:
        print("uploadData error: " + str(e))



def ipUpdate():
    ip = get('https://api.ipify.org').text
    try:
        with open('../jamiedf8@gmail.com/Garden_BotV1.5/ip.json', 'w') as outfile:
            json.dump({"ip":ip}, outfile)
        now = datetime.datetime.now()
        print("\nIP file updated at " + now.strftime("%c"))

    except Exception as e:
        print("ipUpdate error: " + str(e))


scheduler = BackgroundScheduler(timezone="Europe/London")
scheduler.add_job(func=water_routine, trigger="cron", hour=8)
scheduler.add_job(sensor_routine, "interval", minutes=59)
scheduler.add_job(uploadData, "interval", minutes=60)
scheduler.start()
now = datetime.datetime.now()
date = now.strftime("%c")
print ("Uploader Active at " + str(date))

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)

sensor_routine()
uploadData()