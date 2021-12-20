#!/usr/bin/env python3

import sys
import os
from collections import Counter

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

N = 2
inf = "."

def get_pixel(i, j, image, rows, cols):
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return inf
    return image[i][j]


def enhance_pixel(p, i, j, image, rows, cols, s):
    r1 = (
        get_pixel(i - 1, j - 1, image, rows, cols)
        + get_pixel(i - 1, j, image, rows, cols)
        + get_pixel(i - 1, j + 1, image, rows, cols)
    )
    r2 = (
        get_pixel(i, j - 1, image, rows, cols)
        + get_pixel(i, j, image, rows, cols)
        + get_pixel(i, j + 1, image, rows, cols)
    )
    r3 = (
        get_pixel(i + 1, j - 1, image, rows, cols)
        + get_pixel(i + 1, j, image, rows, cols)
        + get_pixel(i + 1, j + 1, image, rows, cols)
    )
    n = int((r1 + r2 + r3).replace(".", "0").replace("#", "1"), 2)
    return s[n]


with open(filename) as f:
    s = f.readline()
    f.readline()
    image = [list(l.strip("\n")) for l in f.readlines()]
    for i in range(N):
        rows = len(image)
        cols = len(image[0])
        output = []
        for i in range(rows + 2):
            output.append([])
            for _ in range(cols + 2):
                output[i].append(".")
        for i, row in enumerate(output):
            for j, pixel in enumerate(row):
                output[i][j] = enhance_pixel(pixel, i - 1, j - 1, image, rows, cols, s)
        image = output
    for line in image:
        print("".join(line))
    c = Counter("".join(["".join(l) for l in image]))
    print(c)
