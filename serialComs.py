import serial

port = '/dev/ttyUSB0'
rate = 9600

s1 = serial.Serial(port,rate)
s1.flushInput()


while True:
    if s1.inWaiting() > 0:
        inputValue = s1.read(1)
		printInputValue
        print(ord(inputValue))

		return [inputValue]
