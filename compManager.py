from component import *

class Manager:
    def __init__(self):
        self.components = []
        
    def add(self, c):
        self.components.append(c)
    
    def get(self, typ):
        for c in self.components:
            if(c.type == typ):
                return c
