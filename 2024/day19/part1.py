import time

start_time = time.time()

input = open("input.txt").read()

patterns, designs = input.split('\n\n')

patterns = patterns.split(', ')
patterns = sorted(patterns, key=len, reverse=True)
designs = designs.split('\n')

cache = {}

def is_possible(s):
    if not s:
        return True
    
    if s in cache:
        return cache[s]
    
    for pattern in patterns:
        if s.startswith(pattern):
            if is_possible(s[len(pattern):]):
                cache[s] = True
                return True
    
    cache[s] = False
    return False

res = 0
for i, design in enumerate(designs):
    if is_possible(design):
        res += 1
    
print(res)

end_time = time.time()

print("time ", end_time-start_time)


