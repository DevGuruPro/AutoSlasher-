# import smbus
import time

from utils.commons import calculate_heading, apply_calibration


class Magnetometer:
    def __init__(self, address=0x0C, bus_num=1):
        self.address = address
        try:
            self.bus = smbus.SMBus(bus_num)
            self.initialize_sensor()
        except Exception as e:
            print(f"Failed to initialize Magnetometer: {e}")

    def initialize_sensor(self):
        try:
            # Soft reset the sensor
            # self.write_byte(0x0B, 0x80)
            time.sleep(0.1)
            # Set measurement mode, change 0x01 to other values based on desired configuration
            self.write_byte(0x0A, 0x01)
        except Exception as e:
            print(f"Error during sensor initialization: {e}")

    def write_byte(self, reg, value):
        try:
            self.bus.write_byte_data(self.address, reg, value)
        except Exception as e:
            print(f"Failed to write byte to register {reg}: {e}")

    def read_two_bytes(self, lsb_reg, msb_reg):
        try:
            lsb = self.bus.read_byte_data(self.address, lsb_reg)
            msb = self.bus.read_byte_data(self.address, msb_reg)
            value = (msb << 8) + lsb
            if value >= 32768:
                value -= 65536
            return value
        except Exception as e:
            print(f"Failed to read two bytes from registers {lsb_reg} and {msb_reg}: {e}")
            return None

    def read_heading(self):
        try:
            x = self.read_two_bytes(0x00, 0x01)
            y = self.read_two_bytes(0x02, 0x03)
            z = self.read_two_bytes(0x04, 0x05)
            if x is None or y is None or z is None:
                raise Exception("Failed to read magnetometer data")
            calibrated_x, calibrated_y, calibrated_z = apply_calibration(x, y, z)
            heading = calculate_heading(calibrated_x, calibrated_y)
            return heading
        except Exception as e:
            print(f"Failed to read heading: {e}")
            return None

    def __del__(self):
        self.bus.close()
