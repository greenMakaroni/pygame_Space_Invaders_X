# made by "Dawid Markieton"
# Student at De Montfort University 2019~
# My first Video Game Ever ( also nuclear test site )

import pygame
import random
import math
import time

# Initialize the pygame
pygame.init()

# -----------------------------Creating Main screen-----------------------------
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
# TITLE OF SCREEN AND ICON
pygame.display.set_caption("     S P A C E   I N V A D E R S   X    ")
icon = pygame.image.load('spaceship.png')
bg = pygame.image.load('spacebg.png')
pygame.display.set_icon(icon)

#score variable
score = 0

#colors
white = (255,255,255)
black = (0,0,0)
red = (150,0,0)
bright_red = (255,0,0)
green1 = (0,150,0)
bright_green = (0,255,0)
blue1 = (2,128,218)
gold = (255,223,0)
yellow = (255,255,0)



#----------------------------CREATE WELCOME/PAUSE SCREEN---------------------------------
#GREEN BUTTON CHANGES SO ITS VARIABLE
green_button_state = " S T A R T "

def welcome_screen():
    global black
    global green1
    global bright_green
    global green_button_state 
    
    welcome = True
    while welcome:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("S P A C E   I N V A D E R S   X", largeText)
        TextRect.center = ((400),(100))
        screen.blit(TextSurf, TextRect)
   
        #DRAWING BASES FOR BUTTONS     
        button(green_button_state, 200, 248, 400, 48, white, blue1, main_loop)      
        button(" Q U I T ", 200, 500, 400, 48, white, blue1, quitgame)

        if player_health != 5:
            button(" R E S E T ", 200, 376, 400, 48, white, blue1, main_loop) #reset on ready yet
            
        
        pygame.display.update()

    main_loop()


    
#------------------------------ TEXT OBJECTS------------------------------------

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()


    
#--------------------------BUTTON FUNCTION-------------------------------------
# why did you make me do this 
def quitgame():
    pygame.quit()
    quit()
    
def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(screen,ic,(x,y,w,h))
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x, y, w, h))
        smallText = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)))
        screen.blit(textSurf, textRect)
        if click[0] == 1 and action != None:
            action()
        elif click[0] == 1 and action == quitgame:
            quitgam

    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))

        smallText = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)))
        screen.blit(textSurf, textRect)

#-----------------------------RESET--------------------------------------
##def reset():
##    global player_health
##    global score
##    global enemyX
##    global enemyY
##    global bulletX
##    global bulletY
##    global enemy_bulletX
##    global enemy_bulletY
##    global bullet_state
##    global heal_plus_two_state
##    global heal_plus_one_state
##    global enemy_bullet_state
##    global running
##
##    running = False
##    
##    player_health = 5
##    bullet_state = "ready"
##    heal_plus_two_state = "ready"
##    heal_plus_one_state = "ready"
##    enemy_bullet_state = "ready"
##    bulletX = 0
##    bulletY = 0
##    playerX = 370
##    playerY = 480
##    enemyX = []
##    enemyY = []
##      
##    for i in range(number_of_enemies):
##        enemyX.append(random.randint(0, 770))
##        enemyY.append(random.randint(50, 200))
##          
##    enemy_bulletX = []
##    enemy_bulletY = []
##    enemyX.append(random.randint(0, 770))
##    enemyY.append(random.randint(50, 200))
##
##    heal_plus_oneX = 850
##    heal_plus_oneY = 850
##    heal_plus_twoX = 850
##    heal_plus_twoY = 850
##
##    running = True
##    
##    main_loop()

# --------------------------------CREATE AND DRAW PLAYER---------------------------
player_health = 5
player_health = int(player_health)

playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

def healthbar(playerX, playerY, player_health):
    pygame.draw.rect(screen, black,(playerX +5, playerY +49, 41, 8)) 
    for i in range(player_health):
            if i >= 10:
                pygame.draw.rect(screen, gold,(playerX + ((i - 10) * 8) +6, playerY + 50 , 6, 6))
            elif i >= 5:               
                pygame.draw.rect(screen, blue1,(playerX + ((i - 5) * 8) +6, playerY + 50 , 6, 6))
            else:           
                pygame.draw.rect(screen, green1,(playerX + (i * 8) +6, playerY + 50 , 6, 6))
                 
def player(x, y):
    global player_health
    # Drawing a player takes 2 arguments, (shape or image) and (x, y) coordinates
    screen.blit(playerImg, (x + 10, y))
    healthbar(x, y, player_health)



# --------------------------------CREATE AND DRAW BULLET---------------------------

bulletImg = pygame.image.load('missile.png')
bulletX = 0
bulletY = 0
bulletY_change = 7
bullet_state = "ready"                 

def fire_bullet(x, y):
    global bullet_state
    global bulletY
    global bulletY_change
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 10, y))

    

#-----------------------------COLLISION CHECK----------------------------------------- 

def isCollision(bulletX, enemyX, bulletY, enemyY):
    d = math.sqrt(math.pow(bulletX-enemyX,2) + math.pow(bulletY-enemyY,2))
    if d < 20:
        return True
    else:
        return False   



#-----------------------------EXPLOSION AND PORTAL----------------------------------------- 
explo = pygame.image.load('blast.png')


def explosion(x,y):
    screen.blit(explo, (x + 10, y))



#---------------------------------CREATE AND DRAW ENEMIES----------------------------
number_of_enemies = 6

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 770))
    enemyY.append(random.randint(50, 200))
    enemyX_change.append(2)
    enemyY_change.append(40)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x+10, y))



#-----------------------------ENEMY BULLETS---------------------------------------
enemy_bullet_state = []
enemy_bulletImg = []
enemy_bulletX = []
enemy_bulletY = []
enemy_bulletY_change = 5

for i in range(number_of_enemies):
    enemy_bulletImg.append(pygame.image.load('laser.png'))
    enemy_bullet_state.append("ready")
    enemy_bulletX.append(enemyX[i])
    enemy_bulletY.append(enemyY[i])

def enemy_bullet(x, y, i):
    global enemy_bullet_state
    global enemy_bulletY
    global enemy_bulletY_change
    enemy_bullet_state[i] 
    screen.blit(enemy_bulletImg[i], (x+10, y))
    
#----------------------------------LOOT----------------------------------------------
##  1 = Hp + 1
##  2 = Hp + 2
##  3 = Bomb
##  4 = 10 extra coins
##
##
##
    
number_of_loot = 0


# HP + 1
heal_plus_one_state = "ready"
heal_plus_oneImg = pygame.image.load('plus.png')
heal_plus_oneX = 850
heal_plus_oneY = 850
heal_plus_oneY_change = 1

def heal_plus_one(x,y):
    global heal_plus_one_state
    global heal_plus_oneY
    global heal_plus_oneY_change
    heal_plus_one_state = "fire"
    screen.blit(heal_plus_oneImg, (x+10, y))
     
# HP + 2   
heal_plus_two_state = "ready"
heal_plus_twoImg = pygame.image.load('plustwo.png')
heal_plus_twoX = 850
heal_plus_twoY = 850
heal_plus_twoY_change = 1

def heal_plus_two(x,y):
    global heal_plus_two_state
    global heal_plus_twoY
    global heal_plus_twoY_change
    heal_plus_two_state = "fire"
    screen.blit(heal_plus_twoImg, (x+10, y))

def give_loot(x,y):
    global heal_plus_one_state
    global heal_plus_two_state
    global heal_plus_oneX
    global heal_plus_oneY
    global heal_plus_twoX
    global heal_plus_twoY
    
    loot_randomizer = random.randint(1,3)
    
    if loot_randomizer == 1 and heal_plus_one_state == "ready":
        heal_plus_one_state = "fire"
        heal_plus_oneX = x
        heal_plus_oneY = y
      
    elif loot_randomizer == 2 and heal_plus_two_state == "ready":
        heal_plus_two_state = "fire"
        heal_plus_twoX = x
        heal_plus_twoY = y
        
    
        
    

#-----------------------------GAME LOOP---------------------------------------------
main_running = True

def main_loop():
    global playerX
    global playerX_change
    global bulletX_change
    global bulletX
    global bulletY
    global bulletY_change
    global score
    global bullet_state
    global enemy_bullet_state
    global green_button_state
    global player_health
    global number_of_enemies
    global loot
    global heal_plus_one_state
    global heal_plus_oneX
    global heal_plus_oneY
    global heal_plus_twoY
    global heal_plus_twoX
    global heal_plus_two_state
    global main_running
    

    while main_running:
               
        # RGB Background (surface) FILL
        screen.blit(bg,(0,0))

        # CHECKS FOR KEYS INPUTS AND MOVES PLAYER
        for event in pygame.event.get():                    # EX FOR EXIT
            if event.type == pygame.QUIT:
                running = False   
            
            if event.type == pygame.KEYDOWN:                

                if event.key == pygame.K_LEFT:              # IF LEFT ARROW KEY IS PRESSED
                    playerX_change = -2
      

                if event.key == pygame.K_RIGHT:             # IF RIGHT ARROW KEY IS PRESSED
                    playerX_change = 2
       

                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        bulletX = playerX
                        bulletY = playerY
                        bullet_state = "fire"
                    else:
                        continue

                if event.key == pygame.K_ESCAPE:
                    green_button_state = " C O N T I N U E "
                    welcome_screen()
                    

            if event.type == pygame.KEYUP:                  # IF ANY KEY IS RELEASED
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                
        if playerX <= 0:
            playerX = 0
        elif playerX > 770:
            playerX = 770

        # BOUNDARY AND COLLISION DETECTION FOR EACH ENEMY
        for i in range(number_of_enemies):
            
            if enemyX[i] <= 0:
                enemyX[i] = 0
                enemyY[i] += enemyY_change[i]
                enemyX_change[i] *= -1     # changes direction

            elif enemyX[i] > 770:
                enemyX[i] = 770
                enemyY[i] += enemyY_change[i]
                enemyX_change[i] *= -1     # changes direction

            if enemyY[i] > 800:
                enemyX[i] = random.randint(0, 770)
                enemyY[i] = random.randint(50, 200)
                

            # Collision detection bullet/enemy
            if isCollision(bulletX, enemyX[i], bulletY, enemyY[i]):
                bulletX = 0
                bulletY = 0
                bullet_state = "ready"
                
                explosion(enemyX[i], enemyY[i])
                
                score += 1
                
                give_loot(enemyX[i],enemyY[i])
                
                #LOOT USES ENEMY X,Y THEREFORE GIVES IT BEFORE ENEMY GOES TO RANDOM POSITION
                
                enemyX[i] = random.randint(0, 770)
                enemyY[i] = random.randint(50, 200)
        
            
            else:
                pass

            
           # CREATE ENEMIES / MOVE THEM
    
            enemy(enemyX[i], enemyY[i], i)
            enemyX[i] += enemyX_change[i]
            
            #ENEMY BULLET STATE CHANGES WHEN ENEMYX EQUALS PLAYERX
            if enemyX[i] == playerX:
                if enemy_bullet_state[i] == "ready":
                    enemy_bullet_state[i] = "fire"
                    enemy_bulletX[i] = enemyX[i]
                    enemy_bulletY[i] = enemyY[i]
            else:
                continue

        #DRAWS BULLET IF ITS FIRE AND RESETS AFTER FLYING OVER 800 IN Y AXIS
        for i in range(number_of_enemies):
                       
            #CHECKS COLLISION ENEMY_BULLET - PLAYER
            if isCollision(enemy_bulletX[i], playerX, enemy_bulletY[i], playerY):
                enemy_bulletY[i] = enemyY[i]
                enemy_bullet_state[i] = "ready"
                explosion(playerX, playerY)
                if player_health == 0:
                    player_health = 0
                else:
                    player_health -= 1
                
                                           
            if enemy_bulletY[i] >= 800:
                enemy_bulletY[i] = enemyY[i]
                enemy_bullet_state[i] = "ready"
                
            if enemy_bullet_state[i] is "fire":
                enemy_bullet(enemy_bulletX[i], enemy_bulletY[i], i)
                enemy_bulletY[i] += enemy_bulletY_change
                
        #CHECK FOR COLLISION PLAYER/LOOT  + HP UPPER BOUNDARY
        if isCollision(heal_plus_oneX, playerX, heal_plus_oneY, playerY):
            if player_health < 15:
                player_health += 1

            elif player_health >= 15:
                player_health = 15
                
            heal_plus_oneX = 850
            heal_plus_oneY = 850
            heal_plus_one_state = "ready"

        if isCollision(heal_plus_twoX, playerX, heal_plus_twoY, playerY):
            if player_health <= 13:
                player_health += 2

            if player_health == 14:
                player_health += 1

            elif player_health >= 15:
                player_health = 15
                
            heal_plus_twoX = 850
            heal_plus_twoY = 850
            heal_plus_two_state = "ready"

        # if loot goes off map
        if heal_plus_oneY > 800:
            heal_plus_oneY = 850
            heal_plus_one_state = "ready"
            
        if heal_plus_twoY > 800:
            heal_plus_twoY = 850
            heal_plus_two_state = "ready"
            
        # if bullet hits the ceiling
        if bulletY < 0:
            bulletY = 0
            bullet_state = "ready"

        # if bullet has been fired
        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        if heal_plus_one_state is "fire":
            heal_plus_one(heal_plus_oneX, heal_plus_oneY)
            heal_plus_oneY += heal_plus_oneY_change
        
        if heal_plus_two_state is "fire":
            heal_plus_two(heal_plus_twoX, heal_plus_twoY)
            heal_plus_twoY += heal_plus_twoY_change
            

        # CHANGE POSITION FIRST THEN DRAW PLAYER
        playerX += playerX_change
        player(playerX, playerY)

       
        # Refresh everything on the screen at the end of one iterration of this loop
        pygame.display.update()



#---------------------------------CALL THE GAME-------------------------------------------
welcome_screen()

