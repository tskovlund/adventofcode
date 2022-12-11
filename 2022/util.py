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