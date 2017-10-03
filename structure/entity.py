from structure.entity import *
from structure.component import *
import pygame, pyrr, numpy, random


class Entity:

    def __init__(self):
        self.id = 0
        self.components = {}
        
    def add(self, c):
        self.components[c.typ] = c
    
    def get(self, typ):
        if(typ in self.components):
            return self.components[typ]
        else:
            raise ValueError('error - request non existing component: ' + str(typ))
            
    def contains(self,typ):
        return self.components.contain(typ)

class Camera(Entity):
    def __init__(self,x=0,y=0):
        Entity.__init__(self)
        
        self.add(CBody(x,y))

        #hard coded camera stuff
        self.fov = 70
        self.aspect = [16,9] 
        self.zNear = 0.01
        self.zFar = 1800
        
        self.speedTurn = 0.1
        self.speedMove = 100.
        
        
        """
        Your 2D transformation then is the combination of the Rotation, Scale, and Translation matrices:

        |1, 0, tx|   |cos(theta), -sin(theta), 0|   |sx, 0,  0|
        |0, 1, ty| * |sin(theta), cos(theta),  9| * |0,  sy, 0|
        |0, 0, 1 |   |0,          0,           1|   |0,  0,  1|
        """   

class Enemy(Entity):
    def __init__(self, x, y, img):
        Entity.__init__(self)
        
        #create components
        s = random.uniform(0.0001,0.1)

        #add components to the entity
        self.add(CBody(x,y,s))
        self.add(CMove(0.001,0.001))
        
class Player(Entity):
    def __init__(self, x, y, img):
        Entity.__init__(self)
                
        #add components to the entity
        self.add(CBody(x,y))
        self.add(CMove(0,0))
        self.add(CText('player'))
        
class FpsTimer(Entity):
    def __init__(self,x,y,text,size):
        Entity.__init__(self)
    
        comp_posi = CBody(x,y)
        comp_text = CText(text)
        comp_text.color = (255,255,255)
        
        self.text = text
        
        self.add(comp_posi)
        self.add(comp_text)
        
    def updateText(self, string):
        self.get('text').text = str(self.text) + str(string)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
