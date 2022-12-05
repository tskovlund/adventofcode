from readinput import readfile
from math import ceil


def popfront(stack, i):
    es = stack[:i]
    if len(stack) == i:
        stack = []
    else:
        stack = stack[i:]
    return es, stack


def pushfront(stack, es):
    stack = es + stack
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
    es, stacks[f] = popfront(stacks[f], m)
    stacks[t] = pushfront(stacks[t], es)
for stack in stacks:
    print(stack[0], end="")
print()