import serial
import pynmea2

# Replace '/dev/ttyACM0' with your device name (e.g., '/dev/ttyUSB0') and set the correct baud rate
serial_port = '/dev/ttyACM0'
baud_rate = 115200  # Change to the baud rate configured on your simpleRTK2B


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
                        print(data)
                        fixed_state = data.get("gps_qual") in [4, 5]
                        print(f"State:{fixed_state}")
                    except pynmea2.ParseError as e:
                        print(f"Parse error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    read_serial_data()