#!/usr/bin/env python
import csv
import os.path
import sys
from datetime import datetime
from collections import OrderedDict
import shutil
import os

def log(_LogEntry):
    
    filename = "log.csv"
    feildnames = ['Time', 'Toms soil moisture', 'Ketchups soil moisture']

    try:
        fd = os.open(filename, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except OSError as e:
        if e.errno == 17:
            #print (e)
            
            with open(filename, 'a', newline='') as f: 
                w = csv.DictWriter(f, feildnames)
                w.writerow(_LogEntry)
        else:
            #print ("Error")
            raise
    else:
        with open(filename, 'w', newline='') as f:
            #print ("else")
            w = csv.DictWriter(f, feildnames)
            w.writeheader()
            w.writerow(_LogEntry)
