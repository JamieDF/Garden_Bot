#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for, jsonify
import datetime
import time
import json
import store_to_csv
from threading import Thread

import moisture_sensor
import pump

app = Flask(__name__)

sensorList = [{'sensorID' : 25,'is_wet' : None,'last_watered': None, 'last_wet': None}, {'sensorID' : 24,'is_wet' : None,'last_watered': None, 'last_wet':None}]

global run_auto_water
run_auto_water = False

datetimeFormat = '%Y-%m-%d %H:%M:%S'



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

@app.route("/autoWaterStatus")
def get_auto_water_status():
    global run_auto_water
    global sensorList

    if run_auto_water:
        
        return "Auto water is running : data = " + str(sensorList)
    else:
        return "Auto water is not running"



def auto_water():
    global run_auto_water
    global sensorList
    #loop

    print ("running")
    while run_auto_water:
        #check moisture sensor every min for each plant
        for plant in sensorList:
            _is_wet = moisture_sensor.is_wet(sensor)
            if _is_wet:
                plant['is_wet'] = True
                plant['last_wet'] = getTime
            else:
                plant['is_wet'] = False
                if water_time_check(plant):
                    plant['last_watered'] = getTime
                    pump.activate()
                    
            logger(plant, True)

        time.sleep(60)
        print("Auto water active")
        

def getTime():
    now = datetime.datetime.now()
    return now.strftime(datetimeFormat)

def water_time_check(plant_dict):
    last_watered = get_time_diff_in_hours(plant_dict['last_watered'])
    last_wet = get_time_diff_in_hours(plant_dict['last_wet'])

    #if it hasnt been waterd for 6 hours
    if last_watered:
        if last_watered > 6:
            return True
    else:
        #never been watered
        return True

    # #if it has been dry for an hour
    # if last_wet > 1:
    #     return True

        
def get_time_diff_in_hours(recordedtime):
    if recordedtime:
        now = datetime.datetime.now()
        diff = datetime.datetime.strptime(recordedtime, datetimeFormat)- datetime.datetime.strptime(now.strftime(datetimeFormat), datetimeFormat)
        diff_in_hours = diff.total_seconds()/3600
        return diff_in_hours
    

def logger(plant_dict, csv):
    
    now = datetime.datetime.now()
    strTime = now.strftime(datetimeFormat)
    log = ('Event log time:' + strTime +  " | plant_data = " + str(plant_dict))
    print (log)
    if csv:
        store_to_csv.log(strTime, plant_dict)
    return (log)


   
@app.route("/test")
def outside_check():
    return "did this work?"

if __name__ == '__main__':
    app.run()
