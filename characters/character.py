import pygame
blue = (0,0,255)
class Character(pygame.sprite.Sprite):
    def __init__(self,name,hp,weapon = 1, armour = 0,color=blue,width = 32,height = 32):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.location = [100,100]
     
    def attack(self,other):
        pass
    def set_position(self,x,y):
        self.rect.x=x
        self.rect.y=y
        

    def UpdateHP(self,value):
        self.hp = self.hp+value
        if self.hp < 0:
            self.hp = 0

    def isDead(self):
        if self.hp <= 0:
            return True
        else:
            return False
    def addImage(self,picture):
        
        self.image = pygame.image.load(picture)
        self.image = pygame.transform.scale(self.image,(32,32))

        self.rect = self.image.get_rect()
        
