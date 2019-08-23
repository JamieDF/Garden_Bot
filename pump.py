#!/usr/bin/env python
import RPi.GPIO as GPIO
import time



def clean():
    GPIO.cleanup()

def water(pin, time):
    GPIO.setmode(GPIO.BCM)
    pump_on(pin, time)

def pump_on(pump_pin, delay):
    print("pump on | pin: " + str(pump_pin))
    GPIO.setup(pump_pin, GPIO.OUT)
    GPIO.output(pump_pin, GPIO.LOW)
    GPIO.output(pump_pin, GPIO.HIGH) 
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(pump_pin, GPIO.HIGH)
    print("pump off | pin: " + str(pump_pin))