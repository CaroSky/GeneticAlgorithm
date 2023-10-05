import math, random

# base class for simulator
class GAPoint:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    # find the distance to another object
    def get_distance_to(self, other):
        return math.sqrt(math.pow(self.x_pos - other.x_pos, 2) + math.pow(self.y_pos - other.y_pos, 2))


class Chromosome(GAPoint):
    # x_pos and y_pos are the features of our chromosome
    def __init__(self, x_pos, y_pos):
        self.fitness = 0
        super().__init__(x_pos, y_pos)

    # encode X-Y position into low-level representation
    def encode_position():
        pass
    
    # decode X-Y position from low-level representation
    def decode_position():
        pass

    # produce a new offspring from 2 parents
    def crossover(self, other):
        # perform crossover by taking the average of the x and y positions of two parents
        child_x = (self.x_pos + other.x_pos) / 2
        child_y = (self.y_pos + other.y_pos) / 2
        return Chromosome(child_x, child_y)

    # mutate the individual
    def mutate(self):
        mutation_range = 20 # Defines the range within which the mutation can occur
        # randomly adjust the x and y positions
        self.x_pos += random.randint(-mutation_range, mutation_range)
        self.y_pos += random.randint(-mutation_range, mutation_range)
        # Ensure positions remain within the screen dimensions
        self.x_pos = max(0, min(790, self.x_pos))
        self.y_pos = max(0, min(590, self.y_pos))


class Food(GAPoint):
    def __init__(self, x_pos, y_pos):
        self.amount = 100
        super().__init__(x_pos, y_pos)

    def reduce_amount(self):
        self.amount -= 1

    def get_amount(self):
        return self.amount

    # respawn food when depleted
    def reposition(self):
        self.amount = 100
        self.x_pos = random.randint(10, 790)
        self.y_pos = random.randint(10, 590)