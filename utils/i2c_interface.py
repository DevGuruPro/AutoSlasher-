# utils/i2c_interface.py

import smbus

class I2CInterface:
    def __init__(self, bus_num=1):
        self.bus = smbus.SMBus(bus_num)

    def read_byte(self, address, reg):
        return self.bus.read_byte_data(address, reg)

    def write_byte(self, address, reg, data):
        self.bus.write_byte_data(address, reg, data)

    # Add additional methods as needed
