import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You need to specify an input file")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        print(sum(sorted([sum([int(e[:-1]) for e in g.split(":")]) for g in ":".join(f.readlines()).split(":\n:")])[-3:]))
