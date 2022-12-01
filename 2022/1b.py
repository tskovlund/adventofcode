import sys


def update_max_sums(max_sums, current):
    for i, s in enumerate(max_sums):
        if current > s:
            max_sums[i] = current
            break
    return list(sorted(max_sums))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You need to specify an input file")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        max_sums = [0, 0, 0]
        current = 0
        while l := f.readline():
            l = l[:-1]
            if l == "":
                max_sums = update_max_sums(max_sums, current)
                current = 0
                continue
            l = int(l)
            current += l
        max_sums = update_max_sums(max_sums, current)
        print(max_sums)
        print(sum(max_sums))
