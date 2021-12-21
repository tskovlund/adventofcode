#!/usr/bin/env python3

import sys
import os
import functools

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


@functools.cache
def wins(p1, p2, turn, scores):
    w = [0, 0]
    if turn == 0:
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    _p1 = p1
                    _scores = scores
                    _p1 += i
                    _p1 = (_p1 - 1) % 10 + 1
                    _p1 += j
                    _p1 = (_p1 - 1) % 10 + 1
                    _p1 += k
                    _p1 = (_p1 - 1) % 10 + 1
                    _scores = (_scores[0] + _p1, _scores[1])
                    if _scores[0] >= 21:
                        w[0] += 1
                    else:
                        w1, w2 = wins(_p1, p2, 1, _scores)
                        w[0] += w1
                        w[1] += w2
    if turn == 1:
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    _p2 = p2
                    _scores = scores
                    _p2 += i
                    _p2 = (_p2 - 1) % 10 + 1
                    _p2 += j
                    _p2 = (_p2 - 1) % 10 + 1
                    _p2 += k
                    _p2 = (_p2 - 1) % 10 + 1
                    _scores = (_scores[0], _scores[1] + _p2)
                    if _scores[1] >= 21:
                        w[1] += 1
                    else:
                        w1, w2 = wins(p1, _p2, 0, _scores)
                        w[0] += w1
                        w[1] += w2
    return w


with open(filename) as f:
    p1, p2 = [int(l.strip("\n").split(": ")[1]) for l in f.readlines()]
    print(wins(p1, p2, 0, (0, 0)))
