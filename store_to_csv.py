#!/usr/bin/env python
import csv
import os.path
import sys
from datetime import datetime
from collections import OrderedDict
import shutil
import os

def log(time, plant_dict):
    #get data
    print ("Logging")

    data = {'Time': time,
            'sensorID': plant_dict['sensorID'],
            'Is_wet': plant_dict['is_wet'],
            'Last_Watered': plant_dict['last_watered'],
            'Last_Wet': plant_dict['last_wet'],
            }
            
    filename = "log.csv"
    feildnames = ['Time', 'sensorID', 'Is_wet', 'Last_Watered', 'Last_Wet']

    try:
        fd = os.open(filename, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except OSError as e:
        if e.errno == 17:
            print (e)
            
            with open(filename, 'a', newline='') as f: 
                w = csv.DictWriter(f, feildnames)
                w.writerow(data)
        else:
            print ("Error")
            raise
    else:
        with open(filename, 'w', newline='') as f:
            print ("else")
            w = csv.DictWriter(f, feildnames)
            w.writeheader()
            w.writerow(data)
