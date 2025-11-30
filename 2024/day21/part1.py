import time

class Keypad:
    def __init__(self, controller):
        self.controller = controller
        self.gap = (0,3)
        self.pressed_keys = []

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
        # time.sleep(1)
        key_coordinate = self.keys[key]
        current_key_coordinate = self.keys[self.current_key]

        while key_coordinate != current_key_coordinate:
            # print("Keypad")
            # print(key_coordinate, current_key_coordinate)

            if key_coordinate[0] > current_key_coordinate[0] and key_coordinate[1] == current_key_coordinate[1]:
                self.controller.click_key(["RIGHT"])
                current_key_coordinate = (current_key_coordinate[0]+1, current_key_coordinate[1])
            elif key_coordinate[0] < current_key_coordinate[0] and key_coordinate[1] == current_key_coordinate[1]:
                self.controller.click_key(["LEFT"])
                current_key_coordinate = (current_key_coordinate[0]-1, current_key_coordinate[1])
            elif key_coordinate[1] > current_key_coordinate[1] and key_coordinate[0] == current_key_coordinate[0]:
                self.controller.click_key(["DOWN"])
                current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]+1)
            elif key_coordinate[1] < current_key_coordinate[1] and key_coordinate[0] == current_key_coordinate[0]:
                self.controller.click_key(["UP"])
                current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]-1)
            elif key_coordinate[0] > current_key_coordinate[0] and key_coordinate[1] > current_key_coordinate[1]:
                if (current_key_coordinate[0]+1, current_key_coordinate[1]) != self.gap and (current_key_coordinate[0], current_key_coordinate[1]+1) != self.gap:
                    clicked = self.controller.click_key(["RIGHT", "DOWN"])
                elif (current_key_coordinate[0]+1, current_key_coordinate[1]) != self.gap:
                    clicked = self.controller.click_key(["RIGHT"])
                elif (current_key_coordinate[0], current_key_coordinate[1]+1) != self.gap:
                    clicked = self.controller.click_key(["DOWN"])
                if clicked == "RIGHT":
                    current_key_coordinate = (current_key_coordinate[0]+1, current_key_coordinate[1])
                else:
                    current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]+1)
            elif key_coordinate[0] > current_key_coordinate[0] and key_coordinate[1] < current_key_coordinate[1]:
                if (current_key_coordinate[0]+1, current_key_coordinate[1]) != self.gap and (current_key_coordinate[0], current_key_coordinate[1]-1) != self.gap:
                    clicked = self.controller.click_key(["RIGHT", "UP"])
                elif (current_key_coordinate[0]+1, current_key_coordinate[1]) != self.gap:
                    clicked = self.controller.click_key(["RIGHT"])
                elif (current_key_coordinate[0], current_key_coordinate[1]-1) != self.gap:
                    clicked = self.controller.click_key(["UP"])
                if clicked == "RIGHT":
                    current_key_coordinate = (current_key_coordinate[0]+1, current_key_coordinate[1])
                else:
                    current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]-1)
            elif key_coordinate[0] < current_key_coordinate[0] and key_coordinate[1] > current_key_coordinate[1]:
                if (current_key_coordinate[0]-1, current_key_coordinate[1]) != self.gap and (current_key_coordinate[0], current_key_coordinate[1]+1) != self.gap:
                    clicked = self.controller.click_key(["LEFT", "DOWN"])
                elif (current_key_coordinate[0]-1, current_key_coordinate[1]) != self.gap:
                    clicked = self.controller.click_key(["LEFT"])
                elif (current_key_coordinate[0], current_key_coordinate[1]+1) != self.gap:
                    clicked = self.controller.click_key(["DOWN"])
                if clicked == "LEFT":
                    current_key_coordinate = (current_key_coordinate[0]-1, current_key_coordinate[1])
                else:
                    current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]+1)
            elif key_coordinate[0] < current_key_coordinate[0] and key_coordinate[1] < current_key_coordinate[1]:
                if (current_key_coordinate[0]-1, current_key_coordinate[1]) != self.gap and (current_key_coordinate[0], current_key_coordinate[1]-1) != self.gap:
                    clicked = self.controller.click_key(["LEFT", "UP"])
                elif (current_key_coordinate[0]-1, current_key_coordinate[1]) != self.gap:
                    clicked = self.controller.click_key(["LEFT"])
                elif (current_key_coordinate[0], current_key_coordinate[1]-1) != self.gap:
                    clicked = self.controller.click_key(["UP"])
                if clicked == "LEFT":
                    current_key_coordinate = (current_key_coordinate[0]-1, current_key_coordinate[1])
                else:
                    current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]-1)

        
        self.controller.click_key(['A'])


        self.current_key = self.positions[current_key_coordinate]
        self.pressed_keys.append(self.current_key)

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

    def click_key(self, valid_keys):
        key_coordinate = self.keys[valid_keys[0]]
        key2_coordinate = None
        current_key_coordinate = self.keys[self.current_key]
        if len(valid_keys) == 2:
            key2_coordinate = self.keys[valid_keys[1]]
            if (abs(key_coordinate[0] - current_key_coordinate[0]) + abs(key_coordinate[1] - current_key_coordinate[1])) > (abs(key2_coordinate[0] - current_key_coordinate[0]) + abs(key2_coordinate[1] - current_key_coordinate[1])):
                temp = key_coordinate
                key_coordinate = key2_coordinate
                key2_coordinate = temp

        while key_coordinate != current_key_coordinate and key2_coordinate != current_key_coordinate:
            # time.sleep(1)
            # print(self.name)
            # print(key_coordinate, current_key_coordinate)
            
            if key_coordinate[0] > current_key_coordinate[0] and key_coordinate[1] == current_key_coordinate[1]:
                self.controller.click_key(["RIGHT"])
                current_key_coordinate = (current_key_coordinate[0]+1, current_key_coordinate[1])
            elif key_coordinate[0] < current_key_coordinate[0] and key_coordinate[1] == current_key_coordinate[1]:
                self.controller.click_key(["LEFT"])
                current_key_coordinate = (current_key_coordinate[0]-1, current_key_coordinate[1])
            elif key_coordinate[1] > current_key_coordinate[1] and key_coordinate[0] == current_key_coordinate[0]:
                self.controller.click_key(["DOWN"])
                current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]+1)
            elif key_coordinate[1] < current_key_coordinate[1] and key_coordinate[0] == current_key_coordinate[0]:
                self.controller.click_key(["UP"])
                current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]-1)
            elif key_coordinate[0] > current_key_coordinate[0] and key_coordinate[1] > current_key_coordinate[1]:
                if (current_key_coordinate[0]+1, current_key_coordinate[1]) != self.gap and (current_key_coordinate[0], current_key_coordinate[1]+1) != self.gap:
                    clicked = self.controller.click_key(["RIGHT", "DOWN"])
                elif (current_key_coordinate[0]+1, current_key_coordinate[1]) != self.gap:
                    clicked = self.controller.click_key(["RIGHT"])
                elif (current_key_coordinate[0], current_key_coordinate[1]+1) != self.gap:
                    clicked = self.controller.click_key(["DOWN"])
                if clicked == "RIGHT":
                    current_key_coordinate = (current_key_coordinate[0]+1, current_key_coordinate[1])
                else:
                    current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]+1)
            elif key_coordinate[0] > current_key_coordinate[0] and key_coordinate[1] < current_key_coordinate[1]:
                if (current_key_coordinate[0]+1, current_key_coordinate[1]) != self.gap and (current_key_coordinate[0], current_key_coordinate[1]-1) != self.gap:
                    clicked = self.controller.click_key(["RIGHT", "UP"])
                elif (current_key_coordinate[0]+1, current_key_coordinate[1]) != self.gap:
                    clicked = self.controller.click_key(["RIGHT"])
                elif (current_key_coordinate[0], current_key_coordinate[1]-1) != self.gap:
                    clicked = self.controller.click_key(["UP"])
                if clicked == "RIGHT":
                    current_key_coordinate = (current_key_coordinate[0]+1, current_key_coordinate[1])
                else:
                    current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]-1)
            elif key_coordinate[0] < current_key_coordinate[0] and key_coordinate[1] > current_key_coordinate[1]:
                if (current_key_coordinate[0]-1, current_key_coordinate[1]) != self.gap and (current_key_coordinate[0], current_key_coordinate[1]+1) != self.gap:
                    clicked = self.controller.click_key(["LEFT", "DOWN"])
                elif (current_key_coordinate[0]-1, current_key_coordinate[1]) != self.gap:
                    clicked = self.controller.click_key(["LEFT"])
                elif (current_key_coordinate[0], current_key_coordinate[1]+1) != self.gap:
                    clicked = self.controller.click_key(["DOWN"])
                if clicked == "LEFT":
                    current_key_coordinate = (current_key_coordinate[0]-1, current_key_coordinate[1])
                else:
                    current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]+1)
            elif key_coordinate[0] < current_key_coordinate[0] and key_coordinate[1] < current_key_coordinate[1]:
                if (current_key_coordinate[0]-1, current_key_coordinate[1]) != self.gap and (current_key_coordinate[0], current_key_coordinate[1]-1) != self.gap:
                    clicked = self.controller.click_key(["LEFT", "UP"])
                elif (current_key_coordinate[0]-1, current_key_coordinate[1]) != self.gap:
                    clicked = self.controller.click_key(["LEFT"])
                elif (current_key_coordinate[0], current_key_coordinate[1]-1) != self.gap:
                    clicked = self.controller.click_key(["UP"])
                if clicked == "LEFT":
                    current_key_coordinate = (current_key_coordinate[0]-1, current_key_coordinate[1])
                else:
                    current_key_coordinate = (current_key_coordinate[0], current_key_coordinate[1]-1)

        self.controller.click_key(['A'])

        self.current_key = self.positions[current_key_coordinate]

        if self.current_key == 'A':
            self.pressed_keys.append('A')
        elif self.current_key == 'LEFT':
            self.pressed_keys.append('<')
        elif self.current_key == 'RIGHT':
            self.pressed_keys.append('>')
        elif self.current_key == 'UP':
            self.pressed_keys.append('^')
        elif self.current_key == 'DOWN':
            self.pressed_keys.append('v')


        return self.current_key

class ManualController:
    def __init__(self):
        self.pressed_keys = []
    
    def click_key(self, keys):
        # print(keys)
        key = keys[0]
        # print("Manual Controller, press", key)
        if key == 'A':
            self.pressed_keys.append('A')
            return 'A'
        elif key == 'LEFT':
            self.pressed_keys.append('<')
            return 'LEFT'
        elif key == 'RIGHT':
            self.pressed_keys.append('>')
            return 'RIGHT'
        elif key == 'UP':
            self.pressed_keys.append('^')
            return 'UP'
        elif key == 'DOWN':
            self.pressed_keys.append('v')
            return 'DOWN'
    
    def get_nbr_pressed_keys(self):
        return len(self.pressed_keys)

input = open("test.txt").read().split('\n')

res = 0
for row in input:
    manual_controller = ManualController()
    controller1 = Controller(manual_controller, "Controller 1")
    controller2 = Controller(controller1, "controller 2")
    keypad = Keypad(controller2)

    for key in row:
        keypad.click_key(key)
    
    print(''.join(manual_controller.pressed_keys))
    print(''.join(controller1.pressed_keys))
    print(''.join(controller2.pressed_keys))
    print(''.join(keypad.pressed_keys))
    print(manual_controller.get_nbr_pressed_keys())
    res += int(row[:-1]) * manual_controller.get_nbr_pressed_keys()

print(res)

    
    