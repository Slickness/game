from .character import *

class Player(Character):
    def __init__(self,name,hp,info,spell):
        Character.__init__(self,name,hp)
        self.spell = spell
        self.info = info


