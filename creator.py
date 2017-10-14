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
    s = random.uniform(0.01,0.10)

    b = CBody(x,y,s)
    m = CMove(random.uniform(-0.2,0.2),random.uniform(-0.2,0.2))

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
    manager.group_create('player',[i])
    return i

