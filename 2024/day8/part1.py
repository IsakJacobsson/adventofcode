input = open("input.txt").read()
grid = input.split('\n')

antennas = {}

height = len(grid)
width = len(grid[0])

for y in range(height):
    for x in range(width):
        symbol = grid[y][x]
        if symbol == '.':
            continue
        if symbol not in antennas:
            antennas[symbol] = [(x,y)]
        else:
            antennas[symbol].append((x,y))

signals = set()
for symbol, positions in antennas.items():
    for i in range(len(positions)):
        signals.add((positions[i][0], positions[i][1]))
        for j in range(i+1, len(positions)):
            x_diff = positions[i][0] - positions[j][0]
            y_diff = positions[i][1] - positions[j][1]

            signal_pos1 = (positions[i][0] + x_diff, positions[i][1] + y_diff)
            while 0 <= signal_pos1[0] < width and 0 <= signal_pos1[1] < height:
                signals.add(signal_pos1)
                signal_pos1 = (signal_pos1[0] + x_diff, signal_pos1[1] + y_diff)

            signal_pos2 = (positions[j][0] - x_diff, positions[j][1] - y_diff)
            while 0 <= signal_pos2[0] < width and 0 <= signal_pos2[1] < height:
                signals.add(signal_pos2)
                signal_pos2 = (signal_pos2[0] - x_diff, signal_pos2[1] - y_diff)

print(len(signals))
