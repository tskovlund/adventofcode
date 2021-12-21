#!/usr/bin/env python3

import sys
import os
import functools
from itertools import product

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


@functools.cache
def wins(p1, p2, s1, s2, turn):
    total = 0
    w = 0
    rolls = product(range(1, 4), repeat=3)
    for roll in rolls:
        p = (p1 + (sum(roll) - 1)) % 10 + 1
        if s1 + p >= 21:
            w += turn
            total += 1
        else:
            _w, _total = wins(p2, p, s2, s1 + p, not turn)
            w += _w
            total += _total
    return w, total


with open(filename) as f:
    p1, p2 = [int(l.strip("\n").split(": ")[1]) for l in f.readlines()]
    w, total = wins(p1, p2, 0, 0, True)
    print(max(w, total - w))
