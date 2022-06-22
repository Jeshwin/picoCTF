#!/usr/bin/python3

from binascii import hexlify
from gmpy2 import *
from time import sleep
import math
import os
import sys

e = 65537

def get_prime(state, bits):
    return next_prime(mpz_urandomb(state, bits) | (1 << (bits - 1)))

def get_smooth_prime(state, bits, smoothness=16):
    p = mpz(2)
    p_factors = [p]
    while p.bit_length() < bits - 2 * smoothness:
        factor = get_prime(state, smoothness)
        p_factors.append(factor)
        # print('New Factor(s): ' + str(factor.digits(16)))
        p *= factor
        # print('bLength: ' + str(p.bit_length()))
        # sleep(0.1)

    bitcnt = (bits - p.bit_length()) // 2
    # print('Current Bit Count Left: ' + str(bitcnt))

    loop_cnt = 0
    while True:
        prime1 = get_prime(state, bitcnt)
        # print('New Prime #1: ' + str(prime1))
        prime2 = get_prime(state, bitcnt)
        # print('New Prime #2: ' + str(prime2))
        tmpp = p * prime1 * prime2
        # print('Temporary p: ' + str(tmpp))
        if tmpp.bit_length() < bits:
            bitcnt += 1
            loop_cnt += 1
            # print('Current Bit Count of p: ' + str(bitcnt))
            continue
        if tmpp.bit_length() > bits:
            bitcnt -= 1
            loop_cnt += 1
            # print('Current Bit Count of p: ' + str(bitcnt))
            continue
        if is_prime(tmpp + 1):
            # print('Retries: ' + str(loop_cnt))
            p_factors.append(prime1)
            p_factors.append(prime2)
            # print('New Factor(s): ' + str(prime1.digits(16)) + ', ' + str(prime2.digits(16)))
            p = tmpp + 1
            print('Final prime: ' + str(p.digits(16)))
            print('Bit Length: ' + str(p.bit_length()))
            break

    p_factors.sort()
    # print(p_factors)
    print('# of Factors: ' + str(len(p_factors)))

    return (p, p_factors)

FLAG  = open('flag.txt').read().strip()
FLAG  = mpz(hexlify(FLAG.encode()), 16)
SEED  = mpz(hexlify(os.urandom(32)).decode(), 16)
STATE = random_state(SEED)

p, p_factors = get_smooth_prime(STATE, 1024, 16)
print()
q, q_factors = get_smooth_prime(STATE, 1024, 17)
n = p * q
print()
print('n: ' + str(n.digits(16)))
print(n.bit_length())
