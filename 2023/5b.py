from readinput import readfile_and_split


def is_in_range(n, r):
    return r[0] <= n < r[1]


class RangeDict(dict):
    def __getitem__(self, key):
        for src, dest in super().items():
            if is_in_range(key, src):
                return dest + key - src[0]
        return key


def lookup_seed(key, maps):
    map = maps[0]
    if len(maps) == 1:
        return map[key]
    return lookup_seed(map[key], maps[1:])


lines = readfile_and_split()

seeds = list(map(int, lines[0][1:]))
seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))

maps = []
n = len(lines)
i = 1
while i < n:
    line = lines[i]
    if line == [""]:
        i += 2
        maps = [RangeDict()] + maps
        continue
    dest_start, source_start, length = map(int, line)
    maps[0][(dest_start, dest_start + length)] = source_start
    i += 1

x = 0
while True:
    s = lookup_seed(x, maps)
    for seed_range in seed_ranges:
        if is_in_range(s, seed_range):
            print(x)
            exit()
    x += 1
