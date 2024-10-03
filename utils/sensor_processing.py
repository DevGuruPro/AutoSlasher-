# sensor_processing.py

import math

class HeadingCalculator:
    def __init__(self):
        pass

    def calculate_heading(self, x, y):
        heading = math.atan2(y, x) * (180 / math.pi)
        if heading < 0:
            heading += 360
        return heading
