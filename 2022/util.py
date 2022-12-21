def transpose(grid):
    grid_ = [[] for _ in range(len(grid[0]))]
    for row in grid:
        for i, el in enumerate(row):
            grid_[i].append(el)
    return grid_


def flip(grid, axis="vertical"):
    if axis == "vertical":
        return [list(reversed(row)) for row in grid]
    elif axis == "horizontal":
        return transpose(flip(transpose(grid)))


def neighbors_2d(x, y):
    n = set()
    for i in range(x - 1, x + 2):
        n.add(i, y)
    for j in range(y - 1, y + 2):
        n.add((x, j))
    n.remove((x, y))
    return n


def neighbors_3d(x, y, z):
    n = set()
    for i in range(x - 1, x + 2):
        n.add((i, y, z))
    for j in range(y - 1, y + 2):
        n.add((x, j, z))
    for k in range(z - 1, z + 2):
        n.add((x, y, k))
    n.remove((x, y, z))
    return n
