#main game file
import pygame
from characters.player import *
import sys
#from things import * # sprite class

#move to setup file later
white = (255,255,255)
healthbar = pygame.image.load("images/healthbar.png")
health = pygame.image.load("images/health.png")
healthbarunits = 194        
#creating the player spite
player = Player("default",194)
player.set_positon(player.location[0],player.location[1])
pygame.font.init()



#player = Character("defult",1)
def movePlayer(direction):
    #adding movement to player, add in no areas later
    
    screen.blit(background,(0,0))
    #updateHP()
    if direction == "north":
        player.location[1] = player.location[1]-10
        player.set_positon(player.location[0],player.location[1])

    if direction == "south":
        player.location[1] = player.location[1]+10
        player.set_positon(player.location[0],player.location[1])
    if direction == "east":
        player.location[0] = player.location[0]+10
        player.set_positon(player.location[0],player.location[1])
    if direction == "west":
        player.location[0] = player.location[0]-10
        player.set_positon(player.location[0],player.location[1])
#    screen.blit(playerImage,player.location)
    
    block_group.draw(screen)
    pygame.display.update()
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



pygame.init()
screen = pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill(white)
screen.blit(background,(0,0))
pygame.display.update()
block_group=pygame.sprite.Group()
block_group.add(player)
block_group.draw(screen)
while True:
    updateHP(0)
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
