#!/usr/bin/env python3

import sys
import os
from collections import Counter

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

N = 50

def get_pixel(i, j, image, rows, cols, inf):
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return inf
    return image[i][j]


def enhance_pixel(p, i, j, image, rows, cols, s, inf):
    r1 = (
        get_pixel(i - 1, j - 1, image, rows, cols, inf)
        + get_pixel(i - 1, j, image, rows, cols, inf)
        + get_pixel(i - 1, j + 1, image, rows, cols, inf)
    )
    r2 = (
        get_pixel(i, j - 1, image, rows, cols, inf)
        + get_pixel(i, j, image, rows, cols, inf)
        + get_pixel(i, j + 1, image, rows, cols, inf)
    )
    r3 = (
        get_pixel(i + 1, j - 1, image, rows, cols, inf)
        + get_pixel(i + 1, j, image, rows, cols, inf)
        + get_pixel(i + 1, j + 1, image, rows, cols, inf)
    )
    n = int((r1 + r2 + r3).replace(".", "0").replace("#", "1"), 2)
    return s[n]


with open(filename) as f:
    s = f.readline()
    f.readline()
    image = [list(l.strip("\n")) for l in f.readlines()]
    inf = "."
    for i in range(N):
        rows = len(image)
        cols = len(image[0])
        output = []
        for j in range(rows + 2):
            output.append([])
            for _ in range(cols + 2):
                output[j].append(".")
        for j, row in enumerate(output):
            for k, pixel in enumerate(row):
                output[j][k] = enhance_pixel(pixel, j - 1, k - 1, image, rows, cols, s, inf)
        image = output
        if s[0] == "#":
            if i % 2 == 0:
                inf = "#"
            else:
                inf = "."
    for line in image:
        print("".join(line))
    c = Counter("".join(["".join(l) for l in image]))
    print(c)
