from compManager import *

class Entity:
    def __init__(self):
        self.id = 0
        self.components = Manager()
        
    def get(self,typ):
        return self.components.get(typ)
