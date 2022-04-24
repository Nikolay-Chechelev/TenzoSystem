import smbus
from time import sleep


class mcp4725:
	def __init__(self):
		self.i2c = smbus.SMBus(1)
		self.i2c_address = 0x60
		self.data = [0, 0]
		self.gain = 3
		self.v_ref = 3.55
	
	def convert_voltage(self, voltage):
		num = voltage / (self.v_ref * self.gain / 4096)
		self.data[0] = int(num // 256)
		self.data[1] = int(num % 256)
		return self.data
	
	def set_voltage(self, voltage):
		self.convert_voltage(voltage)
		try:
			self.i2c.write_byte_data(self.i2c_address, self.data[0], self.data[1])
		except:
			return True
		return False
	
	def check_available(self):
		try:
			self.i2c.write_byte_data(self.i2c_address, 0, 0)
		except:
			return True
		return False

