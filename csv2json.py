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

