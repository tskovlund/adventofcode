from readinput import readfile_and_split

visited = set()
knots = [[0, 0] for _ in range(10)]
for d, n in readfile_and_split(" "):
    n = int(n)
    for _ in range(n):
        match d:
            case "U":
                knots[0][0] += 1
            case "D":
                knots[0][0] -= 1
            case "L":
                knots[0][1] += 1
            case "R":
                knots[0][1] -= 1
        for k in range(1, 10):
            i, j = knots[k - 1]
            if knots[k][0] < i - 1:
                knots[k][0] += 1
                if knots[k][1] < j:
                    knots[k][1] += 1
                if knots[k][1] > j:
                    knots[k][1] -= 1
            if knots[k][0] > i + 1:
                knots[k][0] -= 1
                if knots[k][1] < j:
                    knots[k][1] += 1
                if knots[k][1] > j:
                    knots[k][1] -= 1
            if knots[k][1] < j - 1:
                knots[k][1] += 1
                if knots[k][0] < i:
                    knots[k][0] += 1
                if knots[k][0] > i:
                    knots[k][0] -= 1
            if knots[k][1] > j + 1:
                knots[k][1] -= 1
                if knots[k][0] < i:
                    knots[k][0] += 1
                if knots[k][0] > i:
                    knots[k][0] -= 1
        visited.add((knots[9][0], knots[9][1]))
print(len(visited))
