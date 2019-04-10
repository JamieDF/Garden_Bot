#!/usr/bin/env python

def Get_Data():

    percentage_Array = Get_Normailzed_SerialData()

    _sensorDataArr = [
                    {'SensorID': "S1", 'Moisture_Level_Percentage': percentage_Array[0]},
                    {'SensorID': "S2", 'Moisture_Level_Percentage': percentage_Array[1]},
                    {'SensorID': "S3", 'Moisture_Level_Percentage': percentage_Array[2]},
                    {'SensorID': "S4", 'Moisture_Level_Percentage': percentage_Array[3]}
    ]

    return _sensorDataArr
