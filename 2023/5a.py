from readinput import readfile_and_split


def is_in_range(n, r):
    return r[0] <= n < r[1]


class RangeDict(dict):
    def __getitem__(self, key):
        for src, dest in super().items():
            if is_in_range(key, src):
                return dest + key - src[0]
        return key


def lookup_location(key, maps):
    map = maps[0]
    if len(maps) == 1:
        return map[key]
    return lookup_location(map[key], maps[1:])


lines = readfile_and_split()
seeds = map(int, lines[0][1:])

maps = []
n = len(lines)
i = 1
j = -1
while i < n:
    line = lines[i]
    if line == [""]:
        j += 1
        i += 2
        maps.append(RangeDict())
        continue
    dest_start, source_start, length = map(int, line)
    maps[j][(source_start, source_start + length)] = dest_start
    i += 1

res = lookup_location(next(seeds), maps)
for seed in seeds:
    res = min(res, lookup_location(seed, maps))
print(res)
