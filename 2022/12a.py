from readinput import readfile

lines = readfile()
grid = []

# Map heights to ints
# and remember indices of S and E
start = None
end = None
for i, line in enumerate(lines):
    grid.append([])
    for j, c in enumerate(line):
        if c == "S":
            start = (i, j)
            grid[i].append(0)
        elif c == "E":
            end = (i, j)
            grid[i].append(ord("z") - ord("a"))
        else:
            grid[i].append(ord(c) - ord("a"))

# Do BFS
n = len(grid)
m = len(grid[0])
bfs = [(start[0], start[1], 0)]
visited = set()
node_ = None
while bfs:
    i, j, l = bfs.pop()
    if (i, j) in visited:
        continue
    h = grid[i][j]
    if i > 0:
        if grid[i - 1][j] <= h + 1:
            node_ = (i - 1, j, l + 1)
            if (node_[0], node_[1]) not in visited:
                if (node_[0], node_[1]) == end:
                    break
                bfs = [node_] + bfs
    if i < n - 1:
        if grid[i + 1][j] <= h + 1:
            node_ = (i + 1, j, l + 1)
            if (node_[0], node_[1]) not in visited:
                if (node_[0], node_[1]) == end:
                    break
                bfs = [node_] + bfs
    if j > 0:
        if grid[i][j - 1] <= h + 1:
            node_ = (i, j - 1, l + 1)
            if (node_[0], node_[1]) not in visited:
                if (node_[0], node_[1]) == end:
                    break
                bfs = [node_] + bfs
    if j < m - 1:
        if grid[i][j + 1] <= h + 1:
            node_ = (i, j + 1, l + 1)
            if (node_[0], node_[1]) not in visited:
                if (node_[0], node_[1]) == end:
                    break
                bfs = [node_] + bfs
    visited.add((i, j))
print(node_[2])
