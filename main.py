import pygame

#This initializes pygame
pygame.init()

width = 800
height = 600


#This creates the game screen
new_screen = pygame.display.set_mode((width,height))

#Below will be the code for the title of the game window that will be seen by the user as well as the Space Invaders icon (well the one that I am choosing to use).
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('launch.png')
pygame.display.set_icon(icon)
#Icon that we are using above is from : https://www.flaticon.com/authors/icongeek26

#Adding the player's "character"

player_image = pygame.image.load('player-ship.png')

#Player coordinates when the game starts up
playerX = 370
playerY = 480

def player():
    new_screen.blit(player_image,(playerX,playerY))


#Infinite Loop that houses the 'Events' in the game window.
# Also allows the window to close when the x is pressed. 
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    
    #This will work for background, the three values are the RGB colors
    new_screen.fill ((0,0,0))
    
    #screen.fill always needs to be above the player so that it acts as the background, and is not in front of the player's character.
    player()
    pygame.display.update()