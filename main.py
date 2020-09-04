import threading
import sys
import getopt
import os
from threading import Event
from server import server
from sensor import temperatureSensor
from sensor import pressureSensor
from sensor import humiditySensor
from sensor import co2Sensor

# Main entry point of application
def main(argv):
	try:
		# Parsing argv
		opts, args = getopt.getopt(argv,"-d","--development")
		for opt, arg in opts:
			if opt == "-d":
				os.environ["DEVELOPMENT"] = "1"

		print('Application Started')
		if os.environ.get("DEVELOPMENT") == "1":
			print("Application started in DEVELOPMENT mode")

		# Sensor related start up
		print('Starting Temperature Sensor')
		temperatureThread = threading.Thread(target=temperatureSensor.run, daemon=True)
		temperatureThread.start()

		print('Starting Pressure Sensor')
		pressureThread = threading.Thread(target=pressureSensor.run, daemon=True)
		pressureThread.start()

		print('Starting Humidity Sensor')
		humidityThread = threading.Thread(target=humiditySensor.run, daemon=True)
		humidityThread.start()

		print('Starting CO2 Sensor')
		co2Thread = threading.Thread(target=co2Sensor.run, daemon=True)
		co2Thread.start()

		# Http related start up
		print('Starting Flask Server')
		serverThread = threading.Thread(target=server.run, daemon=True)
		serverThread.start()

		Event().wait()
		print('Exit with ctrl-c')
	except KeyboardInterrupt as e:
		print('Shutting down')

if __name__=="__main__":
	main(sys.argv[1:])
