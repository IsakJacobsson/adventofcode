import time

with open("input.txt", "r") as f:
    s = f.read().strip()


def find_min(goal, switches):
    current = [False] * len(goal)
    found = find_min_helper(goal, current, switches, 0)
    if found > 5:
        found = find_min_helper(goal, current, switches, 0, 7)
    return found


def find_min_helper(goal, current, switches, depth, max_depth=5):
    if goal == current:
        return depth
    if depth > max_depth:
        return 1000

    best = 1000
    for i in range(len(switches)):
        copy_current = current[:]
        for s in switches[i]:
            copy_current[s] = not copy_current[s]
        copy_switches = switches[i + 1 :]  # No need to check different orders of clicks
        best = min(
            best,
            find_min_helper(goal, copy_current, copy_switches, depth + 1, max_depth),
        )
    return best


start = time.perf_counter()
res = 0
for row in s.split("\n"):
    goal, *switches, other = row.split()
    goal = [False if l == "." else True for l in goal[1:-1]]
    switches = [[int(s) for s in switch[1:-1].split(",")] for switch in switches]
    # print(goal)
    # print(switches)

    nbr = find_min(goal, switches)
    res += nbr

end = time.perf_counter()
print(f"Elapsed: {end - start:.6f} seconds")
print(res)
