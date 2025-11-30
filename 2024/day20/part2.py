import math
import time

start_time = time.time()

walls = set()
start = None
end   = None

# For part 2, I did manual binary search to find the first coordinate that did not produce a result
input = open("input.txt").read().split('\n')
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == '#': walls.add((x,y))
        elif input[y][x] == 'S': start = (x,y)
        elif input[y][x] == 'E': end = (x,y)

width = len(input[0])
height = len(input)
open = {}
closed = {}

def print_map(walk):
    for y in range(height):
        row = []
        for x in range(width):
            if (x,y) in walls:
                row.append('#')
            elif (x,y) in walk:
                row.append('O')
            else:
                row.append('.')
        print(''.join(row))

open[start] = (0,0,0,[])

def a_star():
    while open:
        q = None
        for pos, value in open.items():
            if q == None:
                q = (pos, value)
            elif value[2] < q[1][2]:
                q = (pos, value)

        pos = q[0]
        x, y = pos
        g, h, f, p = q[1]

        open.pop(pos)

        successors = {}

        if (x,y-1) not in walls:
            g_north = g + 1
            h_north = math.sqrt((x - end[0])**2 + (y-1 - end[1])**2)
            successors[(x,y-1)] = (g_north, h_north, g_north+h_north, p + [pos])
        
        if (x,y+1) not in walls:
            g_south = g + 1
            h_south = math.sqrt((x - end[0])**2 + (y+1 - end[1])**2)
            successors[(x,y+1)] = (g_south, h_south, g_south+h_south, p + [pos])
        
        if (x-1,y) not in walls:
            g_west = g + 1
            h_west = math.sqrt((x-1 - end[0])**2 + (y - end[1])**2)
            successors[(x-1,y)] = (g_west, h_west, g_west+h_west, p + [pos])
        
        if (x+1,y) not in walls:
            g_east = g + 1
            h_east = math.sqrt((x+1 - end[0])**2 + (y - end[1])**2)
            successors[(x+1,y)] = (g_east, h_east, g_east+h_east, p + [pos])

        for succ_pos, succ_value in successors.items():
            if succ_pos == end:
                return succ_value[0], succ_value[3] + [succ_pos]
            
            if succ_pos in open:
                if succ_value[2] > open[succ_pos][2]:
                    continue
            if succ_pos in closed:
                if succ_value[2] > closed[succ_pos][2]:
                    continue
            
            open[succ_pos] = succ_value
        
        closed[pos] = (g, h, f, p)


def poses_from_here(pos):
    f1 = {}
    f1[pos] = 0

    for _ in range(20):
        next_f1 = {}
        for pos, i in f1.items():
            x,y = pos
            if 0 <= y-1:
                next_f1[(x,y-1)] = i+1
            if y+1 < height:
                next_f1[(x,y+1)] = i+1
            if 0 <= x-1:
                next_f1[(x-1,y)] = i+1
            if x+1 < width:
                next_f1[(x+1,y)] = i+1

        for pos, steps in next_f1.items():
            if not pos in f1:
                f1[pos] = steps

    res = {}
    for p, steps in f1.items():
        if not p in walls:
            res[p] = steps

    return res

first_walk_len, walk = a_star()
print(first_walk_len)

res = {}

for i, pos in enumerate(walk):
    print(i)
    poses = poses_from_here(pos)
    for p, steps in poses.items():
        pre = i
        after = walk.index(p)

        saved_picos = after - pre - steps
        if saved_picos >= 100:
            if saved_picos in res:
                res[saved_picos] += 1
            else:
                res[saved_picos] = 1

print(res)

res2 = 0
for key, value in res.items():
    res2 += value

print(res2)

end_time = time.time()
print("time ", end_time-start_time)
