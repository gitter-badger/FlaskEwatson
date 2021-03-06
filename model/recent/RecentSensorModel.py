from model.recent.RecentPressureModel import RecentPressureModel
from model.recent.RecentHumidityModel import RecentHumidityModel
from model.recent.RecentCO2Model import RecentCO2Model
from model.recent.RecentTemperatureModel import RecentTemperatureModel
import logging

logging.getLogger(__name__)


class RecentSensorModel():
	def __init__(self, pressures, humidities, co2, temperatures):
		self.pressures = pressures
		self.humidities = humidities
		self.co2 = co2
		self.temperatures = temperatures

	# Used if container is filled with arrays
	def to_json_array(self):
		# Init
		pressureJsonArray = []
		humidityJsonArray = []
		co2JsonArray = []
		temperatureJsonArray = []

		# Converting to json
		for press in self.pressures:
			pressureJsonArray.append(press.to_json())

		for hum in self.humidities:
			humidityJsonArray.append(hum.to_json())

		for c in self.co2:
			co2JsonArray.append(c.to_json())

		for temp in self.temperatures:
			temperatureJsonArray.append(temp.to_json())

		# Return data
		data = {
			'type': 'All recent sensor readings',
			'attributes': {
				'pressures': pressureJsonArray,
				'humidities': humidityJsonArray,
				'co2': co2JsonArray,
				'temperatures': temperatureJsonArray
			}
		}
		return data

	# Used if variables are only one value
	def to_single_json(self):
		# Init
		pressureJson = None
		humidityJson = None
		co2Json = None
		temperatureJson = None

		if self.pressures is not None:
			pressureJson = self.pressures.to_json()

		if self.humidities is not None:
			humidityJson = self.humidities.to_json()

		if self.co2 is not None:
			co2Json = self.co2.to_json()

		if self.temperatures is not None:
			temperatureJson = self.temperatures.to_json()

		# Return data
		logging.debug("Formatting SensorModel to json")
		data = {
			'type': 'All recent sensor readings',
			'attributes': {
				'pressure': pressureJson,
				'humidity': humidityJson,
				'co2': co2Json,
				'temperature': temperatureJson
			}
		}
		return data

	def to_average_json(self):
		logging.debug("Formatting SensorModel to average json")
		json = {
			'type': 'All recent sensor average',
			'attributes': {
				'pressure': RecentPressureModel.average_json(self.pressures),
				'humidity': RecentHumidityModel.average_json(self.humidities),
				'co2': RecentCO2Model.average_json(self.co2),
				'temperature': RecentTemperatureModel.average_json(self.temperatures)
			}
		}
		return json

	# The nuclear option, sending an entire database via json
	@staticmethod
	def get_all():
		# init
		foundPressure = []
		foundHumidities = []
		foundCo2 = []
		foundTemperatures = []

		# Execution (4 connection, could be more efficient but query time is hardly an issue)
		foundPressure = RecentPressureModel.get_all()
		foundHumidities = RecentHumidityModel.get_all()
		foundCo2 = RecentCO2Model.get_all()
		foundTemperatures = RecentTemperatureModel.get_all()

		# Build object
		returnObj = RecentSensorModel(
			foundPressure, foundHumidities, foundCo2, foundTemperatures)

		# Clean and return
		return returnObj

	@staticmethod
	def get_by_search(start, end):
		# init
		foundPressure = []
		foundHumidities = []
		foundCo2 = []
		foundTemperatures = []

		# Execution (4 connection, could be more efficient but query time is hardly an issue)
		foundPressure = RecentPressureModel.get_by_search(start, end)
		foundHumidities = RecentHumidityModel.get_by_search(start, end)
		foundCo2 = RecentCO2Model.get_by_search(start, end)
		foundTemperatures = RecentTemperatureModel.get_by_search(start, end)

		# Build object
		returnObj = RecentSensorModel(
			foundPressure, foundHumidities, foundCo2, foundTemperatures)

		# Clean and return
		return returnObj

	@staticmethod
	def get_oldest():
		# init
		foundPressure = None
		foundHumidities = None
		foundCo2 = None
		foundTemperatures = None

		# Execution (4 connection, could be more efficient but query time is hardly an issue)
		foundPressure = RecentPressureModel.get_oldest()
		foundHumidities = RecentHumidityModel.get_oldest()
		foundCo2 = RecentCO2Model.get_oldest()
		foundTemperatures = RecentTemperatureModel.get_oldest()

		# Build object
		returnObj = RecentSensorModel(
			foundPressure, foundHumidities, foundCo2, foundTemperatures)

		# Clean and return
		return returnObj

	@staticmethod
	def get_newest():
		# init
		foundPressure = None
		foundHumidities = None
		foundCo2 = None
		foundTemperatures = None

		# Execution (4 connection, could be more efficient but query time is hardly an issue)
		foundPressure = RecentPressureModel.get_newest()
		foundHumidities = RecentHumidityModel.get_newest()
		foundCo2 = RecentCO2Model.get_newest()
		foundTemperatures = RecentTemperatureModel.get_newest()

		# Build object
		returnObj = RecentSensorModel(
			foundPressure, foundHumidities, foundCo2, foundTemperatures)

		# Clean and return
		return returnObj

	@staticmethod
	def get_average():
		# init
		foundPressure = None
		foundHumidities = None
		foundCo2 = None
		foundTemperatures = None

		# Execution (4 connection, could be more efficient but query time is hardly an issue)
		foundPressure = RecentPressureModel.get_average()
		foundHumidities = RecentHumidityModel.get_average()
		foundCo2 = RecentCO2Model.get_average()
		foundTemperatures = RecentTemperatureModel.get_average()

		# Build object
		returnObj = RecentSensorModel(
			foundPressure, foundHumidities, foundCo2, foundTemperatures)

		# Clean and return
		return returnObj

	@staticmethod
	def get_average_by_range(start, end):
		# init
		foundPressure = None
		foundHumidities = None
		foundCo2 = None
		foundTemperatures = None

		# Execution (4 connection, could be more efficient but query time is hardly an issue)
		foundPressure = RecentPressureModel.get_average_by_range(start, end)
		foundHumidities = RecentHumidityModel.get_average_by_range(start, end)
		foundCo2 = RecentCO2Model.get_average_by_range(start, end)
		foundTemperatures = RecentTemperatureModel.get_average_by_range(start, end)

		# Build object
		returnObj = RecentSensorModel(
			foundPressure, foundHumidities, foundCo2, foundTemperatures)

		# Clean and return
		return returnObj

	@staticmethod
	def delete_all():
		# Init
		returnValue = True

		# Execution
		RecentPressureModel.delete_all()
		RecentHumidityModel.delete_all()
		RecentCO2Model.delete_all()
		RecentTemperatureModel.delete_all()

		# Clean and return
		return returnValue

	@staticmethod
	def delete_by_range(start, end):
		# Init
		returnValue = True

		# Execution
		RecentPressureModel.deltee_by_range(start, end)
		RecentHumidityModel.delete_by_range(start, end)
		RecentCO2Model.delete_by_range(start, end)
		RecentTemperatureModel.delete_by_range(start, end)

		# Clean and return
		return returnValue
