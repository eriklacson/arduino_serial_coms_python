from settings import Settings
import time
import serial

com_settings = Settings()

serialFromArduino = serial.Serial(com_settings.port)


def run():

	while True:
	 	input_value = raw_input("Enter a character: ")
	 	send = input_value + '\n'
		serialFromArduino.write(send)
		print "Sent from Raspberry Pi " + send
		time.sleep(.25)

		if (serialFromArduino.inWaiting() > 0):
			input = serialFromArduino.readline()
			print "Received from Arduino: " + input	
run()