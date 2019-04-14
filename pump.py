#!/usr/bin/env python
import RPi.GPIO as GPIO
import time



def clean():
    GPIO.cleanup()

def water(_PumpID, _pumpDuration):
    pumpDict = {'P1': 22,'P2': 23}
    GPIO.setmode(GPIO.BCM)
    pump_on(pumpDict[_PumpID], _pumpDuration)

def pump_on(pump_pin, delay):
    print("pump on | pin: " + str(pump_pin))
    GPIO.setup(pump_pin, GPIO.OUT)
    GPIO.output(pump_pin, GPIO.LOW)
    GPIO.output(pump_pin, GPIO.HIGH) 
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(pump_pin, GPIO.HIGH)
