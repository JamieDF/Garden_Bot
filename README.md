This was a project which revolved around creating an automated watering system to keep some tomato plants in my window alive.  

It consisted of a raspberryPi attached to a 5v DC pump and an Arduino nano with a moisture sensor.   The idea was that the moisture sensor would recognise when the plant needed watered then trigger a routine where the pump would water the plants and then wait until needed again. 

The data record from the sensor was logged and stored at hourly increments throughout the day.  This data was pushed into the git repo https://github.com/JamieDF/web-test/.  This was done to host a simple interface on Git Pages to see the logged sensor data without hosting anything elsewhere, or on the raspberryPI. 

This repo has been abandoned in favour of a newer repo of mine https://github.com/JamieDF/aquaponic
