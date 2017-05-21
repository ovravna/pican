import can

bus = can.interface.Bus(channel='vcan0', bustype='socketcan_native')
msg = can.Message(arbitration_id=0x64,
                  data=[0, 1, 2, 3, 4, 5],
                  extended_id=False)
bus.send(msg)
