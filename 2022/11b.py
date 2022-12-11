from readinput import readfile
import math

lines = readfile()

monkeys = []

M = 1

for i in range(1, len(lines), 7):
    monkey = [l.lstrip() for l in lines[i : i + 5]]
    s = list(map(int, monkey[0].lstrip("Starting items: ").split(", ")))
    op, opr = monkey[1].split(" ")[4:]
    m = int(monkey[2].split(" ")[-1])
    t = int(monkey[3].split(" ")[-1])
    f = int(monkey[4].split(" ")[-1])
    monkeys.append([s, op, opr, m, t, f])
    M *= m

inspected = [0 for _ in range(len(monkeys))]
for _ in range(10000):
    for m, monkey in enumerate(monkeys):
        for item in monkey[0]:
            inspected[m] += 1
            op, opr = monkey[1:3]
            if opr == "old":
                item *= item
            elif op == "+":
                item += int(opr)
            else:
                item *= int(opr)
            if item % monkey[3] == 0:
                monkeys[monkey[4]][0].append(item % M)
            else:
                monkeys[monkey[5]][0].append(item % M)
        monkey[0] = []
print(math.prod(sorted(inspected)[-2:]))
