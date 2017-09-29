from compManager import *
from entity import *
from component import *


class Entity:
    def __init__(self):
        self.id = 0
        self.components = Manager()
        
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
        self.components.add(comp_posi)
        self.components.add(comp_img)
        self.components.add(comp_sound)
        self.components.add(comp_speed)
        self.components.add(comp_text)
        
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
        self.components.add(comp_posi)
        self.components.add(comp_img)
        self.components.add(comp_sound)
        self.components.add(comp_speed)
        self.components.add(comp_text)
