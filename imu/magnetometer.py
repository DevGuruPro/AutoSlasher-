# sensors/magnetometer.py

from utils.i2c_interface import I2CInterface

class MagnetometerSensor:
    def __init__(self, address=0x0C, bus_num=1):
        self.i2c = I2CInterface(bus_num)
        self.address = address
        self.configure_sensor()

    def configure_sensor(self):
        # Initialize sensor settings
        pass

    def read_raw_data(self):
        # Read raw X, Y, Z data from the sensor
        x = self._read_axis_data(0x03)
        y = self._read_axis_data(0x05)
        z = self._read_axis_data(0x07)
        return x, y, z

    def _read_axis_data(self, reg):
        high = self.i2c.read_byte(self.address, reg)
        low = self.i2c.read_byte(self.address, reg + 1)
        value = (high << 8) | low
        if value > 32767:
            value -= 65536
        return value
