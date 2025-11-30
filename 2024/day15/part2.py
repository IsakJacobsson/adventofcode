import time

class Warehouse:
    def __init__(self, input):
        self.edges = set()
        self.boxes = set()
        self.robot = None

        rows = input.split('\n')
        for y, row in enumerate(rows):
            for x in range(len(row)):
                if row[x] == '#': 
                    self.edges.add((x*2,y))
                    self.edges.add((x*2+1,y))
                if row[x] == 'O':
                    self.boxes.add(((x*2,y), (x*2+1,y)))
                if row[x] == '@':
                    self.robot = Robot(x*2, y, self)
    
    def move_robot(self, arrow_char):
        self.robot.move(arrow_char)

    def can_move_box_up(self, box):
        if box[0] in self.edges or box[1] in self.edges:
            return False
        
        if box not in self.boxes:
            return True

        if ((box[0][0], box[0][1]-1), (box[1][0], box[1][1]-1)) in self.boxes:
            return self.can_move_box_up(((box[0][0], box[0][1]-1), (box[1][0], box[1][1]-1)))
        
        res1 = True
        if ((box[0][0]-1, box[0][1]-1), (box[1][0]-1, box[1][1]-1)) in self.boxes:
            res1 = self.can_move_box_up(((box[0][0]-1, box[0][1]-1), (box[1][0]-1, box[1][1]-1)))

        res2 = True
        if ((box[0][0]+1, box[0][1]-1), (box[1][0]+1, box[1][1]-1)) in self.boxes:
            res2 = self.can_move_box_up(((box[0][0]+1, box[0][1]-1), (box[1][0]+1, box[1][1]-1)))
        
        return res1 and res2 and self.can_move_box_up(((box[0][0], box[0][1]-1), (box[1][0], box[1][1]-1)))

    def move_box_up(self, box):
        if ((box[0][0], box[0][1]-1), (box[1][0], box[1][1]-1)) in self.boxes:
            self.move_box_up(((box[0][0], box[0][1]-1), (box[1][0], box[1][1]-1)))
        
        if ((box[0][0]-1, box[0][1]-1), (box[1][0]-1, box[1][1]-1)) in self.boxes:
            self.move_box_up(((box[0][0]-1, box[0][1]-1), (box[1][0]-1, box[1][1]-1)))
        
        if ((box[0][0]+1, box[0][1]-1), (box[1][0]+1, box[1][1]-1)) in self.boxes:
            self.move_box_up(((box[0][0]+1, box[0][1]-1), (box[1][0]+1, box[1][1]-1)))

        self.boxes.remove(box)
        self.boxes.add(((box[0][0], box[0][1]-1), (box[1][0], box[1][1]-1)))

    def can_move_box_down(self, box):
        if box[0] in self.edges or box[1] in self.edges:
            return False
        
        if box not in self.boxes:
            return True

        if ((box[0][0], box[0][1]+1), (box[1][0], box[1][1]+1)) in self.boxes:
            return self.can_move_box_down(((box[0][0], box[0][1]+1), (box[1][0], box[1][1]+1)))
        
        res1 = True
        if ((box[0][0]-1, box[0][1]+1), (box[1][0]-1, box[1][1]+1)) in self.boxes:
            res1 = self.can_move_box_down(((box[0][0]-1, box[0][1]+1), (box[1][0]-1, box[1][1]+1)))

        res2 = True
        if ((box[0][0]+1, box[0][1]+1), (box[1][0]+1, box[1][1]+1)) in self.boxes:
            res2 = self.can_move_box_down(((box[0][0]+1, box[0][1]+1), (box[1][0]+1, box[1][1]+1)))
        
        return res1 and res2 and self.can_move_box_down(((box[0][0], box[0][1]+1), (box[1][0], box[1][1]+1)))

    def move_box_down(self, box):
        if ((box[0][0], box[0][1]+1), (box[1][0], box[1][1]+1)) in self.boxes:
            self.move_box_down(((box[0][0], box[0][1]+1), (box[1][0], box[1][1]+1)))
        
        if ((box[0][0]-1, box[0][1]+1), (box[1][0]-1, box[1][1]+1)) in self.boxes:
            self.move_box_down(((box[0][0]-1, box[0][1]+1), (box[1][0]-1, box[1][1]+1)))
        
        if ((box[0][0]+1, box[0][1]+1), (box[1][0]+1, box[1][1]+1)) in self.boxes:
            self.move_box_down(((box[0][0]+1, box[0][1]+1), (box[1][0]+1, box[1][1]+1)))

        self.boxes.remove(box)
        self.boxes.add(((box[0][0], box[0][1]+1), (box[1][0], box[1][1]+1)))


    def move_box_right(self, box):
        if box[0] in self.edges:
            return False

        if box not in self.boxes:
            return True
        
        next_box = ((box[1][0]+1, box[1][1]), (box[1][0]+2, box[1][1]))

        if self.move_box_right(next_box):
            self.boxes.remove(box)
            moved_box = ((box[1][0], box[1][1]), (box[1][0]+1, box[1][1]))
            self.boxes.add(moved_box)
            return True
        
        return False

    def move_box_left(self, box):
        if box[1] in self.edges:
            return False

        if box not in self.boxes:
            return True
        
        next_box = ((box[0][0]-2, box[0][1]), (box[0][0]-1, box[0][1]))

        if self.move_box_left(next_box):
            self.boxes.remove(box)
            moved_box = ((box[0][0]-1, box[0][1]), (box[0][0], box[0][1]))
            self.boxes.add(moved_box)
            return True
        
        return False
        
    def gps(self):
        res = 0
        for box in self.boxes:
            res += 100 * box[0][1] + box[0][0]
        return res
    
    def draw(self, width, height):
        for y in range(height):
            x = 0
            row = []
            while x < width:
                if (x,y) in self.edges:
                    row.append('#')
                elif ((x,y), (x+1, y)) in self.boxes:
                    row.append("[]")
                    x += 1
                elif (x,y) == (self.robot.x, self.robot.y):
                    row.append('@')
                else:
                    row.append('.')
                x += 1
            print(''.join(row))

class Robot:
    def __init__(self, x, y, warehouse):
        self.x = x
        self.y = y
        self.warehouse = warehouse
    
    def move(self, arrow_char):
        if arrow_char == '^':
            if ((self.x-1, self.y-1), (self.x, self.y-1)) in self.warehouse.boxes:
                if self.warehouse.can_move_box_up(((self.x-1, self.y-1), (self.x, self.y-1))):
                    self.warehouse.move_box_up(((self.x-1, self.y-1), (self.x, self.y-1)))
                    self.y -= 1
            elif ((self.x, self.y-1), (self.x+1, self.y-1)) in self.warehouse.boxes:
                if self.warehouse.can_move_box_up(((self.x, self.y-1), (self.x+1, self.y-1))):
                    self.warehouse.move_box_up(((self.x, self.y-1), (self.x+1, self.y-1)))
                    self.y -= 1
            elif (self.x, self.y-1) not in self.warehouse.edges:
                self.y -= 1
        if arrow_char == '>':
            if self.warehouse.move_box_right(((self.x+1, self.y), (self.x+2, self.y))):
                self.x += 1
        elif arrow_char == 'v':
            if ((self.x-1, self.y+1), (self.x, self.y+1)) in self.warehouse.boxes:
                if self.warehouse.can_move_box_down(((self.x-1, self.y+1), (self.x, self.y+1))):
                    self.warehouse.move_box_down(((self.x-1, self.y+1), (self.x, self.y+1)))
                    self.y += 1
            elif ((self.x, self.y+1), (self.x+1, self.y+1)) in self.warehouse.boxes:
                if self.warehouse.can_move_box_down(((self.x, self.y+1), (self.x+1, self.y+1))):
                    self.warehouse.move_box_down(((self.x, self.y+1), (self.x+1, self.y+1)))
                    self.y += 1
            elif (self.x, self.y+1) not in self.warehouse.edges:
                self.y += 1
        elif arrow_char == '<':
            if self.warehouse.move_box_left(((self.x-2, self.y), (self.x-1, self.y))):
                self.x -= 1
        
input = open("input.txt").read()

warehouse_input, moves = input.split('\n\n')

height = len(warehouse_input.split('\n'))
width = len(warehouse_input.split('\n')[0]) * 2

moves = moves.replace('\n','')

warehouse = Warehouse(warehouse_input)
warehouse.draw(width, height)

for move in moves:
    time.sleep(0.25)
    print("\n" * 10)
    warehouse.draw(width, height)
    warehouse.move_robot(move)


print(warehouse.gps())