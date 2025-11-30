import time

start_time = time.time()

input = list(map(int, open("input.txt").read().split(' ')))
input = [(x, 0) for x in input]
nbr_blinks = 25

cache = {}

def split_nbr(nbr):
    sn = str(nbr)
    half = len(sn) // 2
    return int(sn[:half]), int(sn[half:])

res = 0
while input:
    nbr, blink_nbr = input.pop()
    if blink_nbr == nbr_blinks:
        res += 1
        continue
    
    if nbr in cache:
        c = cache[nbr]
        c = [(x, b+blink_nbr) for x,b in c]
        input.extend(c)
        continue

    if nbr == 0:
        new = [(1, 1)]
    elif len(str(nbr)) % 2 == 0:
        f, s = split_nbr(nbr)
        new = [(f, 1), (s, 1)]
    else:
        new = [(nbr * 2024, 1)]
    
    cache[nbr] = new

    input.extend([(x, b+blink_nbr) for x,b in new])

print(res)

end_time = time.time()
print("time: ", end_time-start_time)