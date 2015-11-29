#main game file
import pygame
from characters.player import *
from characters.blocks import *
import sys

#import pyscroll
from pytmx.util_pygame import load_pygame
import pytmx

rect_color = (255,0,0)
poly_color = (0,255,0)

def displayMap(level):
    global screenWidth
    global screenHeight
    global screen 
    #tileWidth = int(screenWidth/32)
    #tileHeight = int(screenHeight/32)
    #screenSize = (screenWidth,screenHeight)
    gameMap = load_pygame(level)
    #blockers = []
    for layer in gameMap.visible_layers:
        if isinstance(layer,pytmx.TiledTileLayer):
            for x,y,image in layer.tiles():
                screen.blit(image,(x*gameMap.tilewidth,y*gameMap.tileheight))
        elif isinstance(layer,pytmx.TiledObjectGroup):
            for obj in layer:
                if hasattr(obj,'col'):
                    pygame.draw.lines(screen,poly_color,obj.closed,obj.points,3)
                     
                elif obj.image:
                    screen.blit(obj.image,(obj.x,obj.y))
        elif isinstance(layer,pytmx.TiledImageLayer):
        
            screen.blit(layer.image,(0,0))
    for obj in gameMap.objects:
        #print (obj.x,obj.y,obj.width,obj.height)
        blocker_group.add(Blocks(obj.x,obj.y,obj.width,obj.height))
         
    #print (blockers)
    
    #blocker_group.add(Blocks(blockers))
            

def movePlayer(direction):
    #adding movement to player, add in no areas later
    # add variable for distance moved instead of number
    moveSize = 10
    
    #updateHP()
    global screenWidth
    global screenHeight
    if direction == "north":
        player.location[1] = player.location[1]-moveSize
        if player.location[1] < 0:
            player.location[1] = 0
        player.set_positon(player.location[0],player.location[1])
        if len(pygame.sprite.spritecollide(player,blocker_group,False)) > 0:
            player.location[1] = player.location[1]+moveSize
        player.set_positon(player.location[0],player.location[1])
    if direction == "south":
        player.location[1] = player.location[1]+moveSize
        if player.location[1] > screenHeight-32:
            player.location[1] = screenHeight-32
        player.set_positon(player.location[0],player.location[1])
        
        if len(pygame.sprite.spritecollide(player,blocker_group,False)) > 0:
            player.location[1] = player.location[1]-moveSize
        player.set_positon(player.location[0],player.location[1])
    if direction == "east":
        player.location[0] = player.location[0]+moveSize
        if player.location[0] > screenWidth-32:
            player.location[0] = screenWidth-move_size
        player.set_positon(player.location[0],player.location[1])

        if len(pygame.sprite.spritecollide(player,blocker_group,False)) > 0:
            player.location[0] = player.location[0]-moveSize
        player.set_positon(player.location[0],player.location[1])
    if direction == "west":
        player.location[0] = player.location[0]-moveSize
        if player.location[0]<0:
            player.location[0] = 0
        player.set_positon(player.location[0],player.location[1])
        if len(pygame.sprite.spritecollide(player,blocker_group,False)) > 0:
            player.location[0] = player.location[0]+moveSize
        player.set_positon(player.location[0],player.location[1])
    displayMap("images/level1.tmx") 
    #block_group.draw(screen)
    #pygame.display.update()
def updateHP(x):
    #player.UpdateHP(-10)
    player.UpdateHP(x)
    screen.blit(healthbar,(5,5))
    for health1 in range(int(player.hp)):
        screen.blit(health,(health1+8,8))
    if player.isDead():
        
        fonts = pygame.font.SysFont("monospace",40)
        label = fonts.render("you are dead",1,(0,0,0))
        screen.blit(label,(100,240))
    #screen.blit(playerImage,(200,200))
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
player.set_positon(player.location[0],player.location[1])
pygame.font.init()


pygame.init()
screen = pygame.display.set_mode((screenWidth,screenHeight))
background = pygame.Surface(screen.get_size())
background.fill(white)
screen.blit(background,(0,0))
block_group=pygame.sprite.Group()
blocker_group=pygame.sprite.Group()

block_group.add(player)

displayMap("images/level1.tmx")
block_group.draw(screen)

while True:
    updateHP(0)
    #blocker_group.draw(screen)
    block_hit_list = pygame.sprite.spritecollide(player,blocker_group,False)
    #print (block_hit_list)
    block_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                updateHP(-5)
            if event.key == pygame.K_UP:
                movePlayer("north")
            if event.key == pygame.K_DOWN:
                movePlayer("south")
            if event.key == pygame.K_RIGHT:
                movePlayer("east")
            if event.key == pygame.K_LEFT:
                movePlayer("west")
