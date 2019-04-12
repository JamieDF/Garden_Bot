import serial
import time

port = '/dev/ttyUSB0'
rate = 9600

def get_serial():

    try:

        print("in serialComs")
        s1 = serial.Serial(port,rate)
        s1.flushInput()
        time.sleep(2)


        while True:
            if s1.inWaiting() > 0:
                inputValue = str(s1.readline())

                inputValue = inputValue.replace("\\r\\n'","")
                inputValue = inputValue.replace("b'", "")
                print(inputValue)
                list = inputValue.split(',')
                return list
#           print(ord(inputValue))
            #return [inputValue]

    except Exception as e:
        print("error " + str(e))
