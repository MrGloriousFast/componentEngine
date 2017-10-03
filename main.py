import random, pygame, math, sys, os, datetime
from pygame.locals import *
from pygame import mixer

#init pygame stuff
pygame.init()
mixer.init()

#import opengl engine stuff
from display import *
from texture import *
from shader import *
from instance import *

#import my component stuff
from entity import *
from component import *
from processor import *
from world import *
from loader import *
from movement import *


#set up the window
FPS = 100
Window_y = int(1080/1.25)
Window_x = int(1920/1.25)

#
#2017-10-02
#todo:

#create subfolders for all modules
#openGL (2D) instead of blit
#py2exe possible?

#multithreading?
#make enemies and player collide
#code cleanup

#chunks/checkerboard world maps?

#some components should be global (only one instance)
#fix inheritance from those base calsses
#write loader class
#hp component
#different image depending on the move direction
#remove enemy / kill / delete

#add background
#add camera

def main():
    #create our main surface
    dis = Display(Window_x, Window_y, "simple engine", FPS)
    
    #create camera
    cam = Camera((dis.w, dis.h))
    

    texture = Texture("art/graphic/Acid.png")
    inst = Instances(texture)

    #add instances  
    #create enemies
    enemies = []
    img = Texture("art/graphic/Acid.png")
    for _ in range(0,1000):
        x = random.uniform(-1.0,1.0)
        y = random.uniform(-1.0,1.0)
        e = Enemy( x, y, img)
        inst.append(e.get('body'))
        enemies.append(e)
    inst.create_dynamic_buffer()
    
    
    
    #create processors
    pro_move = Processor_Move()

    while True:
        #start measuring how long this loop will take and clear the screen
        dis.clear()
        # MAINLOOP
        
        t=[]
        for i, e in enumerate(enemies):
            pro_move.process(e)     
            t.extend(e.get('body').pos)
        inst.inst_pos = t

        inst.create_dynamic_buffer()
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
        
        #pro_control.process(player,contx, conty)
                
                
        

if __name__ == '__main__':
    main()
