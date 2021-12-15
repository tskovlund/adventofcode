#!/usr/bin/env python3

import sys
import os

sys.setrecursionlimit(10000)

N = 1
INF = 10 ** 10

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


def dijkstra(node, end, min_distances, unvisited, visited=set()):
    i, j = node
    n = len(min_distances)
    w = min_distances[i][j]
    min_dist = INF
    if i < n - 1:
        min_distances[i + 1][j] = min(min_distances[i + 1][j], w + cave[i + 1][j])
    if j < n - 1:
        min_distances[i][j + 1] = min(min_distances[i][j + 1], w + cave[i][j + 1])
    if i > 0:
        min_distances[i - 1][j] = min(min_distances[i - 1][j], w + cave[i - 1][j])
    if j > 0:
        min_distances[i][j - 1] = min(min_distances[i][j - 1], w + cave[i][j - 1])
    
    unvisited.remove(node)
    visited.add(node)

    if node == end:
        return min_distances[-1][-1]

    n = min(unvisited, key=lambda n: min_distances[n[0]][n[1]])

    if n == INF:
        return min_distances[-1][-1]

    return dijkstra(n, end, min_distances, unvisited, visited=visited)


with open(filename) as f:
    cave = []
    min_distances = []
    lines = f.readlines()
    count = 0
    n = len(lines)
    for k in range(N):
        for _i, _line in enumerate(lines):
            line = _line.strip("\n")
            cave.append([0] * N * n)
            min_distances.append([INF] * N * n)
            for l in range(N):
                for _j, _w in enumerate(map(int, line)):
                    i = _i + k * n
                    j = _j + l * n
                    w = _w + k + l
                    if w > 9:
                        w = w % 10 + 1
                    cave[i][j] = w
    min_distances[0][0] = 0

    unvisited = set()
    for i, l in enumerate(min_distances):
        for j, w in enumerate(l):
            unvisited.add((i, j))

    print(dijkstra((0, 0), (n * N - 1, n * N - 1), min_distances, unvisited))
