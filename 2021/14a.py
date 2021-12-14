#!/usr/bin/env python3

import sys
import os
from collections import Counter, defaultdict

N = 10

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    template = f.readline().strip("\n")
    pair_count = Counter()
    for i in range(len(template) - 1):
        pair_count[template[i : i + 2]] += 1

    f.readline()
    rules = defaultdict(lambda: None)
    for line in f:
        pair, rule = line.strip("\n").split(" -> ")
        rules[pair] = rule

    for i in range(N):
        for pair, count in pair_count.copy().items():
            rule = rules[pair]
            if rule:
                pair_count[pair[0] + rule] += count
                pair_count[rule + pair[1]] += count
                pair_count[pair] -= count
    print(pair_count)

    character_count = Counter()
    for pair, count in pair_count.items():
        character_count[pair[0]] += count
        character_count[pair[1]] += count

    for c, count in character_count.items():
        character_count[c] //= 2
    start = template[0]
    end = template[-1]
    character_count.update([start, end])
    print(character_count)

    print(character_count.most_common()[0][1] - character_count.most_common()[-1][1])
