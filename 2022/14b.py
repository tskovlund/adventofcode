from readinput import readfile_and_split

sand = (500, -1)
blocked = set()

max_y = 0

for path in [
    [tuple(int(i) for i in m.split(",")) for m in p] for p in readfile_and_split(" -> ")
]:
    prev_x, prev_y = path[0]
    blocked.add((prev_x, prev_y))
    for x, y in path:

        # Find max y
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

assert sand not in blocked
count = 0
while True:
    pos = sand
    done = False
    while True:
        a = (pos[0], pos[1] + 1)
        b = (pos[0] - 1, pos[1] + 1)
        c = (pos[0] + 1, pos[1] + 1)
        if a not in blocked and a[1] < max_y + 2:
            pos = a
        elif b not in blocked and a[1] < max_y + 2:
            pos = b
        elif c not in blocked and a[1] < max_y + 2:
            pos = c
        else:
            blocked.add(pos)
            if pos == (500, 0):
                done = True
            break
    if done:
        count += 1
        break
    count += 1
print(count)
