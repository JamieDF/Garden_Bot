#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

def activate():
    print("Pump working")


init = False

GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH) 
    
#pump pin = 22
def pump_on(pump_pin, delay):
    init_output(pump_pin)
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(pump_pin, GPIO.HIGH)