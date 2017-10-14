#import Entity-Component-System class files
from structure.component import *
import random
from structure.manager import Manager

"""
this class will act as a blueprint creator of entities.
some entities will be created over and over again

"""


#create a default enemy    
def enemy(manager):
    i = manager.new_id()
    #add components to the entity
    x = 0.0#random.uniform(-1.0,1.0)
    y = 0.0#random.uniform(-1.0,1.0)
    s = 0.1*random.uniform(0.1,1.0)**2

    #just some random move directions, dont read too much into it
    b = CBody(x,y,s)
    speedx = random.uniform(-1,1)*random.uniform(-1,1)*random.uniform(-1,1)
    speedy = random.uniform(-1,1)*random.uniform(-1,1)*random.uniform(-1,1)
    m = CMove(speedx, speedy)

    manager.add(i,  b)
    manager.add(i,  m)
    return i
    
    
def player(manager):
    i = manager.new_id()
                
    #create player    
    #add components to the entity
    x=0.0
    y=0.0
    s = 0.15
    b = CBody(x,y,s)
    m = CMove(0.00,0.00)


    cam = CCamera(1.0)     #create a camera
    manager.add(i,  cam)

    
    manager.add(i,  b)
    manager.add(i,  m)
    #put the player into a tagged group. with manager.group_get('player') you can get this entity everywhere. like a global variable
    manager.group_create('player',[i])
    return i

