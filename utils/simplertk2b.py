import serial
import pynmea2
from extractLocation import extract_from_gps

from utils.logger import logger

serial_port = '/dev/ttyAMA0'
baud_rate = 115200


def read_serial_data():
    data = {}
    try:
        with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
            while True:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if line.startswith('$GNGGA'):
                    try:
                        msg = pynmea2.parse(line)
                        for field in msg.fields:
                            label, attr = field[:2]
                            value = getattr(msg, attr)
                            data[attr] = value
                        x, y = extract_from_gps(data)
                        logger.info(f"Location : {x},{y}")
                    except pynmea2.ParseError as e:
                        logger.error(f"Parse error: {e}")
    except Exception as e:
        logger.error(f"Error: {e}")


if __name__ == '__main__':
    read_serial_data()
