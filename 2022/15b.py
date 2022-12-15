from readinput import readfile_and_split
from collections import defaultdict

# MAX = 20
MAX = 4000000


def manhattan_distance(s, b):
    return abs(s[0] - b[0]) + abs(s[1] - b[1])


def merge_ranges(ranges, r_):
    if not ranges:
        return [r_]
    a_, b_ = r_
    for i, r in enumerate(ranges):
        a, b = r
        if b_ < a - 1:
            return ranges[:i] + [r_] + ranges[i:]
        if a_ > b + 1:
            continue
        return ranges[:i] + merge_ranges(ranges[i + 1 :], [min(a, a_), max(b, b_)])
    return ranges + [r_]


def add_ranges(ranges, s, d):
    sx, sy = s
    for y in range(max(0, sy - d), min(MAX, sy + d) + 1):
        a = abs(sy - y)
        b = d - a
        r = [max(0, sx - b), min(MAX, sx + b)]
        ranges[y] = merge_ranges(ranges[y], r)


ranges = defaultdict(list)

for i, line in enumerate(readfile_and_split()):
    print(i)
    sx = int(line[2][2:-1])
    sy = int(line[3][2:-1])
    bx = int(line[8][2:-1])
    by = int(line[9][2:])
    d = manhattan_distance((sx, sy), (bx, by))
    add_ranges(ranges, (sx, sy), d)

for k, r in ranges.items():
    if len(r) > 1:
        print(k, r)
        print(k + (r[0][1] + 1) * 4000000)
