from time import sleep

import can
import math

import struct

bus = can.interface.Bus(channel='vcan0', bustype='socketcan_native')
i = 0


def send():
    global i
    i += 0.5
    v = int(40 * math.sin(i) + 50)
    print(v)
    m = [n for n in struct.pack('I', v)]
    msg = can.Message(arbitration_id=0x7b,
                      data=m,
                      extended_id=False)
    bus.send(msg)
    sleep(0.001)


def sending():
    while True:
        send()
