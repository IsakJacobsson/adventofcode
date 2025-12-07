with open("input.txt", "r") as f:
    s = f.read().strip()

rows = s.split("\n")

nbr_rows = len(rows)
splitters = set()
start = 0


for r in range(len(rows)):
    for x in range(len(rows[r])):
        if rows[r][x] == "^":
            splitters.add(complex(x, r))
        if rows[r][x] == "S":
            start = complex(x, r)

visited = dict()
visited_splitters = set()


def beam_down(pos):
    if pos.imag >= nbr_rows:
        return 1

    if pos in visited:
        return visited[pos]

    if pos in splitters:
        visited_splitters.add(pos)

        time_lines = beam_down(pos - 1) + beam_down(pos + 1)
    else:
        time_lines = beam_down((pos + 1j))

    visited[pos] = time_lines
    return time_lines


time_lines = beam_down(start)
print(len(list(visited_splitters)))

print(time_lines)
