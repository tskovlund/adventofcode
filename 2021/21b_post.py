#!/usr/bin/env python3

import sys
import os
import functools
from itertools import product

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


@functools.cache
def wins(p1, p2, turn, s1, s2):
    w1, w2 = [0, 0]
    rolls = product(range(1, 4), repeat=3)
    if turn == 0:
        for roll in rolls:
            p = (p1 + (sum(roll) - 1)) % 10 + 1
            if s1 + p >= 21:
                w1 += 1
            else:
                _w1, _w2 = wins(p, p2, 1, s1 + p, s2)
                w1 += _w1
                w2 += _w2
    if turn == 1:
        for roll in rolls:
            p = (p2 + (sum(roll) - 1)) % 10 + 1
            if s2 + p >= 21:
                w2 += 1
            else:
                _w1, _w2 = wins(p1, p, 0, s1, s2 + p)
                w1 += _w1
                w2 += _w2
    return w1, w2


with open(filename) as f:
    p1, p2 = [int(l.strip("\n").split(": ")[1]) for l in f.readlines()]
    print(wins(p1, p2, 0, 0, 0))
