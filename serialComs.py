import serial
import time

port = '/dev/ttyUSB0'
rate = 9600

def get_serial():

    try:

#        print("in serialComs")
        s1 = serial.Serial(port,rate)
        s1.flushInput()
        time.sleep(2)


        while True:
            if s1.inWaiting() > 0:
                inputValue = str(s1.readline())
               # print(inputValue)

                inputValue = inputValue.replace("\\r\\n'","")
                inputValue = inputValue.replace("b'", "")
                #print(inputValue)
                # list = inputValue.split('.')
                # for idx, val in enumerate(list):
                #     list[idx]= val.split(',')
                #for i in list:
                #    print(i)
                inputStr = inputValue
                dict = {
                            "temp":None,
                            "humidity": None,
                            "moisture1" : None,
                            "moisture2" : None,
                }

                dict["temperature"] = inputStr.split("t")[0]
                inputStr = inputStr.replace(dict["temperature"] + "t", "")
                dict["humidity"] = inputStr.split("h")[0]
                inputStr = inputStr.replace(dict["humidity"]+ "h", "")
                dict["moisture1"] = inputStr.split("m1")[0]
                inputStr = inputStr.replace(dict["moisture1"]+ "m1", "")
                dict["moisture2"] = inputStr.split("m2")[0]
                inputStr = inputStr.replace(dict["moisture2"]+ "m2", "")

                return dict
#           print(ord(inputValue))
            #return [inputValue]

    except Exception as e:
        print("Serial Comms error " + str(e))


# inputStr = "21.10t68.00h-4m1"
# dict = {
#             "temp":None,
#             "humidity": None,
#             "moisture1" : None,
# }

# dict["temperature"] = inputStr.split("t")[0]
# inputStr = inputStr.replace(dict["temp"] + "t", "")
# dict["humidity"] = inputStr.split("h")[0]
# inputStr = inputStr.replace(dict["humidity"]+ "h", "")
# dict["moisture1"] = inputStr.split("m1")[0]
# inputStr = inputStr.replace(dict["moisture1"]+ "m1", "")

# print(dict)
