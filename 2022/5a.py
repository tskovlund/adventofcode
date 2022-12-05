from readinput import readfile
from math import ceil


def popfront(stack):
    e = stack[0]
    if len(stack) == 1:
        stack = []
    else:
        stack = stack[1:]
    return e, stack


def pushfront(stack, e):
    stack = [e] + stack
    return stack


lines = readfile()
i = 0
n = ceil(len(lines[0]) / 4)
stacks = [[] for _ in range(n)]
while (line := lines[i]).startswith("["):
    for j in range(n):
        item = line[j * 4 + 1]
        if item != " ":
            stacks[j].append(item)
    i += 1
i += 2
for instruction in lines[i:]:
    m, f, t = map(int, filter(lambda e : e.isnumeric(), instruction.split(" ")))
    f -= 1
    t -= 1
    for i in range(m):
        e, stacks[f] = popfront(stacks[f])
        stacks[t] = pushfront(stacks[t], e)
for stack in stacks:
    print(stack[0], end="")
print()