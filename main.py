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

#These variables will be used to deal with the key presses and therefore the movement of the player;.
playerX_movement = 0
playerY_movement = 0

#Function that will be executed to edit where the player's position is.
def player(x,y):
    new_screen.blit(player_image,(x,y))


#Infinite Loop that houses the 'Events' in the game window.
# Also allows the window to close when the x is pressed. 
game_running = True
while game_running:

    #This will work for background, the three values are the RGB colors
    new_screen.fill ((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    
        #This will check if a keystroke is being pressed and which key it is that is being pressed.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_movement = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_movement = 0.3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_movement = 0

    playerX += playerX_movement

    if playerX <= 0:
        playerX = 0
    if playerX > width - 64:
        playerX = width - 64
    #We do width - 64 here because the size of the image that we downloaded to use as this piece was of size 64 px.
    #This subtraction of 64 from the width allows us to alway see the whole ship, and if we were to remove the 64,
    #We would then have our ship still partially leaving the screen.
    
    #screen.fill always needs to be above the call to the player function so that it acts as the background, and is not in front of the player's character.
    player(playerX,playerY)
    pygame.display.update()
