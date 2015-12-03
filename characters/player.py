from .character import *

class Player(Character):
    def __init__(self,name,hp,weapon = 1,armour=0):
        Character.__init__(self,name,hp,weapon,armour)
        self.moves = 2
        self.attack = False
		#self.picture = picture
        #self.image, self.rect = load_image(picture, -1)
        #self.location = [100,100]
    
