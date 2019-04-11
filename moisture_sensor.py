#!/usr/bin/env python
import serialComs

def Get_Data():
    try:
        print("in get data")
        percentage_Array = serialComs.get_serial()

        _sensorDataArr = [
                        {'SensorID': "S1", 'Moisture_Level_Percentage': percentage_Array[0]},
                        {'SensorID': "S2", 'Moisture_Level_Percentage': percentage_Array[1]},
                        {'SensorID': "S3", 'Moisture_Level_Percentage': percentage_Array[2]},
                        {'SensorID': "S4", 'Moisture_Level_Percentage': percentage_Array[3]}
        ]

        return _sensorDataArr


    except Exception as e:
        print("type error: " + str(e))
        return None