#!/usr/bin/env python3

import sys
import os
from statistics import mean

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


def distance(l, m):
    print(l, m)
    distances = map(lambda i: abs(i - m) * (abs(i - m) + 1) // 2, l)
    return int(sum(distances))


with open(filename) as f:
    line = list(map(int, f.readline().split(",")))
    m = round(mean(line))

    d = distance(line, m)
    while distance(line, m - 1) < d:
        m -= 1
        d = distance(line, m)
    while distance(line, m + 1) < d:
        m += 1
        d = distance(line, m)

    print(d)
