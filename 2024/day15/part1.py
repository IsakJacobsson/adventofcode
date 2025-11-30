class Warehouse:
    def __init__(self, input):
        self.edges = set()
        self.boxes = set()
        self.robot = None

        rows = input.split('\n')
        for y, row in enumerate(rows):
            for x in range(len(row)):
                if row[x] == '#': 
                    self.edges.add((x,y))
                if row[x] == 'O':
                    self.boxes.add((x,y))
                if row[x] == '@':
                    self.robot = Robot(x, y, self)
    
    def move_robot(self, arrow_char):
        self.robot.move(arrow_char)

    def move_box(self, x, y, dir_x, dir_y):
        if (x,y) in self.edges:
            return False
        
        if (x,y) not in self.boxes:
            return True
        
        next_x = x + dir_x
        next_y = y + dir_y
        if self.move_box(next_x, next_y, dir_x, dir_y):
            self.boxes.remove((x,y))
            self.boxes.add((next_x, next_y))
            return True
        
        return False
    
    def gps(self):
        res = 0
        for box in self.boxes:
            res += 100 * box[1] + box[0]
        return res

class Robot:
    def __init__(self, x, y, warehouse):
        self.x = x
        self.y = y
        self.warehouse = warehouse
    
    def move(self, arrow_char):
        dir_x = dir_y = 0
        if arrow_char == '^':
            dir_y = -1
        elif arrow_char == '>':
            dir_x = 1
        elif arrow_char == 'v':
            dir_y = 1
        elif arrow_char == '<':
            dir_x = -1

        next_x = self.x + dir_x
        next_y = self.y + dir_y

        if self.warehouse.move_box(next_x, next_y, dir_x, dir_y):
            self.x = next_x
            self.y = next_y
        
        
input = open("input.txt").read()

warehouse_input, moves = input.split('\n\n')

moves = moves.replace('\n','')

warehouse = Warehouse(warehouse_input)

for move in moves:
    warehouse.move_robot(move)

print(warehouse.gps())