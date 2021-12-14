#!/usr/bin/env python3

import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


def to_decimal(b):
    d = 0
    for i, bit in enumerate(b):
        d += int(bit) * 2 ** (len(b) - i - 1)
    return d


with open(filename) as f:
    oxy_numbers = f.readlines()
    co2_numbers = oxy_numbers
    i = 0
    while len(oxy_numbers) > 1:
        s = 0
        for number in oxy_numbers:
            s += int(number[i])
        s = int(s >= len(oxy_numbers) / 2)
        oxy_numbers = list(filter(lambda n: int(n[i]) == s, oxy_numbers))
        i += 1
    i = 0
    while len(co2_numbers) > 1:
        s = 0
        for number in co2_numbers:
            s += int(number[i])
        s = int(s < len(co2_numbers) / 2)
        co2_numbers = list(filter(lambda n: int(n[i]) == s, co2_numbers))
        i += 1
    print(to_decimal(oxy_numbers[0][:-1]) * to_decimal(co2_numbers[0][:-1]))
