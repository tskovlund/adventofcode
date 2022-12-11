from readinput import readfile_and_split

visited = set()
h = [0, 0]
t = [0, 0]
for d, n in readfile_and_split(" "):
    n = int(n)
    for _ in range(n):
        match d:
            case "U":
                h[0] += 1
                if h[0] == t[0] + 2:
                    t[0] = h[0] - 1
                    t[1] = h[1]
            case "D":
                h[0] -= 1
                if h[0] == t[0] - 2:
                    t[0] = h[0] + 1
                    t[1] = h[1]
            case "L":
                h[1] += 1
                if h[1] == t[1] + 2:
                    t[1] = h[1] - 1
                    t[0] = h[0]
            case "R":
                h[1] -= 1
                if h[1] == t[1] - 2:
                    t[1] = h[1] + 1
                    t[0] = h[0]
        visited.add((t[0], t[1]))
print(len(visited))
