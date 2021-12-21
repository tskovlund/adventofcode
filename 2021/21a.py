#!/usr/bin/env python3

import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    p1, p2 = [int(l.strip("\n").split(": ")[1]) for l in f.readlines()]
    die = 1
    rolls = 0
    scores = [0, 0]
    while True:
        for _ in range(3):
            p1 += die
            p1 = (p1 - 1) % 10 + 1
            die = die % 100 + 1
            rolls += 1
        scores[0] += p1
        if scores[0] >= 1000:
            break
        for _ in range(3):
            p2 += die
            p2 = (p2 - 1) % 10 + 1
            die = die % 100 + 1
            rolls += 1
        scores[1] += p2
        if scores[1] >= 1000:
            break
    print(min(scores), rolls)
    print(min(scores) * rolls)
