#!/usr/bin/env python
import RPi.GPIO as GPIO

#GPIO SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def is_wet(sensor_channel):
    try:
        if GPIO.input(sensor_channel):
            print("No water detected")
            return False
        else:
            print("Im wet baby")
            return True
    except Exception as e:
        print "check_moisture Exception: " + e
        return "error"
