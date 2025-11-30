import re

with open("input.txt", "r") as f:
    s = f.read()

crates, moves = s.split("\n\n")
crates = crates.split("\n")
moves = moves.strip().split("\n")

nbr_cranes = round(len(crates[0]) / 4)

cranes = [[] for _ in range(nbr_cranes)]

crates.reverse()
for crate_line in crates:
    i = 0
    crane = -1
    while i < len(crate_line):
        crate = crate_line[i : i + 4]
        crane += 1
        i += 4
        if crate[1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            cranes[crane].append(crate[1])

# Part 1
for move in moves:
    m = re.search(r"move (\d+) from (\d+) to (\d+)", move)
    if not m:
        continue
    amount = int(m.group(1))
    fr = int(m.group(2)) - 1
    to = int(m.group(3)) - 1
    for _ in range(amount):
        if len(cranes[fr]) == 0:
            break
        popped = cranes[fr].pop()
        cranes[to].append(popped)

# Part 2
# for move in moves:
#     m = re.match(r"move (\d+) from (\d+) to (\d+)", move)
#     if not m:
#         continue
#     amount = int(m.group(1))
#     fr = int(m.group(2)) - 1
#     to = int(m.group(3)) - 1
#     cranes[to] += cranes[fr][-1 * amount :]
#     for _ in range(amount):
#         if len(cranes[fr]) == 0:
#             break
#         cranes[fr].pop()


res = ""
for crane in cranes:
    res += crane.pop()

print(res)
