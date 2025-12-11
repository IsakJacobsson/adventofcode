import copy

with open("input.txt", "r") as f:
    s = f.read().strip()

in_out = dict(tuple(row.split(": ")) for row in s.split("\n"))


# Part 1
def find_ways(input):
    if input == "out":
        return 1

    cur = 0
    for out in in_out[input].split():
        cur += find_ways(out)

    return cur


res = find_ways("you")
print(res)


# Part 2
def find_more_ways(input, visited, fft_found, dac_found, mem):
    if input == "out":
        if fft_found and dac_found:
            return 1
        else:
            return 0
    if input in visited:
        return 0

    vis_copy = set(visited)
    vis_copy.add(input)

    if input == "fft":
        fft_found = True
    if input == "dac":
        dac_found = True

    if (input, fft_found, dac_found) in mem:
        return mem[(input, fft_found, dac_found)]

    cur = 0
    for out in in_out[input].split():
        cur += find_more_ways(out, vis_copy, fft_found, dac_found, mem)

    mem[(input, fft_found, dac_found)] = cur
    return cur


res = find_more_ways("svr", {}, False, False, dict())
print(res)
