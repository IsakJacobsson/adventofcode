with open("input.txt", "r") as f:
    s = f.read().strip()

id_ranges = s.split(",")

res = 0

for id_range in id_ranges:
    start = int(id_range.split("-")[0])
    end = int(id_range.split("-")[1]) + 1

    for id in range(start, end):
        str_id = str(id)
        div = len(str_id) // 2
        while div > 0:
            times = len(str_id) // div
            g = set()
            if len(str_id) % div != 0:
                div -= 1
                continue
            for time in range(times):
                g.add(str_id[time * div : time * div + div])
            if len(list(g)) == 1:
                res += id
                break
            div -= 1

print(res)
