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

all_points = {(int(x), int(y)) for row in rows for x, y in [row.split(",")]}

parimeter = set()
for i in range(nbr_rows):
    x1, y1 = map(int, rows[i].split(","))
    x2, y2 = map(int, rows[(i + 1) % nbr_rows].split(","))
    if x1 == x2:
        if y1 < y2:
            for y in range(y1, y2 + 1):
                parimeter.add((x1, y))
        else:
            for y in range(y2, y1 + 1):
                parimeter.add((x1, y))

    elif y1 == y2:
        if x1 < x2:
            for x in range(x1, x2 + 1):
                parimeter.add((x, y1))
        else:
            for x in range(x2, x1 + 1):
                parimeter.add((x, y1))

largest_area = 0


# def is_inside_parimeter(x1, y1, x2, y2):
#     start_x = 0
#     end_x = 0
#     start_y = 0
#     end_y = 0
#     if x1 > x2:
#         start_x = x2 + 1
#         end_x = x1 - 1
#     elif x1 < x2:
#         start_x = x1 + 1
#         end_x = x2 - 1
#     else:
#         start_x = end_x = x1
#
#     if y1 > y2:
#         start_y = y2 + 1
#         end_y = y1 - 1
#     elif y1 < y2:
#         start_y = y1 + 1
#         end_y = y2 - 1
#     else:
#         start_y = end_y = y1
#
#     for x in range(start_x, end_x + 1):
#         for y in range(start_y, end_y + 1):
#             if (x, y) in parimeter:
#                 return False
#
#     return True


def check_if_points_not_inside_area(x1, y1, x2, y2):
    start_x = 0
    end_x = 0
    start_y = 0
    end_y = 0
    if x1 > x2:
        start_x = x2 + 1
        end_x = x1 - 1
    elif x1 < x2:
        start_x = x1 + 1
        end_x = x2 - 1
    else:
        start_x = end_x = x1

    if y1 > y2:
        start_y = y2 + 1
        end_y = y1 - 1
    elif y1 < y2:
        start_y = y1 + 1
        end_y = y2 - 1
    else:
        start_y = end_y = y1

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if (x, y) in all_points:
                return False

    return True


start = time.perf_counter()

for i in range(nbr_rows):
    x1, y1 = map(int, rows[i].split(","))
    for j in tqdm(range(i, nbr_rows)):
        x2, y2 = map(int, rows[j].split(","))

        if check_if_points_not_inside_area(x1, y1, x2, y2):
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            largest_area = max(area, largest_area)

end = time.perf_counter()
print(f"Elapsed: {end - start:.6f} seconds")
print(largest_area)
