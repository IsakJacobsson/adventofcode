import time

class Robot:
    def __init__(self, p, v):
        self.pos_x = p[0]
        self.pos_y = p[1]
        self.vel_x = v[0]
        self.vel_y = v[1]
    
    def move(self, width, height):
        self.pos_x = (self.pos_x + self.vel_x) % width
        self.pos_y = (self.pos_y + self.vel_y) % height

    def print(self):
        print(f"[{self.pos_x}, {self.pos_y}] [{self.vel_x}, {self.vel_y}]")

class RobotMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.robots = []
        self.occopied_spaces = [[0 for x in range(width)] for y in range(height)]

    def add_robot(self, robot):
        self.robots.append(robot)
        self.occopied_spaces[robot.pos_y][robot.pos_x] += 1
    
    def move_all(self):
        for robot in self.robots:
            self.occopied_spaces[robot.pos_y][robot.pos_x] -= 1
            robot.move(self.width, self.height)
            self.occopied_spaces[robot.pos_y][robot.pos_x] += 1

    def print_all(self):
        for robot in self.robots:
            robot.print()

    def top_left(self):
        x_bound = self.width // 2
        y_bound = self.height // 2

        res = 0
        for robot in self.robots:
            if 0 <= robot.pos_x < x_bound and 0 <= robot.pos_y < y_bound:
                res += 1
        
        return res
    
    def top_right(self):
        x_bound = self.width // 2
        y_bound = self.height // 2

        res = 0
        for robot in self.robots:
            if x_bound < robot.pos_x < self.width and 0 <= robot.pos_y < y_bound:
                res += 1
        
        return res
    
    def bottom_left(self):
        x_bound = self.width // 2
        y_bound = self.height // 2

        res = 0
        for robot in self.robots:
            if 0 <= robot.pos_x < x_bound and y_bound < robot.pos_y < self.height:
                res += 1
        
        return res
    
    def bottom_right(self):
        x_bound = self.width // 2
        y_bound = self.height // 2

        res = 0
        for robot in self.robots:
            if x_bound < robot.pos_x < self.width and y_bound < robot.pos_y < self.height:
                res += 1
        
        return res
    
    def safety_factor(self):
        return self.top_left() * self.top_right() * self.bottom_left() * self.bottom_right()
    
    def print_pattern(self, idx):
        build_rows = []
        do_print = False
        for row in self.occopied_spaces:
            build_row = [' '] * width
            s = 20
            for i, num in enumerate(row):
                if num > 0:
                    build_row[i] = chr(0x2588)
                    s -= 1
            if s < 0:
                do_print = True
            build_rows.append(build_row)
        if do_print:
            print(idx)
            for build_row in build_rows:
                print(''.join(build_row))

input = open("input.txt").read().split('\n')
width = 101
height = 103

robotMap = RobotMap(width, height)


for line in input:
    p, v = [x[2:] for x in line.split(' ')]
    p = list(map(int, p.split(',')))
    v = list(map(int, v.split(',')))
    robot = Robot(p, v)
    robotMap.add_robot(robot)

i = 1

while True:
    robotMap.move_all()
    robotMap.print_pattern(i)
    i += 1