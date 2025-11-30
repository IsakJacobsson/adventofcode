with open("input.txt", "r") as f:
    input = f.read()


to_win = {1: 2, 2: 3, 3: 1}
to_lose = {1: 3, 2: 1, 3: 2}
values = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


def calc_score2(op, res):
    if res == "Y":
        return op + 3
    elif res == "Z":
        return to_win[op] + 6
    else:
        return to_lose[op]


def calc_score(op, me):
    if op == me:
        return me + 3
    elif (op == 1 and me == 2) or (op == 2 and me == 3) or (op == 3 and me == 1):
        return me + 6
    else:
        return me


p1 = [
    calc_score(values[game[0]], values[game[2]]) for game in input.strip().split("\n")
]

print(sum(p1))

p2 = [calc_score2(values[game[0]], game[2]) for game in input.strip().split("\n")]

print(sum(p2))
