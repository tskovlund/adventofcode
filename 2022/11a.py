from readinput import readfile
import math

lines = readfile()

monkeys = []

for i in range(1, len(lines), 7):
    monkey = [l.lstrip() for l in lines[i : i + 5]]
    s = list(map(int, monkey[0].lstrip("Starting items: ").split(", ")))
    op, opr = monkey[1].split(" ")[4:]
    m = int(monkey[2].split(" ")[-1])
    t = int(monkey[3].split(" ")[-1])
    f = int(monkey[4].split(" ")[-1])
    monkeys.append([s, op, opr, m, t, f])

inspected = [0 for _ in range(len(monkeys))]
for _ in range(20):
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
            item = item // 3
            if item % monkey[3] == 0:
                monkeys[monkey[4]][0].append(item)
            else:
                monkeys[monkey[5]][0].append(item)
        monkey[0] = []
print(math.prod(sorted(inspected)[-2:]))
