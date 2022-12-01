import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You need to specify an input file")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        max_sum = 0
        current = 0
        while l := f.readline():
            l = l[:-1]
            if l == "":
                max_sum = max(current, max_sum)
                current = 0
                continue
            l = int(l)
            current += l
        max_sum = max(current, max_sum)
        print(max_sum)
