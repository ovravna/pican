import socket

from struct import pack, unpack

s = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
s.bind(('vcan0',))

# packet = struct.pack("<IB3x8s", 0x741, len(b"hello"), b"hello")

# msg = s.recv(256)


# print(hex(82990))
print([n for n in pack('!I', 82990)])

# print(list(hex(m) for m in msg))
# for n in msg:
#
# 	print(hex(n))

# ID ID 00 00 DL 00 00 00 00 DT DT ...

