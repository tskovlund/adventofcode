#!/usr/bin/env python3

import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


def count(c, patterns):
    count = 0
    for p in patterns:
        if c in p:
            count += 1
    return count


with open(filename) as f:
    lines = f.readlines()
    result = 0
    for line in lines:
        mapping = dict()
        line = line.split(" | ")
        patterns = list(sorted(line[0].split(), key=lambda p: len(p)))
        output = line[1].split()

        mapping[[c for c in patterns[1] if c not in patterns[0]][0]] = "a"

        for c in patterns[0]:
            if count(c, patterns) == 8:
                mapping[c] = "c"
            else:
                mapping[c] = "f"

        for c in [c for c in "abcdefg" if c not in mapping.keys()]:
            if count(c, patterns) == 6:
                mapping[c] = "b"
            if count(c, patterns) == 4:
                mapping[c] = "e"

        for c in [c for c in "abcdefg" if c not in mapping.keys()]:
            if c in patterns[2]:
                mapping[c] = "d"
            else:
                mapping[c] = "g"

        digits = {
            "abcefg": "0",
            "cf": "1",
            "acdeg": "2",
            "acdfg": "3",
            "bcdf": "4",
            "abdfg": "5",
            "abdefg": "6",
            "acf": "7",
            "abcdefg": "8",
            "abcdfg": "9",
        }

        n = []
        for o in output:
            mapped_o = "".join(list(sorted(map(lambda c: mapping[c], o))))
            n.append(digits[mapped_o])

        result += int("".join(n))
    print(result)
