with open("input.txt", "r") as f:
    s = f.read().strip()


def find_min(goal, switches):
    current = [False] * len(goal)
    found = find_min_helper(goal, current, switches, 0) - 1
    if found > 5:
        found = find_min_helper(goal, current, switches, 0, 7) - 1
    return found


def find_min_helper(goal, current, switches, depth, max_depth=5):
    if goal == current:
        return 1
    if depth > max_depth:
        return 1000

    best = 1000
    for i in range(len(switches)):
        copy_current = current[:]
        for s in switches[i]:
            copy_current[s] = not copy_current[s]
        copy_switches = switches[:]
        copy_switches.pop(i)
        best = min(
            best,
            find_min_helper(goal, copy_current, copy_switches, depth + 1, max_depth)
            + 1,
        )
    return best


res = 0
for row in s.split("\n"):
    print(row)
    goal, *switches, other = row.split()
    goal = [False if l == "." else True for l in goal[1:-1]]
    switches = [[int(s) for s in switch[1:-1].split(",")] for switch in switches]
    # print(goal)
    # print(switches)

    nbr = find_min(goal, switches)
    print(nbr)
    res += nbr

print(res)
