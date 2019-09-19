#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for, jsonify
import datetime
import time
import json
import store_to_csv
from threading import Thread
from requests import get
import subprocess
import os
import csv2json
#import gitUpload


import time

#import schedule
from apscheduler.schedulers.background import BackgroundScheduler
import sensors
#import moisture_sensor
import pump

app = Flask(__name__)

plants = {
            'strawberry' :  {
                                'pumpGPIO' : 22,
                                'waterTime' :16
                           },
            'pepper' : {
                          'pumpGPIO' : 24,
			  'waterTime': 16
                       },
            'Smol pepper & Other' : {
                          'pumpGPIO' : 23,
			  'waterTime': 6
                       }
        }

_plants = {
            'ebbAndFlow' :  {
                                'pumpGPIO' : 22,
                                'waterTime' :30
                           }}


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.datetime.now().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

@app.route("/ebbAndFlow")
def ebbAndFlow():

    global _plants
    now = datetime.datetime.now()
    print("\nEbb & Flow routine called at " + now.strftime("%c"))
    #check time is good
    if is_time_between(datetime.time(8,00), datetime.time(22,30)):
        print("Time Good")

        print("Flush")
        pump.water(pin = 22, time = 2)
        time.sleep(1)
        
        for key, value in _plants.items():
            print("Watering " + str(key) + " : pin=" + str(value['pumpGPIO']) + ", time=" + str(value['waterTime']))       
            pump.water(pin = value['pumpGPIO'], time = value['waterTime'])
            time.sleep(1)
            pump.clean()

        print("End Of Ebb & Flow routine event")
        return("Ebb & Flow routine concluded")

    else:
        print("Time not within active range, not activating Ebb & Flow routine")
        return("Time not within active range, not activating Ebb & Flow routine")




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
    store_to_csv.writeCSV('../jamiedf8@gmail.com/Garden_BotV1.5/sensorData.csv', sensorData)
    return str(sensorData)

def ipUpdate():

    try:
        ip = get('https://api.ipify.org').text
        with open('../jamiedf8@gmail.com/Garden_BotV1.5/ip.json', 'w') as outfile:
            json.dump({"ip":ip}, outfile)
        now = datetime.datetime.now()
        print("\nIP file updated at " + now.strftime("%c"))

    except Exception as e:
        print("ipUpdate error: " + str(e))
        print("Potentially internet error,  Assuming insync is down")
        try:
            os.system('./runInsync.sh')
        except Exception as e:
            print("Run insync expct : " +  str(e))

scheduler = BackgroundScheduler(timezone="Europe/London")
#scheduler.add_job(func=water_routine, trigger="cron", hour=8)
scheduler.add_job(func=ipUpdate, trigger="cron", hour=12)
#scheduler.add_job(sensor_routine, "interval", minutes=60)
scheduler.add_job(ebbAndFlow, "interval", minutes=90)
scheduler.start()
now = datetime.datetime.now()
date = now.strftime("%c")
print ("Uploader Active at " + str(date))

#log_routine()
#uploadData()

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
#water_routine()
ebbAndFlow()
ipUpdate()

   
# @app.route("/test")
# def outside_check():
#     print(get_time_diff_in_hours('2019-03-31 15:34:05'))
#     return "did this work?"

# @app.route("/pumptest")
# def outside_check():
#     pump.activate()
#     return "did pump test work?"




# global run_auto_water
# run_auto_water = False
# @app.route("/beginAutoWater")
# def begin_auto_water():
#     global run_auto_water
    
#     if run_auto_water:
#         return "Auto water already running"
#     else:
#         try:
#             run_auto_water = True
#             auto_thread = Thread(target=auto_water)
#             auto_thread.start()
#             return "Auto water thread started"
#         except Exception as err:
#             return "Error starting thread: " + str(err)


                # {'sensorID' : 25,'is_wet' : None,'last_watered': None, 'last_wet': None},
                # {'sensorID' : 24,'is_wet' : None,'last_watered': None, 'last_wet':None}]

# @app.route("/stopAutoWater")
# def stop_auto_water():
#     global run_auto_water
#     if run_auto_water:
#         try:
#             run_auto_water = False
#             return "Auto water thread stopped"
#         except Exception as err:
#             return "Error stopping thread: " + str(err)
#     else:
#         return "Auto water already stopped"

# @app.route("/autoWaterStatus")
# def get_auto_water_status():
#     global run_auto_water
#     global sensorList

#     if run_auto_water:
        
#         return "Auto water is running : data = " + str(sensorList)
#     else:
#         return "Auto water is not running"


# def getTime():
#     now = datetime.datetime.now()
#     return now.strftime(datetimeFormat)

# def water_time_check(plant_dict):
#     last_watered = get_time_diff_in_hours(plant_dict['last_watered'])
#     last_wet = get_time_diff_in_hours(plant_dict['last_wet'])

#     #if it hasnt been waterd for 6 hours
#     if last_watered:
#         if last_watered > 6:
#             return True
#     else:
#         #never been watered
#         return True

#     # #if it has been dry for an hour
#     # if last_wet > 1:
#     #     return True

        
# def get_time_diff_in_hours(recordedtime):
#     if recordedtime:
#         now = datetime.datetime.now()
#         diff = datetime.datetime.strptime(now.strftime(datetimeFormat), datetimeFormat)- datetime.datetime.strptime(recordedtime, datetimeFormat)
#         diff_in_hours = diff.total_seconds()/3600
#         return diff_in_hours
    
