import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

brackets = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

with open(filename) as f:
    lines = f.readlines()
    p = 0
    for line in lines:
        stack = []
        for bracket in line[:-1]:
            if bracket in brackets.values():
                stack.append(bracket)
            else:
                if stack[-1] != brackets[bracket]:
                    p += points[bracket]
                    break
                else:
                    stack.pop()
    print(p)
