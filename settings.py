import json
import os

_cur_dir = os.path.dirname(os.path.realpath(__file__))

ROOT_DIR = os.path.expanduser('~/.as')
os.makedirs(ROOT_DIR, exist_ok=True)

DEFAULT_CONFIG = {

}

CONFIG_FILE = os.path.join(ROOT_DIR, 'config.json')
if not os.path.exists(CONFIG_FILE):
    print("No config found! Creating the default one...")
    with open(CONFIG_FILE, 'w') as jp:
        json.dump(DEFAULT_CONFIG, jp, indent=2)


SERIAL_PORT = '/dev/ttyAMA0'
BAUD_RATE = 115200

Error_MSG = [
    "AutoSlasher is of bounds, manually drive to within the Field Boundary to start the field.",
    "AutoSlasher is of bounds, manually drive out of the exclusion zone to start the field."
]

DATABASE_PATH = "field_data"

GPS_STAT_MSG = [
    "GPS Quality: Excellent",
    "GPS Quality: Poor",
    "GPS Quality: Fault"
]

CALIBRATION = {
    "MIN_X": 962,
    "MAX_X": 2553,
    "MIN_Y": -1555,
    "MAX_Y": 27,
    "MIN_Z": -1015,
    "MAX_Z": 642
}

MAGNETIC_DECLINATION = 0.0
POSITION_TOLERANCE = 1.0

try:
    from local_settings import *
except ImportError:
    pass
