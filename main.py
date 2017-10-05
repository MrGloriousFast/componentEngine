import random, pygame, math, sys, os, datetime
from pygame.locals import *
from pygame import mixer

#init pygame stuff
pygame.init()
mixer.init()

#import opengl engine stuff
from gpu.display import *
from gpu.texture import *
from gpu.shader import *
from gpu.s_render import *

#import my component stuff
from structure.entity import *
from structure.component import *
from structure.processor import *
from structure.manager import Manager
from structure.world import *
from data.loader import *

#set up the window
FPS = 100
Window_y = int(1080/1.25)
Window_x = int(1920/1.25)

"""
#2017-10-05


--emergency--

--inprogress--

rework systems(processors) and components to fit better into our manager
    systeme müssen sortierte componenten listen bekommen
    wenn ein system zwei komponte bruacht ists vllt wichtig das sie vom selben entity sind
    make a O(n**2) collision detection on the gpu similiar to instance class

--testing--

component manager
    be weary of intercomponent communication
    some components should be global (only one instance)
    code cleanup
    variable cleanup in manager
    one image is not moving(entity_id collision)
    need entity id manager(singleton?)
    

--done--

--icebox--

working file for phillip
    need wine to run py2exe or pyinsstaller or cxfreeze may even need vm
    Seems hard to set up but possible
    2017-10-04 

render player

isDead flag and removal of objects

runtime entity creation

play sound

support more than one texture

turn instance class into processor component model

buffer streaming

drehen spiegeln der bilder
different image depending on the move direction

multithreading?
make enemies and player collide
code cleanup

chunks/checkerboard world maps?

fix inheritance from those base calsses
write loader class
hp component

remove enemy / kill / delete

add background
add camera
"""

def main():
    #create our main surface
    dis = Display(Window_x, Window_y, "simple engine", FPS)
    


    #create a manager
    man = Manager()
    #fill the manager
    for e in range(0,1000):


        #add components to the entity
        x = random.uniform(-1.0,1.0)
        y = random.uniform(-1.0,1.0)
        s = random.uniform(0.01,0.10)

        b = CBody(x,y,s)
        m = CMove(0.001,0.001)
    
        man.add(e, b.typ, b)
        man.add(e, m.typ, m)
    
    
    

        
    #create player    
    #add components to the entity
    x=0.1#Window_x/2
    y=0.1#Window_y/2
    s = .1
    p = -1 #id of t he player character; might create conflicts!
    b = CBody(x,y,s)
    m = CMove(0.00,0.00)
    
    man.add(p, b.typ, b)
    man.add(p, m.typ, m)
    man.group_create('player',[p])
       
    
    #create systems
    sys_render = SRender(Texture("data/images/Acid.png"))

    pro_move = Processor_Move()
    pro_human = Processor_HumanControl()
    
    while True:
        #start measuring how long this loop will take and clear the screen
        dis.begin_frame()
        # MAINLOOP
        
        #for all entities that have a body and a move component
        for E_ID in man.get_all_type_list(['body','move']): 
            body = man.get(E_ID, 'body')
            move = man.get(E_ID, 'move')
            #move them            
            pro_move.process(body, move)
               
        #prepare new body positions for gpu
        sys_render.stream( man.get_all_components('body'))

        #render
        sys_render.step()


        # MAINLOOP END

        dis.flip()
              
        # event handling loop
        for event in pygame.event.get(): 
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                print('Exit Game')
                pygame.quit()
                sys.exit()
                
        #Player Movements
        pygame.event.pump()
        keyArray = pygame.key.get_pressed()
        
        contx = 0.0
        conty = 0.0

        if(keyArray[273] or keyArray[119]):#UP+W
            conty = 1.0
        elif(keyArray[274] or keyArray[115]):#DOWN+S
            conty = -1.0
        else:
            conty = 0.0

        if(keyArray[276] or keyArray[97]):#LEFT+A
            contx = -1.0
        elif(keyArray[275] or keyArray[100]):#RIGHT+D
            contx = 1.0
        else:
            contx = 0.0
        
        #process the change direction from keypresses to the human control processor
        pid = man.group_get('player')
        for i in pid:
            pro_human.process(man.get(i,'move'), contx, conty)
                
        dis.finish_frame()
        

if __name__ == '__main__':
    main()
