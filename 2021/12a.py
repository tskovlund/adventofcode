#!/usr/bin/env python3

import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


def count_paths(v, g, visited=set()):
    _visited = set()
    for item in visited:
        _visited.add(item)
    if v == "end":
        return 1
    if v == v.lower():
        _visited.add(v)
    count = 0
    for node in g[v]:
        if node not in _visited:
            count += count_paths(node, g, _visited)
    return count


graph = {}
with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        a, b = line[:-1].split("-")
        try:
            graph[a].add(b)
        except KeyError:
            graph[a] = {b}
        try:
            graph[b].add(a)
        except KeyError:
            graph[b] = {a}
    print(count_paths("start", graph))
