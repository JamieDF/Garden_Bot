#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for, jsonify
import datetime
import time
import json
import store_to_csv
from threading import Thread

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
                                'waterTime' :25
                            },
            'pepper' : {
                          'pumpGPIO' : 24,
			  'waterTime': 22
                       },
            'Smol pepper & Other' : {
                          'pumpGPIO' : 23,
			  'waterTime': 6
                       }
        }
#plants = {
#            'strawberry' :  {
#                                'pumpGPIO' : 22,
#                                'waterTime' :25
#                            },
#            'pepper' : {
#                          'pumpGPIO' : 24,
#			  'waterTime': 22
#                       },
#            'Smol pepper & Other' : {
#                          'pumpGPIO' : 23,
#			  'waterTime': 6
#                       }
#        }
#

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
def test():
    print(sensors.get_data())
    return str(sensors.get_data())
# @app.route("/logRoutine")
# def log_routine():
#     global Plants
#     now = datetime.datetime.now()
#     strTime = now.strftime(datetimeFormat)
    
#     print ("\nlog_routine called at :" + now.strftime("%c"))


#     log_Array = get_data(strTime, Plants)
#     print ("Log data = ")
#     for _LogEntry in log_Array:
#         print(str(_LogEntry))
#         store_to_csv.log(_LogEntry)

# def uploadData():
#     csv2json.parseAndWrite()
#     #gitUpload.git_push()

# @app.route("/get_data")
# def get_data(_strTime, _Plants):
    
#     _returnData = []
#     _TempDict = {}
#     # sensorData = moisture_sensor.Get_Data()

#     # _TempDict = {
#     #                 'Time': _strTime,
#     #                 'Toms soil moisture': sensorData[0]['Moisture_Level_Percentage'],
#     #                 'Ketchups soil moisture': sensorData[1]['Moisture_Level_Percentage']}
#     # _returnData.append(_TempDict)


#     # for _plant in _Plants:
#     #     #for each plant
#     #     for _plant_sensor_data in sensorData:
#     #         #find right sensor
#     #         if _plant_sensor_data['SensorID'] == _plant['Sensor_ID']:


#     #             _TempDict = {
#     #                             'Time': _strTime,
#     #                             'Plant_Name': _plant['Plant_Name'],
#     #                             'Moisture_Level' : _plant_sensor_data['Moisture_Level_Percentage']
#     #                         }
#     #             _returnData.append(_TempDict)

#     return _returnData

scheduler = BackgroundScheduler(timezone="Europe/London")
scheduler.add_job(func=water_routine, trigger="cron", hour=8)
scheduler.start()
now = datetime.datetime.now()
date = now.strftime("%c")
print ("Uploader Active at " + str(date))

#log_routine()
#uploadData()

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)

#water_routine()
test()

   
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
    
