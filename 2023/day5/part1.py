import time

start_time = time.time()
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line[:-1] for line in lines]
    seeds = lines[0].split(':')[1].split(' ')[1:]
    seeds = [int(seed) for seed in seeds]
    
    # all_seeds = []
    # for i in range(0,len(seeds), 2):
    #     start = seeds[i]
    #     end = seeds[i+1]
    #     for j in (range(start, start+end)):
    #         all_seeds.append(j)
    # seeds = all_seeds
    
    maps = [[], [], [], [], [], [], []]
    i = 3
    map_i = 0
    while i < len(lines):
        if lines[i] == '':
            map_i += 1
            i += 2
            continue
        maps[map_i].append([int(x) for x in lines[i].split(' ')])
        i += 1

    for idx, seed in enumerate(seeds):
        for map in maps:
            for row in map:
                if row[1] <= seed <= row[1] + row[2]:
                    seed += int(row[0]) - int(row[1])
                    break
        seeds[idx] = seed
    
lowest = 1000000000
for seed in seeds:
    if seed < lowest:
        lowest = seed
print(lowest)

end_time = time.time()
print(f"Time: {end_time - start_time:.6f} seconds")
