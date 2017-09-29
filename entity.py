from compManager import *
from entity import *
from component import *


class Entity:
    def __init__(self):
        self.id = 0
        self.components = Manager()
        
    def add(self,comp):
        self.components.add(comp)
        
    def get(self,typ):
        return self.components.get(typ)

class Enemy(Entity):
    def __init__(self, x, y, img, wav):
    
        #give us a components manager
        self.components = Manager()
        self.id = 0

        #create components
        comp_posi = Component_Position(x,y)
        comp_img = Component_Image(img)
        comp_sound = Component_Sound(wav)
        comp_speed = Component_Speed(0,0)
        comp_text = Component_Text('bla!')
        
        
        
        #add components to the entity
        self.add(comp_posi)
        self.add(comp_img)
        self.add(comp_sound)
        self.add(comp_speed)
        self.add(comp_text)
        
class Player(Entity):
    def __init__(self, x, y, img, wav):
        self.id = 0
        self.components = Manager()
        
        #create components
        comp_posi = Component_Position(x,y)
        comp_img = Component_Image(img)
        comp_sound = Component_Sound(wav)
        comp_speed = Component_Speed(0,0)
        comp_text = Component_Text('player')
               
        #add components to the entity
        self.add(comp_posi)
        self.add(comp_img)
        self.add(comp_sound)
        self.add(comp_speed)
        self.add(comp_text)
        
class FpsTimer(Entity):
    def __init__(self,x,y,text,size):
        self.id = 0
        self.components = Manager()
    
        comp_posi = Component_Position(x,y)
        comp_text = Component_Text(text)
        
        self.text = text
        
        self.add(comp_posi)
        self.add(comp_text)
        
    def updateText(self, string):
        self.get('text').text = str(self.text) + str(string)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
