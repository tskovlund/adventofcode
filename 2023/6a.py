from readinput import readfile_and_split

races = map(lambda t: (int(t[0]), int(t[1])), list(zip(*readfile_and_split(None)))[1:])

res = 1
for time, record in races:
    ways = 0
    for t in range(time):
        if (time - t) * t > record:
            ways += 1
    res *= ways
print(res)
