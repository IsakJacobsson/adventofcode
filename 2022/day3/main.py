with open("input.txt", "r") as f:
    s = f.read()

sacks = s.strip().split("\n")
res = 0

prio = {}

for i, c in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    prio[c] = i + 1

for sack in sacks:
    half = len(sack) // 2
    (c,) = set(sack[:half]).intersection(sack[half:])
    res += prio[c]

print(res)

res = 0
for i in range(0, len(sacks), 3):
    (c,) = set(sacks[i]).intersection(set(sacks[i + 1]), set(sacks[i + 2]))
    res += prio[c]

print(res)
