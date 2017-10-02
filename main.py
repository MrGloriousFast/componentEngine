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
FPS = 30
Window_y = int(1080/1.25)
Window_x = int(1920/1.25)

#
#2017-10-02
#todo:

#create subfolders for all modules
#openGL (2D) instead of blit

#
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
    
    #make a point
    shader = AShader('default')
    a=CQuad()
    verticies = a.verticies
    texcords = a.texcords
    texture = Texture("art/graphic/Acid.png")
    inst = Instances( verticies, texcords, shader, texture)

    #add instances
    for i in range(0,100):    
        inst.append(CBody(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0)).pos)
        #inst.append([0.7-i/100,1-i/100,0.0])
    inst.createBuffer_pos()


    while True:
        #start measuring how long this loop will take and clear the screen
        dis.clear()
        # MAINLOOP

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
