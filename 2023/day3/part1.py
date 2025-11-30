with open("input.txt") as file:
    rows = file.readlines()
    nbr_rows = len(rows)
    row_length = len(rows[0])-1
    print(row_length)

    res = 0

    for row_index, row in enumerate(rows):
        i = 0
        while i < row_length:
            if not row[i].isdigit():
                i += 1
                continue

            num_len = 1
            while i + num_len < row_length and row[i+num_len].isdigit(): num_len += 1

            print(i, num_len)

            isValid = False

            # Check before
            if i > 0 and not row[i-1].isdigit() and row[i-1] != '.': isValid = True

            # Check after
            if i+num_len < row_length and not row[i+num_len].isdigit() and row[i+num_len] != '.': isValid = True

            # Check over
            if row_index > 0:
                for y in range(max(0, i-1), min(i+num_len+1, row_length)):
                    if not rows[row_index-1][y].isdigit() and rows[row_index-1][y] != '.': isValid = True

            # Check under
            if row_index+1 < nbr_rows:
                for y in range(max(0, i-1), min(i+num_len+1, row_length)):
                    if not rows[row_index+1][y].isdigit() and rows[row_index+1][y] != '.': isValid = True
            
            if isValid: 
                print ("hej")
                res += int(row[i:i + num_len])

            i += num_len

print(res)