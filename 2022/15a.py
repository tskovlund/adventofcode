from readinput import readfile_and_split

# Y = 10
Y = 2000000


def manhattan_distance(s, b):
    return abs(s[0] - b[0]) + abs(s[1] - b[1])


def find_range(s, d, Y):
    sx, sy = s
    assert sy <= Y <= sy + d or sy - d <= Y <= sy
    a = abs(sy - Y)
    b = d - a
    assert b >= 0
    return set(range(sx - b, sx + b + 1))


beacons = set()
empty_ranges = set()
for i, line in enumerate(readfile_and_split()):
    print(i)
    sx = int(line[2][2:-1])
    sy = int(line[3][2:-1])
    bx = int(line[8][2:-1])
    by = int(line[9][2:])
    d = manhattan_distance((sx, sy), (bx, by))

    if sy - d > Y or sy + d < Y:
        continue

    if by == Y:
        beacons.add((bx, by))

    empty_ranges = empty_ranges.union(find_range((sx, sy), d, Y))

print(len(empty_ranges) - len(beacons))
