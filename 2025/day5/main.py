import copy

with open("input.txt", "r") as f:
    s = f.read().strip()

ranges, _ = s.split("\n\n")
ranges = [[int(r.split("-")[0]), int(r.split("-")[1])] for r in ranges.split("\n")]

while True:
    new_ranges = []
    for r in ranges:
        found = False
        for n_r in new_ranges:
            if r[0] < n_r[0] and r[1] > n_r[1]:
                n_r[0] = r[0]
                n_r[1] = r[1]
                found = True
                break
            if n_r[0] <= r[0] <= n_r[1]:
                if r[1] > n_r[1]:
                    n_r[1] = r[1]
                found = True
                break
            if n_r[0] <= r[1] <= n_r[1]:
                if r[0] < n_r[0]:
                    n_r[0] = r[0]
                found = True
                break
        if not found:
            new_ranges.append([r[0], r[1]])

    if ranges == new_ranges:
        break
    ranges = copy.deepcopy(new_ranges)


res = 0
for start, end in ranges:
    res += end - start + 1

print(res)
