#!/usr/bin/env python
import serialComs

def get_data():

    sensorData = {
                    'Toms soil moisture': None,
                    'Ketchups soil moisture': None
                 }

    try:
        sensors = serialComs.get_serial()
       # print(sensors)
        sensorData['Toms soil moisture'] = sensors['moisture2']
        sensorData['Ketchup'] = sensors['moisture1']
        # sensorData['temperature'] = sensors['temperature']
        # sensorData['humidity'] = sensors['humidity']
        
        return sensorData


    except Exception as e:
        print("sensors get_data error: " + str(e))
        return None
