with open("input.txt", "r") as f:
    s = f.read().strip()

rows = s.split("\n")
nbr_rows = len(rows)

largest_area = 0

for i in range(nbr_rows):
    x1, y1 = map(int, rows[i].split(","))
    for j in range(i, nbr_rows):
        x2, y2 = map(int, rows[j].split(","))

        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        largest_area = max(area, largest_area)

print(largest_area)
