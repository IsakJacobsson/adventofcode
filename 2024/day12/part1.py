input = open("input.txt").read()
grid = input.split('\n')

grid_height = len(grid)
grid_width = len(grid[0])

class Plant:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.letter = letter

    def get_fences(self, plants):
        nbr_fences = 0
        if (self.x-1, self.y) not in plants:
            nbr_fences += 1
        if (self.x+1, self.y) not in plants:
            nbr_fences += 1
        if (self.x, self.y-1) not in plants:
            nbr_fences += 1
        if (self.x, self.y+1) not in plants:
            nbr_fences += 1

        return nbr_fences

class Garden:
    def __init__(self, letter):
        self.letter = letter
        self.plants = set()

    def is_part_of_garden(self, plant):
        if plant.letter != self.letter: return False
        if plant.x > 0 and (plant.x-1, plant.y) in self.plants: return True
        if plant.x+1 < grid_width and (plant.x+1, plant.y) in self.plants: return True
        if plant.y > 0 and (plant.x, plant.y-1) in self.plants: return True
        if plant.y+1 < grid_height and (plant.x, plant.y+1) in self.plants: return True

        return False

    def add_plant(self, plant):
        self.plants.add((plant.x, plant.y))

    def add_garden(self, garden):
        self.plants.update(garden.plants)

    def get_area(self):
        return len(self.plants)

    def get_parimeter(self):
        nbr_fences = 0
        for p in self.plants:
            plant = Plant(p[0], p[1], '')
            nbr_fences += plant.get_fences(self.plants)

        return nbr_fences

class Gardens:
    def __init__(self):
        self.gardens = []

    def add_plant_to_garden(self, plant):
        selected_garden_idxs = []
        i = len(self.gardens)-1
        while i >= 0:
            if self.gardens[i].is_part_of_garden(plant):
                selected_garden_idxs.append(i)
            i -= 1

        if selected_garden_idxs:
            main_i = selected_garden_idxs[0]
            self.gardens[main_i].add_plant(plant)
            for i in selected_garden_idxs[1:]:
                self.gardens[main_i].add_garden(self.gardens[i])
                self.gardens.pop(i)
        else:
            new_garden = Garden(plant.letter)
            new_garden.add_plant(plant)
            self.gardens.append(new_garden)

    def total_price(self):
        res = 0
        for garden in self.gardens:
            area = garden.get_area()
            nbr_fences = garden.get_parimeter()
            res += area * nbr_fences
        return res


gardens = Gardens()

for y in range(grid_height):
    for x in range(grid_width):
        plant = Plant(x,y, grid[y][x])
        gardens.add_plant_to_garden(plant)

print(gardens.total_price())


