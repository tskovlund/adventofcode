from readinput import readfile_and_split

sand = (500, 0)
blocked = set()

min_x = None
max_x = None
max_y = None
for path in [
    [tuple(int(i) for i in m.split(",")) for m in p] for p in readfile_and_split(" -> ")
]:
    prev_x, prev_y = path[0]
    blocked.add((prev_x, prev_y))
    for x, y in path:

        # Find min and max
        if min_x is None:
            min_x = x
        if max_x is None:
            max_x = x
        if max_y is None:
            max_y = y
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

        # Build map
        if x > prev_x:
            for x_ in range(prev_x + 1, x + 1):
                blocked.add((x_, y))
        elif x < prev_x:
            for x_ in range(prev_x - 1, x - 1, -1):
                blocked.add((x_, y))
        elif y > prev_y:
            for y_ in range(prev_y + 1, y + 1):
                blocked.add((x, y_))
        elif y < prev_y:
            for y_ in range(prev_y - 1, y - 1, -1):
                blocked.add((x, y_))

        # Update prev
        prev_x = x
        prev_y = y

print(min_x, max_x, max_y)

assert sand not in blocked
count = 0
while True:
    pos = sand
    done = False
    while True:
        a = (pos[0], pos[1] + 1)
        b = (pos[0] - 1, pos[1] + 1)
        c = (pos[0] + 1, pos[1] + 1)
        if a not in blocked:
            pos = a
        elif b not in blocked:
            pos = b
        elif c not in blocked:
            pos = c
        else:
            blocked.add(pos)
            break
        if pos[0] < min_x or pos[0] > max_x or pos[1] > max_y:
            done = True
            break
    if done:
        break
    count += 1
print(count)
