		
from .character import *

class Enemy(Character):
    def __init__(self,name,hp,weapon = 1,armour=0):
        Character.__init__(self,name,hp,weapon,armour)
        self.moves = 2
