from ADS1115 import ads1115
from time import sleep

class tenzo:
	def __init__(self):
		self.adc = ads1115()
		self.adc.configure()
		self.weight = 0
		self.offset = 0
		self.offset = self.calibration()

	def get_weight(self):
		v = self.adc.get_voltage()
		self.weight = v / (0.01 / 500)
		return self.weight - self.offset

	def calibration(self):
		print("Calibration start...")
		offset = 0
		for i in range(100):
			offset += self.get_weight()
			sleep(0.01)
		print("Calibration finished...")
		return offset / 100
    

