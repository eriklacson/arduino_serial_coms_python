from settings import Settings
import time
import serial

com_settings = Settings()

serialFromArduino = serial.Serial(com_settings.port)


def run():
	while True:
		
		if (serialFromArduino.inWaiting() > 0):
			input = serialFromArduino.read(1)
			print input
			serialFromArduino.write(input)
	
run()