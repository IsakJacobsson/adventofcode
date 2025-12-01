with open("input.txt", "r") as f:
    s = f.read().strip()

s = s.split("\n")

# Part 1
moves = []
res = 0

for i, move in enumerate(s):
    dir = move[0]
    amount = int(move[1:])

    prev = 50 if len(moves) == 0 else moves[i - 1]

    if dir == "R":
        moves.append((prev + amount) % 100)
    else:
        moves.append((prev - amount) % 100)

    if moves[i] == 0:
        res += 1

print(res)

# Part 2
res = 0
prev = 50

for i, move in enumerate(s):
    dir = move[0]
    amount = int(move[1:])

    if dir == "R":
        for step in range(amount):
            prev = (prev + 1) % 100
            if prev == 0:
                res += 1
    else:
        for step in range(amount):
            prev = (prev - 1) % 100
            if prev == 0:
                res += 1


print(res)
