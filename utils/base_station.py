import serial
import time

def read_continuously(port_name):
    try:
        with serial.Serial(port_name, baudrate=38400, timeout=1) as ser:
            print(f"Reading continuous data from {port_name}...")
            while True:
                line = ser.readline().decode('ascii', errors='ignore').strip()
                if line:
                    print(f"Data: {line}")
    except serial.SerialException as e:
        print(f"Error reading from {port_name}: {e}")


if __name__ == "__main__":
    port_name = '/dev/ttyUSB0'  # Replace with the actual port
    read_continuously(port_name)