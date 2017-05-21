from binascii import unhexlify

def arrayify(num):
	hex_str = hex(num)
	if len(hex_str) % 2 != 0:
		hex_str = hex_str[:2]+ '0' + hex_str[2:]



