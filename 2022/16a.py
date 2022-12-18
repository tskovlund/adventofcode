from readinput import readfile_and_split
from functools import cache

MINUTES = 30

valves = {}
for line in readfile_and_split(" "):
    id = line[1]
    flow = int(line[4][5:-1])
    to = [id.rstrip(",") for id in line[9:]]
    valves[id] = (flow, to)


@cache
def search(current="AA", minutes=MINUTES, open=frozenset(), openflow=0):
    if minutes == 0:
        return 0
    flow, to = valves[current]
    solution = 0
    for valve in to:
        solution = max(solution, openflow + search(valve, minutes - 1, open, openflow))
    if current not in open and flow > 0:
        open = set(open)
        open.add(current)
        solution = max(
            solution,
            openflow + search(current, minutes - 1, frozenset(open), openflow + flow),
        )
    return solution


print(search())
