import time

start_time = time.time()

input = open("input.txt").read()

patterns, designs = input.split('\n\n')

patterns = patterns.split(', ')
patterns = sorted(patterns, key=len, reverse=True)
designs = designs.split('\n')

cache = {}

def nbr_possible(s):
    if not s:
        return 1
    
    if s in cache:
        return cache[s]
    
    res = 0
    for pattern in patterns:
        if s.startswith(pattern):
            res += nbr_possible(s[len(pattern):])
    

    cache[s] = res
    return res

res = 0
for i, design in enumerate(designs):
    print(i)
    nbr = nbr_possible(design)
    res += nbr
    
print(res)

end_time = time.time()

print("time ", end_time-start_time)


