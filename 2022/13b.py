from readinput import readfile
from functools import cmp_to_key


def compare(left_, right_):
    left = list(reversed(left_))
    right = list(reversed(right_))
    while left and right:
        l = left.pop()
        r = right.pop()
        if isinstance(l, int):
            if isinstance(r, int):
                if l < r:
                    return -1
                if r < l:
                    return 1
            else:
                left.append([l])
                right.append(r)
        elif isinstance(r, int):
            right.append([r])
            left.append(l)
        else:
            c = compare(l, r)
            if c != 0:
                return c
    if left and not right:
        return 1
    if right and not left:
        return -1
    return 0


packet1 = [[2]]
packet2 = [[6]]
lines = (
    [eval(line) for line in filter(lambda line: line, readfile())]
    + [packet1]
    + [packet2]
)
sorted_lines = sorted(lines, key=cmp_to_key(compare))
print((sorted_lines.index(packet1) + 1) * (sorted_lines.index(packet2) + 1))
