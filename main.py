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
from gpu.instance import *

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
#2017-10-04


--emergency--

--inprogress--

component manager
    one dict for all comoponents of one type
    be weary of intercomponent communication
    entities need ids
    some components should be global (only one instance)

--testing--

--done--

--icebox--

working file for phillip
    need wine to run py2exe or pyinsstaller or cxfreeze may even need vm
    Seems hard to set up but possible
    2017-10-04 

render the player

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
    
    #create camera
    cam = Camera((dis.w, dis.h))
    

    texture = Texture("data/images/Acid.png")
    inst = Instances(texture)


    #create a manager
    man = Manager()
    #fill the manager
    for e in range(0,5):
        for i in range(e,10):
            c_t = i
            c = "e_"+str(e)+" c_"+str(c_t)
            man.add(e, c_t, c)
    #get every entity with components C2, C4, C6
    l = man.get_all_type(2)
    print(l)
    ll = man.get_all_type_list([4,6])
    print(ll, [4,6])
    #make groups
    man.group_create('equal',[0,2,4,6,8])
    print(man.group_get('equal'))
    
    
    
    

    #add instances  
    #create enemies
    enemies = []
    img = Texture("data/images/Acid.png")
    for _ in range(0,100):
        x = random.uniform(-1.0,1.0)
        y = random.uniform(-1.0,1.0)
        e = Enemy( x, y, img)
        inst.append(e.get('body'))
        enemies.append(e)
        
    #create player
    x=Window_x/2
    y=Window_y/2
    player = Player(x,y,Texture("data/images/FatAssZombie.png"))
    inst.append(player.get('body'))
    
    #finalize the data for each enemy and the player and send it to the gpu
    inst.create_dynamic_buffer()
    
    
    
    #create processors
    pro_move = Processor_Move()
    pro_human = Processor_HumanControl()
    
    while True:
        #start measuring how long this loop will take and clear the screen
        dis.begin_frame()
        # MAINLOOP
        
        #t=[]
        #for eahc enemy move him and note the changes in a list
        #for i, e in enumerate(enemies):
        #    pro_move.process(e)     
            #inst.inst_pos[3*i+0]=e.get('body').pos[0]
            #inst.inst_pos[3*i+1]=e.get('body').pos[1]
            #inst.inst_pos[3*i+2]=e.get('body').pos[2]
        #    t.extend(e.get('body').pos)
        #the same for the player but only once
        #pro_move.process(player)     
        
        
        #inst.inst_pos[-3]=player.get('body').pos[0]
        #inst.inst_pos[-2]=player.get('body').pos[1]
        #inst.inst_pos[-1]=player.get('body').pos[2]
        
        #t.extend(player.get('body').pos)
        
        #update the positions list in the instance renderer
        #inst.inst_pos = t

        #send the data to the gpu
        #inst.create_dynamic_buffer()

        #render
        inst.render()


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
            conty = -1.0
        elif(keyArray[274] or keyArray[115]):#DOWN+S
            conty = 1.0
        else:
            conty = 0.0

        if(keyArray[276] or keyArray[97]):#LEFT+A
            contx = -1.0
        elif(keyArray[275] or keyArray[100]):#RIGHT+D
            contx = 1.0
        else:
            contx = 0.0
        
        #process the change direction from keypresses to the human control processor
        pro_human.process(player, contx, conty)
                
        dis.finish_frame()
        

if __name__ == '__main__':
    main()
