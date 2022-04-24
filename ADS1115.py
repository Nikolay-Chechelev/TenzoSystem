import smbus
from time import sleep

class ads1115:
    def __init__(self):
        self.i2c = smbus.SMBus(1)
        self.i2c_address = 0x48
        self.adc_config_reg = 0x01
        self.adc_result_reg = 0x00
        self.adc_config = [0x8A, 0xE3]
        self.adc_result = 0
        self.voltage = 0
        
    def configure(self):
        try:
            self.i2c.write_i2c_block_data(self.i2c_address, self.adc_config_reg, self.adc_config)
        except:
            return True
        return False
    
    def check_available(self):
        try:
            self.i2c.write_i2c_block_data(self.i2c_address, self.adc_config_reg, self.adc_config)
        except:
            return True
        return False
        
    def read_adc(self):
        self.adc_result = self.i2c.read_i2c_block_data(self.i2c_address, self.adc_result_reg, 2)
        return self.adc_result
    
    def get_voltage(self):
        data = self.read_adc()
        self.voltage = (int(data[0]) * 256 + int(data[1])) * (0.256 / (2**15))
        if data[0] >= 0x80:
            self.voltage = self.voltage - 0.256
        return self.voltage

