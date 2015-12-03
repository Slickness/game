#main game file
import pygame
from characters.player import *
from characters.blocks import *
from characters.enemy import *
import sys
from pygame.locals import *

#import pyscroll
from pytmx.util_pygame import load_pygame
import pytmx

rect_color = (255,0,0)
poly_color = (0,255,0)

def displayMap(level):
    #show the map using tmx tiles
    global screenWidth
    global screenHeight
    global screen 
    gameMap = load_pygame(level)
    for layer in gameMap.visible_layers:
        if isinstance(layer,pytmx.TiledTileLayer):
            for x,y,image in layer.tiles():
                screen.blit(image,(x*gameMap.tilewidth,y*gameMap.tileheight))
        elif isinstance(layer,pytmx.TiledObjectGroup):
            for obj in layer:
                if hasattr(obj,'col'):
                #    pygame.draw.lines(screen,poly_color,obj.closed,obj.points,3)
                    pass
                elif obj.image:
                    screen.blit(obj.image,(obj.x,obj.y))
        elif isinstance(layer,pytmx.TiledImageLayer):
            screen.blit(layer.image,(0,0))
    for obj in gameMap.objects:
        blocker_group.add(Blocks(obj.x,obj.y,obj.width,obj.height))
         
    
            
def battle(player,enemy):
    global moveNorth
    global moveSouth
    global moveEast 
    global moveWest 
    moveSouth = False
    moveNorth = False
    moveEast = False
    moveWest = False
    #print (player.name)
    #print (enemy.hp)
    #enemy.UpdateHP(-10)
    #print (enemy.name)
    #print (enemy.hp)
    x = True    
    while x == True:
        clock.tick(20)
        updateHP(0)

        background = pygame.Surface(screen.get_size())
        background.fill(white)
        screen.blit(background,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    print ("hit 0")
                    enemy_group.remove(enemy)
                    print (enemy.name)
                    #displayMap("images/level1.tmx")
                    x = False
def movePlayer(direction):
    #adding movement to player, add in no areas later
    # add variable for distance moved instead of number
    moveSize = 8
    global screenWidth
    global screenHeight
    if direction == "north":
        player.location[1] = player.location[1]-moveSize
        if player.location[1] < 0:
            player.location[1] = 0
        player.set_position(player.location[0],player.location[1])
        if len(pygame.sprite.spritecollide(player,blocker_group,False)) > 0:
            player.location[1] = player.location[1]+moveSize
        player.set_position(player.location[0],player.location[1])
    if direction == "south":
        player.location[1] = player.location[1]+moveSize
        if player.location[1] > screenHeight-32:
            player.location[1] = screenHeight-32
        player.set_position(player.location[0],player.location[1])
        
        if len(pygame.sprite.spritecollide(player,blocker_group,False)) > 0:
            player.location[1] = player.location[1]-moveSize
        player.set_position(player.location[0],player.location[1])
    if direction == "east":
        player.location[0] = player.location[0]+moveSize
        if player.location[0] > screenWidth-32:
            player.location[0] = screenWidth-32
        player.set_position(player.location[0],player.location[1])

        if len(pygame.sprite.spritecollide(player,blocker_group,False)) > 0:
            player.location[0] = player.location[0]-moveSize
        player.set_position(player.location[0],player.location[1])
    if direction == "west":
        player.location[0] = player.location[0]-moveSize
        if player.location[0]<0:
            player.location[0] = 0
        player.set_position(player.location[0],player.location[1])
        if len(pygame.sprite.spritecollide(player,blocker_group,False)) > 0:
            player.location[0] = player.location[0]+moveSize
        player.set_position(player.location[0],player.location[1])
    displayMap("images/level1.tmx")
    enemies = pygame.sprite.spritecollide(player,enemy_group,False,False)
    for enemy in enemies:
        enemy.attack = True
    for enemy in enemy_group:
        if enemy.attack == True:
            battle(player,enemy)
            enemy.attack = False
def updateHP(x):
    #x is how much to lower the xp
    player.UpdateHP(x)
    screen.blit(healthbar,(5,5))
    for health1 in range(int(player.hp)):
        screen.blit(health,(health1+8,8))
    if player.isDead():
        
        fonts = pygame.font.SysFont("monospace",40)
        label = fonts.render("you are dead",1,(0,0,0))
        screen.blit(label,(100,240))
    pygame.display.update()


#move to setup file later
white = (255,255,255)
healthbar = pygame.image.load("images/healthbar.png")
health = pygame.image.load("images/health.png")
healthbarunits = 194        
screenWidth = 704
screenHeight = 704
#creating the player spite
player = Player("default",194)
badGuy = Enemy("badguy",50)
badGuy2 = Enemy("worse",75)
badGuy.set_position(450,450)
badGuy2.set_position (200,200)

player.addImage("images/player.png")
player.set_position(player.location[0],player.location[1])
pygame.font.init()


pygame.init()
screen = pygame.display.set_mode((screenWidth,screenHeight))
background = pygame.Surface(screen.get_size())
background.fill(white)
screen.blit(background,(0,0))
block_group=pygame.sprite.Group()
enemy_group=pygame.sprite.Group()

blocker_group=pygame.sprite.Group()
enemy_group.add(badGuy)
enemy_group.add(badGuy2)
block_group.add(player)
block_group.draw(screen)
pygame.mouse.set_visible(0)
pygame.display.set_caption("RPG Game")
clock = pygame.time.Clock()
displayMap("images/level1.tmx")
block_group.draw(screen)
#variables to hold for keep moving

global moveNorth
global moveSouth
global moveEast 
global moveWest 
moveNorth = False
moveSouth = False
moveEast = False
moveWest = False

while True:
    clock.tick(20)
    
    updateHP(0)
    if moveNorth == True:
        movePlayer("north")
    if moveSouth == True:
        movePlayer("south")
    if moveEast == True:
        movePlayer("east")
    if moveWest == True:
        movePlayer("west")
    block_group.draw(screen)
    enemy_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                updateHP(-5)
            if event.key == pygame.K_UP:
                moveNorth = True
            if event.key == pygame.K_DOWN:
                moveSouth = True
            if event.key == pygame.K_RIGHT:
                moveEast = True
            if event.key == pygame.K_LEFT:
                moveWest = True

        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_UP:
                moveNorth = False
            if event.key == pygame.K_DOWN:
                moveSouth = False
            if event.key == pygame.K_RIGHT:
                moveEast = False
            if event.key == pygame.K_LEFT:
                moveWest = False
