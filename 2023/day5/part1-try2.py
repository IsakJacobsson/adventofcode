with open("test.txt") as file:
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
    
    seed-to-soil = {}
    soil-to-fertilizer = {}
    fertilizer-to-water = {}
    water-to-light = {}
    light-to-temperature = {}
    temperature-to-humidity = {}
    humidity-to-location = {}

    