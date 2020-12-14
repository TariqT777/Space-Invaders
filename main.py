import pygame
import random 
import math
from pygame import mixer

#This initializes pygame
pygame.init()

width = 800
height = 600


#This creates the game screen
new_screen = pygame.display.set_mode((width,height))

#Background
background = pygame.image.load('Galaxy-Background.jpg')

#Background Sound
mixer.music.load('backgroundMusic.mp3')
mixer.music.play(-1) #We use '-1' because this will cause the sound to continually loop.

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

#These variables will be used to deal with the key presses and therefore the movement of the player.
playerX_movement = 0
playerY_movement = 0

#Enemy

enemy_image = []
enemyX = []
enemyY = []
enemyX_movement = []
enemyY_movement = []
num_of_enemies = 6


for i in range(num_of_enemies):
    enemy_image.append(pygame.image.load('ufo.png'))

    #Enemy coordinates when the game starts up
    enemyX.append(random.randint(0,width - 65))
    enemyY.append(random.randint(50,150))

    #These variables will be used to deal with the movement of the enemy.
    enemyX_movement.append(.5)
    enemyY_movement.append(40)
    #Function that will be executed to edit where the player's position is.

#Laser
laser_image = pygame.image.load('laser.png')


laserX = 0
laserY = 480


laserX_movement = 0
laserY_movement = .4

#Ready means that you can't see the laser on the screen.
#Fire means that the laser is currently moving and is visible.
laser_state = "ready"


#Score Section
score_value = 0
#Text font and x,y coordinates
text_font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#Game Over Text
gameOver_font = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    over_text = gameOver_font.render("GAME OVER", True, (255,255,255))
    new_screen.blit(over_text, (200, 250))

def show_score(x,y) :
    visible_score = text_font.render("Score : " + str(score_value),True, (255,255,255))
    new_screen.blit(visible_score, (x, y))

def player(x,y):
    new_screen.blit(player_image,(x,y))

def enemy(x,y,i):
    new_screen.blit(enemy_image[i],(x,y))

def fire_laser(x,y):
    global laser_state 
    laser_state = 'fire'
    #The '+ 16' will allow the bullet to appear from the center of the spaceship and the '+10' will allow the bullet to appear from the top of the nose of the ship.
    new_screen.blit(laser_image,(x + 16, y + 10))

#Function below will allow for collison 
#We will be using the distance formula to help us here

def isCollision(enemyX,enemyY,laserX,laserY):
    distance = math.sqrt(math.pow(enemyX-laserX,2) + (math.pow(enemyY-laserY,2)))
    if distance < 27 : #The 27 stands for 27 px
        return True


#Infinite Loop that houses the 'Events' in the game window.
# Also allows the window to close when the x is pressed. 
game_running = True
while game_running:

    #This will work for background, the three values are the RGB colors
    new_screen.fill ((0,0,0))

    #Background Image. Needs to be below the screen.fill.
    new_screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    
        #This will check if a keystroke is being pressed and which key it is that is being pressed.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_movement = -1
            if event.key == pygame.K_RIGHT:
                playerX_movement = 1
            if event.key == pygame.K_SPACE:
                if laser_state is 'ready':
                    laser_sound = mixer.Sound('laserSound.wav')
                    laser_sound.play()
                    #Gets the current x coordinate of the player
                    laserX = playerX
                    fire_laser(laserX,laserY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_movement = 0
    #From the if statements above, this line below will be the guiding factor for where the player ends up based on their keystrokes.
    playerX += playerX_movement

#These two if statements provide the boundaries for the player's character.
    if playerX <= 0:
        playerX = 0
    if playerX > width - 64:
        playerX = width - 64
    #We do 'width - 64' here because the size of the image that we downloaded to use as this piece was of size 64 px.
    #This subtraction of 64 from the width allows us to alway see the whole ship, and if we were to remove the 64,
    #We would then have our ship still partially leaving the screen.
    
    #Laser Movement
    if laserY <= 0 :
        laserY = 480
        laser_state = 'ready'

    if laser_state is 'fire' :
        fire_laser(laserX,laserY) #If this statement isn't hear, the laser won't appear.
        laserY -= laserY_movement

    

    #screen.fill always needs to be above the call to the player function so that it acts as the background, and is not in front of the player's character.
    player(playerX,playerY)


    #### Enemy Movement Below
    for i in range(num_of_enemies):
        #The next few lines will help us to register when a player has lost, thus prompting a game over.
        if enemyY[i] > 440 :
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        
        enemyX[i] += enemyX_movement[i]

        if enemyX[i] <= 0:
            enemyX_movement[i] = .5 #We want the enemy to go the opposite direction in terms of the x - axis when it hits a boundary.
            enemyY[i] += enemyY_movement[i]
        if enemyX[i] > width - 64:
            enemyX_movement[i] = -.5 #We want the enemy to go the opposite direction in terms of the x - axis when it hits a boundary.
            enemyY[i] += enemyY_movement[i]
        enemy(enemyX[i],enemyY[i],i)

        #Collision 
        collision = isCollision(enemyX[i],enemyY[i],laserX,laserY)
        if collision : #Means if the collision function returns true
            hit_sound = mixer.Sound('alienHit.mp3')
            hit_sound.play()
            laserY = 480
            laser_state = 'ready'
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0,width - 65)
            enemyY[i] = random.randint(50,150)
    
    show_score(textX,textY)

    pygame.display.update()
