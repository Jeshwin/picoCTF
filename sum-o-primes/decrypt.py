#!/usr/bin/python3

from binascii import unhexlify

OUTPUT = open("output.txt", "r").read().strip()
x = int(OUTPUT.split()[2], 16)
n = int(OUTPUT.split()[5], 16)
c = int(OUTPUT.split()[8], 16)

totient = n - x + 1

e = 65537
d = pow(e, -1, totient)

answer = pow(c, d, n)
print(unhexlify(str(hex(answer))[2:]))
