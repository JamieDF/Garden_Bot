#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


def water(_PumpID, _pumpDuration):
    pumpDict = {'P1': 22,'P2': 23}
    pump_on(pumpDict[_PumpID], _pumpDuration)

def pump_on(pump_pin, delay):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH) 
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(pump_pin, GPIO.HIGH)