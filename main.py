import pygame

#This initializes pygame
pygame.init()

height = 800
width =600

#This creates the game screen
new_screen = pygame.display.set_mode((height,width))

#Below will be the code for the title of the game window that will be seen by the user as well as the Space Invaders icon (well the one that I am choosing to use).
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('launch.png')
pygame.display.set_icon(icon)
#Icon that we are using above is from : https://www.flaticon.com/authors/icongeek26


#Infinite Loop that houses the 'Events' in the game window.
# Also allows the window to close when the x is pressed. 
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
