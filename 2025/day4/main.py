with open("input.txt", "r") as f:
    s = f.read().strip()


def nbr_stacks_around(grid, x, y):
    res = 0
    if x != 0:
        res += grid[y][x - 1] == "@"
        if y != 0:
            res += grid[y - 1][x - 1] == "@"
        if y != len(grid) - 1:
            res += grid[y + 1][x - 1] == "@"
    if x != len(grid[y]) - 1:
        res += grid[y][x + 1] == "@"
        if y != 0:
            res += grid[y - 1][x + 1] == "@"
        if y != len(grid) - 1:
            res += grid[y + 1][x + 1] == "@"
    if y != 0:
        res += grid[y - 1][x] == "@"
    if y != len(grid) - 1:
        res += grid[y + 1][x] == "@"

    return res


grid = [[c for c in row] for row in s.split("\n")]

# Part 1
res = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "@":
            res += nbr_stacks_around(grid, x, y) < 4

print(res)

# Part 2
total = 0
while True:
    rm_pos = set()

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                if nbr_stacks_around(grid, x, y) < 4:
                    rm_pos.add((x, y))

    for x, y in rm_pos:
        grid[y][x] = "."

    if len(list(rm_pos)) == 0:
        break
    total += len(list(rm_pos))

print(total)
