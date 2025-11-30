import copy
import time

class Keypad:
    def __init__(self, controller, name):
        self.controller = controller
        self.gap = (0,3)
        self.pressed_keys = []
        self.name = name

        self.keys = {}
        self.keys['A'] = (2,3)
        self.keys['0'] = (1,3)
        self.keys['1'] = (0,2)
        self.keys['2'] = (1,2)
        self.keys['3'] = (2,2)
        self.keys['4'] = (0,1)
        self.keys['5'] = (1,1)
        self.keys['6'] = (2,1)
        self.keys['7'] = (0,0)
        self.keys['8'] = (1,0)
        self.keys['9'] = (2,0)

        self.positions = {
            (2, 3): 'A',
            (1, 3): '0',
            (0, 2): '1',
            (1, 2): '2',
            (2, 2): '3',
            (0, 1): '4',
            (1, 1): '5',
            (2, 1): '6',
            (0, 0): '7',
            (1, 0): '8',
            (2, 0): '9'
        }

        self.current_key = 'A'

    def click_key(self, key):
        key_coordinate = self.keys[key]
        current_key_coordinate = self.keys[self.current_key]

        while current_key_coordinate != key_coordinate:
            # time.sleep(1)
            print(self.name)
            print(current_key_coordinate, key_coordinate)

            possible_dirs = []
            if current_key_coordinate[0] > key_coordinate[0] and (current_key_coordinate[0]-1, current_key_coordinate[1]) != self.gap:
                possible_dirs.append("LEFT")
            elif current_key_coordinate[0] < key_coordinate[0] and (current_key_coordinate[0]+1, current_key_coordinate[1]) != self.gap:
                possible_dirs.append("RIGHT")
            
            if current_key_coordinate[1] > key_coordinate[1] and (current_key_coordinate[0], current_key_coordinate[1]-1) != self.gap:
                possible_dirs.append("UP")
            elif current_key_coordinate[1] < key_coordinate[1] and (current_key_coordinate[0], current_key_coordinate[1]+1) != self.gap:
                possible_dirs.append("DOWN")
            
            best_i = 0
            min_presses = float("inf")
            for i, dir in enumerate(possible_dirs):
                presses = self.controller.check_click_key(dir)
                if presses < min_presses:
                    min_presses = presses
                    best_i = i
                
            print(min_presses)
            
            self.controller.click_key(possible_dirs[best_i])
            if possible_dirs[best_i] == "LEFT":
                current_key_coordinate = (current_key_coordinate[0]-1, current_key_coordinate[1])
            elif possible_dirs[best_i] == "RIGHT":
                current_key_coordinate = (current_key_coordinate[0]+1, current_key_coordinate[1])
            elif possible_dirs[best_i] == "UP":
                current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]-1)
            elif possible_dirs[best_i] == "DOWN":
                current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]+1)
        
        self.current_key = self.positions[current_key_coordinate]
        
        self.controller.click_key('A')

class Controller:
    def __init__(self, controller, name):
        self.controller = controller
        self.name = name
        self.gap = (0,0)
        self.pressed_keys = []

        self.keys = {}
        self.keys['A']     = (2,0)
        self.keys['UP']    = (1,0)
        self.keys['LEFT']  = (0,1)
        self.keys['DOWN']  = (1,1)
        self.keys['RIGHT'] = (2,1)

        self.positions = {
            (2, 0): 'A',
            (1, 0): 'UP',
            (0, 1): 'LEFT',
            (1, 1): 'DOWN',
            (2, 1): 'RIGHT'
        }

        self.current_key = 'A'
    
    def check_click_key(self, key):
        key_coordinate = self.keys[key]
        current_key_coordinate = self.keys[self.current_key]

        controller_copy = copy.deepcopy(self.controller)

        res = 0
        while current_key_coordinate != key_coordinate:
            print(key_coordinate, current_key_coordinate)
            possible_dirs = []
            if current_key_coordinate[0] > key_coordinate[0] and (current_key_coordinate[0]-1, current_key_coordinate[1]) != self.gap:
                possible_dirs.append("LEFT")
            elif current_key_coordinate[0] < key_coordinate[0] and (current_key_coordinate[0]+1, current_key_coordinate[1]) != self.gap:
                possible_dirs.append("RIGHT")
            
            if current_key_coordinate[1] > key_coordinate[1] and (current_key_coordinate[0], current_key_coordinate[1]-1) != self.gap:
                possible_dirs.append("UP")
            elif current_key_coordinate[1] < key_coordinate[1] and (current_key_coordinate[0], current_key_coordinate[1]+1) != self.gap:
                possible_dirs.append("DOWN")
            
            best_i = 0
            min_presses = float("inf")
            for i, dir in enumerate(possible_dirs):
                presses = controller_copy.check_click_key(dir)
                if presses < min_presses:
                    min_presses = presses
                    best_i = i
            
            res += min_presses

            controller_copy.click_key(possible_dirs[best_i])
            if possible_dirs[best_i] == "LEFT":
                current_key_coordinate = (current_key_coordinate[0]-1, current_key_coordinate[1])
            elif possible_dirs[best_i] == "RIGHT":
                current_key_coordinate = (current_key_coordinate[0]+1, current_key_coordinate[1])
            elif possible_dirs[best_i] == "UP":
                current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]-1)
            elif possible_dirs[best_i] == "DOWN":
                current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]+1)
        
        return res
        

    def click_key(self, key):
        key_coordinate = self.keys[key]
        current_key_coordinate = self.keys[self.current_key]

        while current_key_coordinate != key_coordinate:
            # time.sleep(1)
            print(self.name)
            print(current_key_coordinate, key_coordinate)

            possible_dirs = []
            if current_key_coordinate[0] > key_coordinate[0] and (current_key_coordinate[0]-1, current_key_coordinate[1]) != self.gap:
                possible_dirs.append("LEFT")
            elif current_key_coordinate[0] < key_coordinate[0] and (current_key_coordinate[0]+1, current_key_coordinate[1]) != self.gap:
                possible_dirs.append("RIGHT")
            
            if current_key_coordinate[1] > key_coordinate[1] and (current_key_coordinate[0], current_key_coordinate[1]-1) != self.gap:
                possible_dirs.append("UP")
            elif current_key_coordinate[1] < key_coordinate[1] and (current_key_coordinate[0], current_key_coordinate[1]+1) != self.gap:
                possible_dirs.append("DOWN")
            
            best_i = 0
            min_presses = float("inf")
            for i, dir in enumerate(possible_dirs):
                presses = self.controller.check_click_key(dir)
                if presses < min_presses:
                    min_presses = presses
                    best_i = i
            
            self.controller.click_key(possible_dirs[best_i])
            if possible_dirs[best_i] == "LEFT":
                current_key_coordinate = (current_key_coordinate[0]-1, current_key_coordinate[1])
            elif possible_dirs[best_i] == "RIGHT":
                current_key_coordinate = (current_key_coordinate[0]+1, current_key_coordinate[1])
            elif possible_dirs[best_i] == "UP":
                current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]-1)
            elif possible_dirs[best_i] == "DOWN":
                current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]+1)
        
        self.current_key = self.positions[current_key_coordinate]
            
        self.controller.click_key('A')

class ManualController:
    def __init__(self):
        self.pressed_keys = []
    
    def check_click_key(self, key):
        return 1
    
    def click_key(self, key):
        print("Clicking ", key)
        if key == 'A':
            self.pressed_keys.append('A')
        elif key == 'LEFT':
            self.pressed_keys.append('<')
        elif key == 'RIGHT':
            self.pressed_keys.append('>')
        elif key == 'UP':
            self.pressed_keys.append('^')
        elif key == 'DOWN':
            self.pressed_keys.append('v')
        return 1
    
    def get_nbr_pressed_keys(self):
        return len(self.pressed_keys)
    

input = open("test.txt").read().split('\n')

res = 0
for row in input:
    manual_controller = ManualController()
    controller1 = Controller(manual_controller, "Controller 1")
    controller2 = Controller(controller1, "controller 2")
    keypad = Keypad(controller2, "Keypad")

    for key in row:
        keypad.click_key(key)
    
    print(''.join(manual_controller.pressed_keys))
    print(''.join(controller1.pressed_keys))
    print(''.join(controller2.pressed_keys))
    print(''.join(keypad.pressed_keys))
    print(manual_controller.get_nbr_pressed_keys())
    res += int(row[:-1]) * manual_controller.get_nbr_pressed_keys()

print(res)