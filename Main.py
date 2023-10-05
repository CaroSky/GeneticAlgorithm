import pygame, sys, time, random
from pygame.locals import *
from GAengine import GAEngine

simulator_speed = 50

# Threshold to determine if a Chromosome has reached the Food
REACH_THRESHOLD = 5 

# add colors as needed...
red_color = pygame.Color(255, 0, 0)
green_color = pygame.Color(0, 255, 0)
blue_color = pygame.Color(0, 0, 255)
black_color = pygame.Color(0, 0, 0)
white_color = pygame.Color(255, 255, 255)

pygame.init()
fps_clock = pygame.time.Clock()

play_surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Assignment 4 - DTE2501')

# initialize engine - you can experiment with different values for the population and food
ga = GAEngine()
ga.make_initial_population(100)
ga.add_food(1)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                running = False

    # Check if any individual has reached the food
    for individual in ga.get_population():
        for food in ga.get_foods():
            if individual.get_distance_to(food) < REACH_THRESHOLD:
                food.reduce_amount()
                pygame.time.wait(2) # Only included for fun - to see the food being reduced
                if food.get_amount() <= 0:
                    food.reposition()  # Reposition the food if it's consumed completely

    # Perform fitness assignment and crossover
    ga.assign_fitness()
    ga.do_crossover(50)

    play_surface.fill(white_color)
    for pp in ga.get_population():
        pygame.draw.rect(play_surface, black_color, Rect(pp.x_pos - 1, pp.y_pos - 1, 22, 22))
        pygame.draw.rect(play_surface, green_color, Rect(pp.x_pos, pp.y_pos, 20, 20))
    for food in ga.get_foods():
        food_size = food.get_amount() / 100 * 40
        pygame.draw.rect(play_surface, red_color, Rect(food.x_pos - food_size / 2, food.y_pos - food_size / 2, food_size, food_size))

    pygame.display.flip()

    fps_clock.tick(simulator_speed)