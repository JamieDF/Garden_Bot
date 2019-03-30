#!/usr/bin/env python
import csv
import os.path
import sys
from datetime import datetime
from collections import OrderedDict
import shutil
import os

def log(time, sensor_name, status):
    #get data
    print ("Logging")
# data = OrderedDict([
#     ('Time', time),
#     ('Sensor', sensor_name),
#     ('Status', status)])  
    data = {'Time': time,
            'Sensor': sensor_name,
            'Status': status}
            
    #date = now.strftime("%Y-%m-%d")
    #filename = "log" + str(date.replace("-","")) + ".csv"
    filename = "log.csv"

    try:
        fd = os.open(filename, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except OSError as e:
        if e.errno == 17:
            print (e)
            feildnames = ['Time', 'Sensor', 'Status']
            with open(filename, 'a', newline='') as f: 
                w = csv.DictWriter(f, feildnames)
                w.writerow(data)
        else:
            print ("Error")
            raise
    else:
        with open(filename, 'w', newline='') as f:
            print ("else")
            feildnames = ['Time', 'Sensor', 'Status']
            w = csv.DictWriter(f, feildnames)
            w.writeheader()
            w.writerow(data)

log("testtime1", "sensor 1", "teststatus")
log("testtime1", "sensor 2", "teststatus")
log("testtime1", "sensor 3", "teststatus")