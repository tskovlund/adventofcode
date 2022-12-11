from readinput import readgrid
from util import transpose, flip
from collections import defaultdict


def find_candidates(grid, translate_indices, scores=defaultdict(lambda: 1)):
    active = []
    for i, row in enumerate(grid):
        for el in active:
            scores[el[2]] *= el[1]
        active = []
        for j, height in enumerate(row):
            remove = []
            for k, el in enumerate(active):
                if el[0] <= height:
                    scores[el[2]] *= el[1] + 1
                    remove.append(k)
                else:
                    el[1] += 1
            for l, k in enumerate(remove):
                active.pop(k - l)
            active.append([height, 0, translate_indices(i, j)])
    return scores


grid = readgrid()
scores = find_candidates(grid, lambda i, j: (i, j))
scores = find_candidates(transpose(grid), lambda i, j: (j, i), scores=scores)
scores = find_candidates(
    flip(grid), lambda i, j: (i, len(grid[0]) - 1 - j), scores=scores
)
scores = find_candidates(
    flip(flip(transpose(grid)), axis="horizontal"),
    lambda i, j: (len(grid[0]) - 1 - j, len(grid) - 1 - i),
    scores=scores,
)
print(max(scores.values()))
