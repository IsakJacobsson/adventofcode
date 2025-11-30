star_to_values = {}


def add_to_dict(dict, key, value):
    if key in dict:
        dict[key].append(value)
        return
    dict[key] = [value]
    
res = 0

with open("input.txt") as file:
    rows = file.readlines()
    nbr_rows = len(rows)
    row_length = len(rows[0])-1

    for row_index, row in enumerate(rows):
        i = 0
        while i < row_length:
            if not row[i].isdigit():
                i += 1
                continue

            num_len = 1
            while i + num_len < row_length and row[i+num_len].isdigit(): num_len += 1

            # Check before
            if i > 0 and row[i-1] == '*': add_to_dict(star_to_values, (row_index, i-1), int(row[i:i + num_len]))

            # Check after
            if i+num_len < row_length and row[i+num_len] == '*': add_to_dict(star_to_values, (row_index, i+num_len), int(row[i:i + num_len]))

            # Check over
            if row_index > 0:
                for y in range(max(0, i-1), min(i+num_len+1, row_length)):
                    if rows[row_index-1][y] == '*': add_to_dict(star_to_values, (row_index-1, y), int(row[i:i + num_len]))

            # Check under
            if row_index+1 < nbr_rows:
                for y in range(max(0, i-1), min(i+num_len+1, row_length)):
                    if rows[row_index+1][y] == '*': add_to_dict(star_to_values, (row_index+1, y), int(row[i:i + num_len]))

            i += num_len

for key, value in star_to_values.items():
    if len(value) == 2:
        res += value[0] * value[1]

print(res)