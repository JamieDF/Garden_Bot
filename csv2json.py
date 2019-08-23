import csv
import json
import os


def parseAndWrite():

    csvfile = open('log.csv', 'r')
    try:
        os.remove("../web-test/log.json")
    except:
        pass

    jsonfile = open('../web-test/log.json', 'w')

    fieldnames = ("Time","Toms soil moisture","Ketchups soil moisture")
    reader = csv.DictReader(csvfile, fieldnames)

    out = json.dumps( [ row for row in reader ] )  

    obj = json.loads(out)
    obj.pop(0)
    out = json.dumps(obj,indent=2)
    jsonfile.write(out)  


def writeCSV(filename, data):

    try:
        fd = os.open(filename, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except OSError as e:
        if e.errno == 17:
            with open(filename, 'a') as f:
                if isinstance(data, list):
                    
                    w = csv.DictWriter(f, list(data[0].keys()))
                    for i in data:
                        
                        w.writerow(i)
                else:
                    
                    w = csv.DictWriter(f, list(data.keys()))
                    w.writerow(data)

            return filename
        else:
            raise
    else:
        with open(filename, 'w') as f:
            if isinstance(data, list):
                
                w = csv.DictWriter(f, list(data[0].keys()))
                w.writeheader()
                for i in data:
                    
                    w.writerow(i)
            else:
                
                w = csv.DictWriter(f, list(data.keys()))
                w.writeheader()
                w.writerow(data)
              
    return filename