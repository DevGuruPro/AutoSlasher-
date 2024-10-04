import smbus
import time

from utils.commons import calculate_heading, apply_calibration


class Magnetometer:
    def __init__(self, address=0x0C, bus_num=1):
        self.address = address
        self.bus = smbus.SMBus(bus_num)
        self.initialize_sensor()

    def initialize_sensor(self):
        # Soft reset the sensor
        # self.write_byte(0x0B, 0x80)
        time.sleep(0.1)
        # Set measurement mode, change 0x01 to other values based on desired configuration
        self.write_byte(0x0A, 0x01)

    def write_byte(self, reg, value):
        self.bus.write_byte_data(self.address, reg, value)

    def read_two_bytes(self, lsb_reg, msb_reg):
        lsb = self.bus.read_byte_data(self.address, lsb_reg)
        msb = self.bus.read_byte_data(self.address, msb_reg)
        value = (msb << 8) + lsb
        if value >= 32768:
            value -= 65536
        return value

    def read_heading(self):
        x = self.read_two_bytes(0x00, 0x01)
        y = self.read_two_bytes(0x02, 0x03)
        z = self.read_two_bytes(0x04, 0x05)
        calibrated_x, calibrated_y, calibrated_z = apply_calibration(x, y, z)
        heading = calculate_heading(calibrated_x, calibrated_y)
        return heading

    def __del__(self):
        self.bus.close()
