#!/usr/bin/env python

import serial
import time

port = "/dev/ttyUSB0"

initial_baudrate = 300
fast_baudrate = 19200  # 6

msg_start_communication = b"/?!\r\n"
msg_change_baudrate = b"\x060" + b"6" + b"0\r\n"
msg_stop_communication = b"\x01B0\x03q\r\n"
msg_last_message = b"!\r\n"

conn = serial.Serial(
    baudrate=initial_baudrate,
    bytesize=serial.SEVENBITS,
    stopbits=serial.STOPBITS_ONE,
    parity=serial.PARITY_EVEN,
)
conn.port = port

with conn as c:
    print("Connected to " + c.name + " at " + str(c.baudrate) + " bps")
    c.write(msg_start_communication)
    msg_code = c.readline()  # /SAT63511C01667006641\r\n
    print("Identification: " + str(msg_code))

    time.sleep(0.3)

    c.write(msg_change_baudrate)
    time.sleep(0.250)

conn.baudrate = fast_baudrate

with conn as c:
    print("Connected to " + c.name + " at " + str(c.baudrate) + " bps")

    while True:
        line = c.readline()

        if line == msg_last_message:
            break

        line = line.decode("UTF-8").strip()
        if line:
            print(line)
