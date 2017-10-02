from entity import *
from component import *
import pygame


class Entity:

    def __init__(self):
        self.id = 0
        self.components = {}
        
    def add(self, c):
        self.components[c.type] = c
    
    def get(self, typ):
        if(typ in self.components):
            return self.components[typ]
        else:
            print('error - request non existing component ' + str(typ))
            
    def contains(self,typ):
        return self.components.contain(typ)


class Enemy(Entity):
    def __init__(self, x, y, img, wav):
        Entity.__init__(self)
        
        #image bigger!
        img = pygame.transform.scale(img, (48,48))
    
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
        Entity.__init__(self)
                
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
        Entity.__init__(self)
    
        comp_posi = Component_Position(x,y)
        comp_text = Component_Text(text)
        comp_text.color = (255,255,255)
        
        self.text = text
        
        self.add(comp_posi)
        self.add(comp_text)
        
    def updateText(self, string):
        self.get('text').text = str(self.text) + str(string)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
