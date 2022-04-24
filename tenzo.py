from ADS1115 import ads1115
from time import sleep
from parameters import Parameters


class Tenzo:
	def __init__(self):
		self.parameters = Parameters()
		self.parameters.read_parameters()
		self.adc = ads1115()
		self.adc.configure()
		self.weight = 0
		self.offset = 0
		self.max_load = float(self.parameters.parameters['max_load'])
		self.rkp = float(self.parameters.parameters['rkp'])
		self.sensor_voltage = float(self.parameters.parameters['sensor_voltage'])
		self.offset = self.calibration()

	def get_weight(self):
		v = self.adc.get_voltage()
		self.weight = v / ((self.rkp * self.sensor_voltage) / (self.max_load * 1000))
		return self.weight - self.offset

	def calibration(self):
		print("Calibration start...")
		offset = 0
		for i in range(100):
			offset += self.get_weight()
			sleep(0.01)
		print("Calibration finished...")
		return offset / 100
