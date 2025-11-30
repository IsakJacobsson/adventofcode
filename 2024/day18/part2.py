import math

walls = set()

input = open("test.txt").read().split('\n')
for row in input[:12]:
    x, y = row.split(',')
    walls.add((int(x), int(y)))

open = {}
closed = {}

start = (0,0)
end = (6,6)

def print_map():
    for y in range(end[1]+1):
        row = []
        for x in range(end[0]+1):
            if (x,y) in walls:
                row.append('#')
            else:
                row.append('.')
        print(''.join(row))

open[start] = (0,0,0,None)

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

        if y > 0 and (x,y-1) not in walls:
            g_north = g + 1
            h_north = math.sqrt((x - end[0])**2 + (y-1 - end[1])**2)
            successors[(x,y-1)] = (g_north, h_north, g_north+h_north, pos)
        
        if y+1 <= end[1] and (x,y+1) not in walls:
            g_south = g + 1
            h_south = math.sqrt((x - end[0])**2 + (y+1 - end[1])**2)
            successors[(x,y+1)] = (g_south, h_south, g_south+h_south, pos)
        
        if x > 0 and (x-1,y) not in walls:
            g_west = g + 1
            h_west = math.sqrt((x-1 - end[0])**2 + (y - end[1])**2)
            successors[(x-1,y)] = (g_west, h_west, g_west+h_west, pos)
        
        if x+1 <= end[0] and (x+1,y) not in walls:
            g_east = g + 1
            h_east = math.sqrt((x+1 - end[0])**2 + (y - end[1])**2)
            successors[(x+1,y)] = (g_east, h_east, g_east+h_east, pos)

        for succ_pos, succ_value in successors.items():
            if succ_pos == end:
                return succ_value[0]
            
            if succ_pos in open:
                if succ_value[2] > open[succ_pos][2]:
                    continue
            if succ_pos in closed:
                if succ_value[2] > closed[succ_pos][2]:
                    continue
            
            open[succ_pos] = succ_value
        
        closed[pos] = (g, h, f, p)

print_map()
i = 12
res = None
while True:
    steps = a_star()
    print(steps)
    if not steps: break

    
    for row in input[:i]:
        x, y = row.split(',')
        res = (x,y)
        walls.add((int(x), int(y)))
    i += 1

print_map()
print(res)

