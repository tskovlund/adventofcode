from readinput import readfile_and_split
from functools import cache
from collections import defaultdict

MINUTES = 26

valves = {}
for line in readfile_and_split(" "):
    id = line[1]
    flow = int(line[4][5:-1])
    to = {id.rstrip(",") for id in line[9:]}
    valves[id] = (flow, to)

flowvalves = frozenset({id for id in valves.keys() if valves[id][0] > 0})


@cache
def search(current="AA", minutes=MINUTES, open=frozenset(), openflow=0):
    if minutes == 0:
        return {open: 0}
    if open == flowvalves:
        return {open: minutes + openflow}
    flow, to = valves[current]
    solutions = defaultdict(int)
    for valve in to:
        for open_, solution in search(valve, minutes - 1, open, openflow).items():
            solutions[open_] = max(solutions[open_], solution + openflow)
    if current not in open and flow > 0:
        open = set(open)
        open.add(current)
        for open_, solution in search(
            current, minutes - 1, frozenset(open), openflow + flow
        ).items():
            solutions[open_] = max(solutions[open_], solution + openflow)
    return solutions


# Find best solution for all open sets and find the
# best two solutions that don't have intersecting open sets
solutions = search().items()
best = 0
for open, solution in solutions:
    for open_, solution_ in solutions:
        if not open.intersection(open_):
            best = max(best, solution + solution_)
print(best)
