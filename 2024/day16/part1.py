import time
import copy

start_time = time.time()

NORTH, EAST, SOUTH, WEST = 1,2,3,4

class Reindeer:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def step(self):
        if self.dir == NORTH:
            self.y -= 1
        elif self.dir == EAST:
            self.x += 1
        elif self.dir == SOUTH:
            self.y += 1
        elif self.dir == WEST:
            self.x -= 1

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
reindeer = None
start = None

for y, row in enumerate(rows):
    for x in range(len(rows[0])):
        if row[x] == '#':
            walls.add((x,y))
        elif row[x] == 'E':
            end = (x,y)
        elif row[x] == 'S':
            start = (x,y)
            reindeer = Reindeer(x, y, EAST)


min_cost = float('inf')

def find_route(reindeer, current_cost):
    time.sleep(0.1)
    print_map(walls, width, height, start, end, reindeer.get_pos())
    #print(current_cost)
    global min_cost
    if current_cost > min_cost: 
        return
    if reindeer.get_pos() == end:
        if current_cost < min_cost: min_cost = current_cost
        return

    if reindeer.get_next_step() and reindeer.get_next_step() not in walls:
        r_copy = copy.copy(reindeer)
        r_copy.step()
        find_route(r_copy, current_cost+1)

    if reindeer.get_right() and reindeer.get_right() not in walls:
        r_copy = copy.copy(reindeer)
        r_copy.turn_right()
        find_route(r_copy, current_cost+1001)

    if reindeer.get_left() and reindeer.get_left() not in walls:
        r_copy = copy.copy(reindeer)
        r_copy.turn_left()
        find_route(r_copy, current_cost+1001)


def print_map(walls, width, height, start, end, pos):
    print('\n'*100)
    for y in range(height):
        build_row = []
        for x in range(width):
            if (x,y) in walls:
                build_row.append('#')
            elif (x,y) == start:
                build_row.append('S')
            elif (x,y) == end:
                build_row.append('E')
            elif (x,y) == pos:
                build_row.append('\033[31m@\033[0m')
            else:
                build_row.append('.')
        print(''.join(build_row))

find_route(reindeer, 0)


print(min_cost)

end_time = time.time()

print("time: ", end_time - start_time)