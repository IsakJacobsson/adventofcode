def find_and_replace_worst(values, new_value):
    worst = values[0]
    worst_idx = 0
    for i, nbr in enumerate(values):
        if nbr < worst:
            worst = nbr
            worst_idx = i
    if new_value > worst:
        values[worst_idx] = new_value


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    lines = [line[:-1] for line in lines]

top_three = [0, 0, 0]
current_nbr = 0

for line in lines:
    if line == "":
        find_and_replace_worst(top_three, current_nbr)
        current_nbr = 0
        continue
    current_nbr += int(line)

find_and_replace_worst(top_three, current_nbr)

print(sum(top_three))
