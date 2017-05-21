import can

bus = can.interface.Bus(channel='vcan0', bustype='socketcan_native')
notifier = can.Notifier(bus, [can.Printer()])

