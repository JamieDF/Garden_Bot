#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("Im wet baby")
    else:
        print("No water detected")



# GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) #event when pin goes high or low
# GPIO.add_event_callback(channel, callback)

#loop
while True:

    if GPIO.input(channel):
        print("Im wet baby")
    else:
        print("No water detected")
    time.sleep(1)
