import pygame

#This initializes pygame
pygame.init()

height = 800
width =600

#This creates the game screen
new_screen = pygame.display.set_mode((height,width))

game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
