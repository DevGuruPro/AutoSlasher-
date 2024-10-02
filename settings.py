import json
import os

_cur_dir = os.path.dirname(os.path.realpath(__file__))

ROOT_DIR = os.path.expanduser('~/.eol')
os.makedirs(ROOT_DIR, exist_ok=True)

DEFAULT_CONFIG = {

}

CONFIG_FILE = os.path.join(ROOT_DIR, 'config.json')
if not os.path.exists(CONFIG_FILE):
    print("No config found! Creating the default one...")
    with open(CONFIG_FILE, 'w') as jp:
        json.dump(DEFAULT_CONFIG, jp, indent=2)


serial_port = '/dev/ttyAMA0'
baud_rate = 115200

Error_MSG = {
    "AutoSlasher is of bounds, manually drive to within the Field Boundary to start the field.",
    "AutoSlasher is of bounds, manually drive out of the exclusion zone to start the field."
}

GPS_STAT_MSG = {
    "GPS Good",
    "GPS Bad"
}

try:
    from local_settings import *
except ImportError:
    pass
