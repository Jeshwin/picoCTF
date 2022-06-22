#!/usr/bin/python3

from binascii import hexlify, unhexlify
FLAG = open('flag.txt').read().strip()
FLAG = int(hexlify(FLAG.encode()), 16)
print(unhexlify(str(hex(FLAG))[2:]))
