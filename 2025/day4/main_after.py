import numpy as np
from scipy.signal import convolve2d

with open("test_input.txt", "r") as f:
    s = f.read().strip()

grid = np.array([[1 if c == "@" else 0 for c in row] for row in s.split("\n")])

# Part 1
kernel = np.ones((3, 3), dtype=int)
kernel[1, 1] = 0  # zero out center

conv = convolve2d(grid, kernel, mode="same")

res = [[1 if x < 4 else 0 for x in row] for row in conv]

print(res)

exit()
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
