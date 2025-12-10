import time

from tqdm import tqdm

with open("input.txt", "r") as f:
    s = f.read().strip()

rows = s.split("\n")
nbr_rows = len(rows)

# Part 1
largest_area = 0

for i in range(nbr_rows):
    x1, y1 = map(int, rows[i].split(","))
    for j in range(i, nbr_rows):
        x2, y2 = map(int, rows[j].split(","))

        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        largest_area = max(area, largest_area)

print(largest_area)

# Part 2

start = time.perf_counter()
largest_area = 0


def is_intersecting(v1, v2, dir):
    if v1[0][0] == v1[1][0]:
        # Vector 1 is vertical
        if v1[0][1] <= v2[0][1] <= v1[1][1] or v1[1][1] <= v2[0][1] <= v1[0][1]:
            if v2[0][0] <= v1[0][0] <= v2[1][0] or v2[1][0] <= v1[0][0] <= v2[0][0]:
                if v1[0] == v2[0] or v1[0] == v2[1] or v1[1] == v2[0] or v1[1] == v2[1]:
                    return False
                if v2[0][0] == v1[0][0]:
                    return (v2[0][0] - v2[1][0]) * dir < 0
                if v2[1][0] == v1[0][0]:
                    return (v2[1][0] - v2[0][0]) * dir < 0
                return True
    else:
        # Vector 1 is horizontal
        if v1[0][0] <= v2[0][0] <= v1[1][0] or v1[1][0] <= v2[0][0] <= v1[0][0]:
            if v2[0][1] <= v1[0][1] <= v2[1][1] or v2[1][1] <= v1[0][1] <= v2[0][1]:
                if v1[0] == v2[0] or v1[0] == v2[1] or v1[1] == v2[0] or v1[1] == v2[1]:
                    return False
                if v2[0][1] == v1[0][1]:
                    return (v2[0][1] - v2[1][1]) * dir < 0
                if v2[1][1] == v1[0][1]:
                    return (v2[1][1] - v2[0][1]) * dir < 0
                return True
    return False


hor_vecs = []
ver_vecs = []

for i in range(nbr_rows):
    x1, y1 = map(int, rows[i].split(","))
    x2, y2 = map(int, rows[(i + 1) % nbr_rows].split(","))
    if x1 == x2:
        # Vertical
        ver_vecs.append(((x1, y1), (x2, y2)))
    else:
        # Horizontal
        hor_vecs.append(((x1, y1), (x2, y2)))


def check_intersections(ver, hor):
    for side, dir in ver:
        for side2 in hor_vecs:
            if is_intersecting(side, side2, dir):
                return True
    for side, dir in hor:
        for side2 in ver_vecs:
            if is_intersecting(side, side2, dir):
                return True
    return False


amount_ok = 0
for i in tqdm(range(nbr_rows)):
    x1, y1 = map(int, rows[i].split(","))
    for j in range(i, nbr_rows):
        x2, y2 = map(int, rows[j].split(","))

        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        #if area < 436525686:  # We know this from a previous guess
            #continue

        sides_hor = []
        sides_ver = []
        sides_hor.append(((x2, y1), (x1, y1)))
        sides_hor.append(((x2, y2), (x1, y2)))

        if y1 > y2:
            sides_hor[0] = (sides_hor[0], -1)
            sides_hor[1] = (sides_hor[1], 1)
        else:
            sides_hor[0] = (sides_hor[0], 1)
            sides_hor[1] = (sides_hor[1], -1)

        sides_ver.append(((x2, y2), (x2, y1)))
        sides_ver.append(((x1, y2), (x1, y1)))

        if x1 > x2:
            sides_ver[0] = (sides_ver[0], 1)
            sides_ver[1] = (sides_ver[1], -1)
        else:
            sides_ver[0] = (sides_ver[0], -1)
            sides_ver[1] = (sides_ver[1], 1)

        if check_intersections(sides_ver, sides_hor):
            continue

        amount_ok += 1
        largest_area = max(area, largest_area)

end = time.perf_counter()
print(f"Elapsed: {end - start:.6f} seconds")
print(amount_ok)
print(largest_area)
