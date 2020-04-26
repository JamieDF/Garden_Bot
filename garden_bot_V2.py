from flask import Flask, render_template, redirect, url_for, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import json
import time
#import pump


app = Flask(__name__)
currentRoutine = {}
scheduler = None

def loadRoutine():
    try:
        with open('routine.json') as json_file:
            return json.load(json_file)
    except Exception as e:
        print("loadroutine Exception : " + str(e))
    return None

def pumpRoutine(routine):
    print("Performing Pump Routine")
    
    for plant in routine['plants']:
        print("Plant: "+ str(plant['Name']))
        if plant['flush']:
        #flush
            print("Flush")
        print("Watering pin=" + str(plant['pumpGPIO']) + ", time=" + str(plant['waterDuration']))
        #water

def mainRoutine():
    print("#############################################################")
    print("{t} | Running Main Routine".format(t=time.ctime(time.time())))
    global currentRoutine

    tempRoutine = loadRoutine()
    if tempRoutine and not currentRoutine:
        print("No current routine,  loading filed routine")
        currentRoutine = tempRoutine
    elif tempRoutine and currentRoutine:
        if tempRoutine['updatedAt'] == currentRoutine['updatedAt']:
            print("Got routine")
        elif tempRoutine['updatedAt'] != currentRoutine['updatedAt']:
            print("Diffrent routine found,  updating to new version")
    elif currentRoutine and not tempRoutine:
        print("No new routine found,  sticking with current routine")
    else:
        print("No current routine or new routine found.  Waiting for routine changes.")

    if currentRoutine:
        pumpRoutine(currentRoutine)


        
if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)

print("{t} | Starting App".format(t=time.ctime(time.time())))
scheduler = BackgroundScheduler(timezone="Europe/London")
scheduler.add_job(mainRoutine, "interval", minutes=1)
scheduler.start()
mainRoutine()