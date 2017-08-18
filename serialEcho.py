from settings import Settings
import time
import serial

com_settings = Settings()

serialFromArduino = serial.Serial(com_settings.port)


def run():

	while True:
		send = raw_input("Enter a character: ")
		serialFromArduino.write(send)
		print "Sent from Raspberry Pi " + send

		if (serialFromArduino.inWaiting() > 0):
			input = serialFromArduino.read(1)
			print "Sent from Arduino: " + input	
run()