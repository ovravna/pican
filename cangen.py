from time import sleep, time

import can
import math

import struct

bus = can.interface.Bus(channel='vcan0', bustype='socketcan_native')
i = 0
n = 0
t = time()
p = math.pi / 8

def send():
    global i, n, t, p
    i += p
    v = int(40 * math.sin(i*0.25) + 50)
    # print(v)
    m = [n for n in struct.pack('I', v)]
    msg = can.Message(arbitration_id=0x7b,
                      data=m,
                      extended_id=False)
    bus.send(msg)
    sleep(0.0005)
    n += 1

    if n % 1000 == 999:
        t1 = time()
        print('Transfer rate: ', 160000/(t1 - t))
        t = t1



def sending():
    print('Start sender')
    global t
    t = time()
    while True:
        send()
