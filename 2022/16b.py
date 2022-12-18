from readinput import readfile_and_split
from functools import cache

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
        return {(0, open)}
    if open == flowvalves:
        return {(minutes * openflow, open)}
    flow, to = valves[current]
    solutions = set()
    for i, valve in enumerate(to):
        if minutes == MINUTES:
            print(i)
        solutions_ = search(valve, minutes - 1, open, openflow)
        solutions_ = {(openflow + solution[0], solution[1]) for solution in solutions_}
        solutions = solutions.union(solutions_)
    if current not in open and flow > 0:
        open = set(open)
        open.add(current)
        solutions_ = search(current, minutes - 1, frozenset(open), openflow + flow)
        solutions_ = {(openflow + solution[0], solution[1]) for solution in solutions_}
        solutions = solutions.union(solutions_)
    return solutions


# Find all possible outcomes and find the best two solutions that don't have intersecting open sets
solutions = sorted(
    filter(lambda s: s[0] > 400, search()), key=lambda s: s[0], reverse=True
)
print(len(solutions))
# Caution: The code below takes a long time to compute
# but it returns the correct result and I don't feel like
# optimizing it more right now even though I could probably
# just iterate smarter through the sorted list :>
best = 0
i = 0
for s, o in solutions:
    if i % 1000 == 0:
        print(i)
    i += 1
    for s_, o_ in solutions:
        if not o.intersection(o_):
            best = max(best, s + s_)
            break
print(best)
