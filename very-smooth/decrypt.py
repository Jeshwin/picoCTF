#!/usr/bin/python3

import math
from time import sleep
import sympy
from binascii import unhexlify

OUTPUT = open("output.txt").read().split()
n = int(OUTPUT[2], 16)
c = int(OUTPUT[5], 16)
e = 65537

print(f'n = {n}, length: {n.bit_length()}')
print(f'c = {c}. length: {c.bit_length()}')

# TODO: find m

# Use Pollard Rho algorithm
def pollard(num):
    x = 2**2047
    y = 2**2047
    g = 1

    def poly(s):
        return (s**2 + 1) % num

    cnt = 0
    while(g == 1):
        x = poly(x)
        y = poly(poly(y))
        g = math.gcd(abs(x - y), num)
        cnt += 1
        print('Current Count: ' + str(cnt))
        # print(str(x) + ', ' + str(y))

    if g == num:
        return -1
    return g


##############################
# Proof that Pollard Works   #
# x = 29599813 # 4283 * 6911 #
# print(pollard(x))          #
##############################

p = pollard(n)
q = n//p

m = (p - 1) * (q - 1)

d = pow(e, -1, m)
answer = hex(pow(c, d, n))
print(str(answer)[2:])
print(unhexlify(str(answer)[2:]))
