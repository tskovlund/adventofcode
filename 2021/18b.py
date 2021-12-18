#!/usr/bin/env python3

import sys
import os
import math
import copy

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


def add(m, n):
    return [m, n]


def left_add(n, m):
    try:
        left, right = n
        return [left_add(left, m), right]
    except TypeError:
        return n + m


def right_add(n, m):
    try:
        left, right = n
        return [left, right_add(right, m)]
    except TypeError:
        return n + m


def explode_nested_pair(n, d=0):
    try:
        left, right = n
        if d == 4:
            return True, [left, right]
        # Try explode left
        r, e = explode_nested_pair(left, d=d + 1)
        if r:
            left_explode, right_explode = e
            if d == 3:
                n[0] = 0
            if right_explode:
                n[1] = left_add(right, right_explode)
            return True, [left_explode, None]
        # Try explode right
        r, e = explode_nested_pair(right, d=d + 1)
        if r:
            left_explode, right_explode = e
            if d == 3:
                n[1] = 0
            if left_explode:
                n[0] = right_add(left, left_explode)
            return True, [None, right_explode]
        # If no explode
        return False, None
    except TypeError:
        # If n is a value
        return False, None


def split_number(n):
    try:
        left, right = n
        r, n = split_number(left)
        if r:
            return True, [n, right]
        r, n = split_number(right)
        if r:
            return True, [left, n]
        return False, [left, right]
    except TypeError:
        if n >= 10:
            return True, [math.floor(n / 2), math.ceil(n / 2)]
        return False, n


def reduce_number(n):
    while True:
        r, _ = explode_nested_pair(n)
        while r:
            r, _ = explode_nested_pair(n)
        r, n = split_number(n)
        if not r:
            return n


def magnitude(n):
    try:
        left, right = n
        return 3 * magnitude(left) + 2 * magnitude(right)
    except TypeError:
        return n


with open(filename) as f:
    numbers = [eval(line.strip("\n")) for line in f]
    max_magnitude = 0
    for n in numbers:
        for m in numbers:
            max_magnitude = max(
                max_magnitude,
                magnitude(reduce_number(add(copy.deepcopy(n), copy.deepcopy(m)))),
            )
    print(max_magnitude)
