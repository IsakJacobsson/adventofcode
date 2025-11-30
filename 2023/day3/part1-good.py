def get_adjacent(i,j, rows, cols):
    dirs = [(-1,-1), (-1,0), (-1,1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)]
    
    adjacent_cells = []
    for di, dj in dirs:
        ni, nj = i+di, j+dj
        if 0 <= ni < rows and 0 <= nj < cols:
            adjacent_cells.append((ni,nj))
    
    return adjacent_cells

res = 0

with open("input.txt") as file:
    text = file.read()
    rows = text.split('\n')

    nbr_rows = len(rows)
    row_len  = len(rows[0])

    for row_index, row in enumerate(rows):
        if row == '':
            continue

        i = 0

        while i < row_len:
            if not row[i].isdigit():
                i += 1
                continue

            num_len = 1
            while i+num_len < row_len and row[i+num_len].isdigit(): num_len += 1

            isValid = False
            for k in range(i, i+num_len):
                adjacent_cells = get_adjacent(row_index, k, nbr_rows, row_len)
                if any(rows[x][y] in "*=/@%+-#&$" for x, y in adjacent_cells):
                        isValid = True
                        break
            
            if isValid:
                res += int(row[i:i+num_len])
            
            i += num_len

print(res)
    
