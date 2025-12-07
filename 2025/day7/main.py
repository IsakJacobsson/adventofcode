with open("input.txt", "r") as f:
    s = f.read().strip()

rows = s.split("\n")

nbr_rows = len(rows)
splitters = set()
start = None


for r in range(len(rows)):
    for x in range(len(rows[r])):
        if rows[r][x] == "^":
            splitters.add((x, r))
        if rows[r][x] == "S":
            start = (x, r)

visited = dict()
visited_splitters = set()


def beam_down(pos):
    if pos[1] >= nbr_rows:
        return 1

    if pos in visited:
        return visited[pos]

    if pos in splitters:
        visited_splitters.add(pos)

        time_lines = beam_down((pos[0] - 1, pos[1])) + beam_down((pos[0] + 1, pos[1]))
    else:
        time_lines = beam_down((pos[0], pos[1] + 1))

    visited[pos] = time_lines
    return time_lines


time_lines = beam_down(start)
print(len(list(visited_splitters)))

print(time_lines)
