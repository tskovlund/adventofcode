import sys
import os
from statistics import median

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

points = {")": 1, "]": 2, "}": 3, ">": 4}

brackets = {")": "(", "]": "[", "}": "{", ">": "<"}

_brackets = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

with open(filename) as f:
    lines = f.readlines()
    scores = []
    for line in lines:
        stack = []
        cont = False
        for bracket in line[:-1]:
            if bracket in _brackets.keys():
                stack.append(bracket)
            else:
                if stack[-1] != brackets[bracket]:
                    cont = True
                    break
                else:
                    stack.pop()
        if cont:
            continue
        stack = list(reversed(list(map(lambda b: _brackets[b], stack))))
        score = 0
        for b in stack:
            score *= 5
            score += points[b]
        scores.append(score)
    print(median(scores))
