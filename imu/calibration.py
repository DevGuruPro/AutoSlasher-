# calibration.py
import importlib.util
import math
import os

class CalibrationData:
    def __init__(self, min_x, max_x, min_y, max_y, min_z, max_z):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.min_z = min_z
        self.max_z = max_z

class CalibrationManager:
    def __init__(self):
        self.calibration_data = None

    def load_calibration(self, filepath):
        # Construct the full path to the settings file
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(base_dir, filepath)

        # Load calibration data from the setup file
        spec = importlib.util.spec_from_file_location("settings", full_path)
        settings = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(settings)

        calibration_data = settings.CALIBRATION
        self.calibration_data = CalibrationData(
            min_x=calibration_data["MIN_X"],
            max_x=calibration_data["MAX_X"],
            min_y=calibration_data["MIN_Y"],
            max_y=calibration_data["MAX_Y"],
            min_z=calibration_data["MIN_Z"],
            max_z=calibration_data["MAX_Z"]
        )

        self.magnetic_declination = settings.MAGNETIC_DECLINATION

    def save_calibration(self, filepath):
        # Save calibration data to a file
        pass

    def apply_calibration(self, x, y, z):
        # Apply calibration to raw data
        x_calibrated = self._normalize(x, self.calibration_data.min_x, self.calibration_data.max_x)
        y_calibrated = self._normalize(y, self.calibration_data.min_y, self.calibration_data.max_y)
        z_calibrated = self._normalize(z, self.calibration_data.min_z, self.calibration_data.max_z)
        return x_calibrated, y_calibrated, z_calibrated

    def _normalize(self, value, min_val, max_val):
        return (2 * (value - min_val) / (max_val - min_val)) - 1

    def calculate_heading(self, x, y):
        # Calculate the heading in radians
        heading_radians = math.atan2(y, x)
        # Convert the heading to degrees
        heading_degrees = math.degrees(heading_radians)
        # Normalize the heading to be in the range of 0 to 360 degrees
        if heading_degrees < 0:
            heading_degrees += 360
        # Apply magnetic declination
        heading_degrees += self.magnetic_declination
        # Normalize again to ensure it's within 0-360 degrees
        if heading_degrees >= 360:
            heading_degrees -= 360
        return heading_degrees