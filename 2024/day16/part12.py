import time
import copy

start_time = time.time()

NORTH, EAST, SOUTH, WEST = 0,1,2,3

class Reindeer:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.visited = set()
        self.current_cost = 0
    
    def step(self):
        if self.dir == NORTH:
            self.y -= 1
        elif self.dir == EAST:
            self.x += 1
        elif self.dir == SOUTH:
            self.y += 1
        elif self.dir == WEST:
            self.x -= 1

        self.current_cost += 1

    def get_next_step(self):
        if self.dir == NORTH:
            return (self.x, self.y-1)
        elif self.dir == EAST:
            return (self.x+1, self.y)
        elif self.dir == SOUTH:
            return (self.x, self.y+1)
        elif self.dir == WEST:
            return (self.x-1, self.y)

    def step_back(self):
        if self.dir == NORTH:
            self.y +=1
        elif self.dir == EAST:
            self.x -= 1
        elif self.dir == SOUTH:
            self.y -= 1
        elif self.dir == WEST:
            self.x += 1

    def turn_right(self):
        self.dir = (self.dir + 1) % 4
        self.step()
        self.current_cost += 1000

    def get_right(self):
        next_dir = (self.dir + 1) % 4

        if next_dir == NORTH:
            return (self.x, self.y-1)
        elif next_dir == EAST:
            return (self.x+1, self.y)
        elif next_dir == SOUTH:
            return (self.x, self.y+1)
        elif next_dir == WEST:
            return (self.x-1, self.y)

    def turn_left(self):
        self.dir = (self.dir - 1) % 4
        self.step()
        self.current_cost += 1000

    def get_left(self):
        next_dir = (self.dir - 1) % 4

        if next_dir == NORTH:
            return (self.x, self.y-1)
        elif next_dir == EAST:
            return (self.x+1, self.y)
        elif next_dir == SOUTH:
            return (self.x, self.y+1)
        elif next_dir == WEST:
            return (self.x-1, self.y)

    def get_pos(self):
        return (self.x, self.y)

    def get_state(self):
        return (self.x, self.y, self.dir)

input = open("input.txt").read()
rows = input.split('\n')

height = len(input.split('\n'))
width = len(input.split('\n')[0])

walls = set()
end = None
reindeers = set()
start = None

for y, row in enumerate(rows):
    for x in range(len(rows[0])):
        if row[x] == '#':
            walls.add((x,y))
        elif row[x] == 'E':
            end = (x,y)
        elif row[x] == 'S':
            start = (x,y)
            reindeers.add(Reindeer(x, y, EAST))

min_cost = float('inf')

def print_map(walls, width, height, start, end, reindeer):
    # print('\n'*100)
    for y in range(height):
        build_row = []
        for x in range(width):
            if (x,y) in walls:
                build_row.append('#')
            elif (x,y) == start:
                build_row.append('S')
            elif (x,y) == end:
                build_row.append('E')
            elif (x,y) in reindeer.visited:
                build_row.append('\033[31m@\033[0m')
            else:
                build_row.append('.')
        print(''.join(build_row))


min_cost_for_state = {}
tiles = set()

steps = 0
while reindeers:
    # time.sleep(0.1)
    reindeer = reindeers.pop()
    # print_map(walls, width, height, start, end, reindeer)
    # print(len(reindeers))

    if reindeer.get_pos() in reindeer.visited:
        continue

    if reindeer.get_state() in min_cost_for_state:
        if reindeer.current_cost < min_cost_for_state[reindeer.get_state()]:
            min_cost_for_state[reindeer.get_state()] = reindeer.current_cost
        elif reindeer.current_cost == min_cost_for_state[reindeer.get_state()]:
            None
        else:
            continue
    else:
        min_cost_for_state[reindeer.get_state()] = reindeer.current_cost
    

    reindeer.visited.add(reindeer.get_pos())

    if reindeer.get_pos() == end:
        if reindeer.current_cost == 74392:
            min_cost = reindeer.current_cost
            tiles.update(reindeer.visited)
        continue



    if reindeer.get_next_step() not in walls:
        rc = copy.deepcopy(reindeer)
        rc.step()
        reindeers.add(rc)

    if reindeer.get_right() not in walls:
        rc = copy.deepcopy(reindeer)
        rc.turn_right()
        reindeers.add(rc)
    
    if reindeer.get_left() not in walls:
        rc = copy.deepcopy(reindeer)
        rc.turn_left()
        reindeers.add(rc)



print(len(tiles))
print(min_cost)

end_time = time.time()

print("time: ", end_time - start_time)