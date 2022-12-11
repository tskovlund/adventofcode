from readinput import readgrid
from util import transpose, flip


def find_visible_trees(grid, translate_indices, visible=set()):
    for i, row in enumerate(grid):
        max = row[0]
        visible.add(translate_indices(i, 0))
        for j, el in enumerate(row[1:]):
            if el > max:
                max = el
                visible.add(translate_indices(i, j + 1))
            if max == 9:
                continue
    return visible


grid = readgrid()
visible = find_visible_trees(grid, lambda i, j: (i, j))
visible = visible.union(find_visible_trees(transpose(grid), lambda i, j: (j, i)))
visible = visible.union(find_visible_trees(flip(grid), lambda i, j: (i, len(grid[0]) - 1 - j)))
visible = visible.union(find_visible_trees(flip(flip(transpose(grid)), axis="horizontal"), lambda i, j: (len(grid[0]) - 1 - j, len(grid) - 1 - i)))
print(len(visible))