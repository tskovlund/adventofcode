#!/usr/bin/env python3

import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    numbers = f.readlines()
    gamma = [0] * (len(numbers[0]) - 1)
    epsilon = [0] * (len(numbers[0]) - 1)
    for number in numbers:
        for i, bit in enumerate(number[:-1]):
            gamma[i] += int(bit)
    for i, bit in enumerate(gamma):
        if gamma[i] > len(numbers) / 2:
            gamma[i] = 2 ** (len(gamma) - i - 1)
            epsilon[i] = 0
        else:
            epsilon[i] = 2 ** (len(gamma) - i - 1)
            gamma[i] = 0
    gamma = sum(gamma)
    epsilon = sum(epsilon)
    print(gamma * epsilon)
