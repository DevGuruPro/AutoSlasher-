import serial

from settings import base_port


def stream_rtcm(base_serial):
    while True:
        data = base_serial.read(1000)
        print(data)


if __name__ == "__main__":

    base_serial = serial.Serial(base_port, baudrate=38400, timeout=1)

    try:
        stream_rtcm(base_serial)
    except KeyboardInterrupt:
        print("Stopping RTCM streaming.")
    finally:
        base_serial.close()
