#!/usr/bin/env python
import serialComs

def get_data(sensorIndex):

    sensorData = {
                    'soil_moisture': None,
                    'temperature': None,
                    'humidity': None
                    
                 }

    try:
        print("in get data")
        sensors = serialComs.get_serial()
        print(sensors)

        for idx, val in enumerate(sensors):
            if idx == sensorIndex:
                sensorData['soil_moisture'] = val[0]
                if val[1] and val[2]:
                    sensorData['temperature'] = val[1]
                    sensorData['humidity'] = val[2]

        
        return sensorData


    except Exception as e:
        print("sensors get_data error: " + str(e))
        return None
