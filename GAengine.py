import random
from Utils import Chromosome, Food

class GAEngine:
    
    def __init__(self, mutation_rate=0.05, max_population_size=100):
        self.mutation_rate = mutation_rate #probability of mutation set to 5% as default
        self.max_population_size = max_population_size #maximum allowed population size
        self.population = []
        self.food = []
        self.generations = 0

    def make_initial_population(self, population_size):       
        for i in range(population_size):
            self.population.append(Chromosome(random.randint(0, 790), random.randint(0, 590)))

    def add_food(self, no_of_food):     
        for i in range(no_of_food):
            self.food.append(Food(random.randint(0, 790), random.randint(0, 590)))

    def do_crossover(self, no_of_offspring):
        new_population = [] # Temporary list to store offspring
        for _ in range(no_of_offspring):
            parent1 = self.select_parent()
            parent2 = self.select_parent()
            # Ensure the parents are not the same individual
            while parent1 == parent2:
                parent2 = self.select_parent()
            child = parent1.crossover(parent2)
            
            # Mutate child based on mutation rate probability
            if random.random() < self.mutation_rate:
                child.mutate()

            new_population.append(child)

        #Elitism: carry forward the top 10% of current population
        new_population.extend(sorted(self.population, key=lambda x: x.fitness, reverse=True)[:int(0.1 * len(self.population))])
        self.population = new_population
        # Ensure the population doesn't exceed the maximum size by selecting the fittest individuals
        self.population = sorted(self.population, key=lambda x: x.fitness, reverse=True)[:self.max_population_size]

    def assign_fitness(self):
        # Assign fitness to each individual based on its distance to the closest food source
        for individual in self.population:
            closest_food_distance = min([individual.get_distance_to(food) for food in self.food])
            individual.fitness = 1 / closest_food_distance

    def select_parent(self):
        # Select a parent for crossover based on fitness
        total_fitness = sum(individual.fitness for individual in self.population)
        selection_point = random.uniform(0, total_fitness)
        for individual in self.population:
            selection_point -= individual.fitness
            if selection_point <= 0:
                return individual            

    def get_population(self):
        return self.population

    def get_foods(self):
        return self.food