import random, pygame, math, sys, os, datetime
from pygame.locals import *
from pygame import mixer

#init pygame stuff
pygame.init()
mixer.init()

#import opengl engine stuff
from gpu.s_screen import *
from gpu.texture import *
from gpu.shader import *
from gpu.s_render import *
from structure.s_fps import SFps

#import Entity-Component-System class files
from structure.entity import *
from structure.component import *
from structure.processor import *
from structure.manager import Manager
from structure.world import *

from physics.s_move import SMove

from controls.s_human import SHuman 

#set up the window
FPS = 100
Window_y = int(1080/1.25)
Window_x = int(1920/1.25)


def main():
    #create our main surface
    sys_screen = SScreen(Window_x, Window_y, "simple component engine")
    sys_fps = SFps(FPS)
    
    #create a manager
    man = Manager()
    #fill the manager
    for e in range(0,1500):

        #add components to the entity
        x = random.uniform(-1.0,1.0)
        y = random.uniform(-1.0,1.0)
        s = random.uniform(0.01,0.10)

        b = CBody(x,y,s)
        m = CMove(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0))
    
        man.add(e, b.typ, b)
        man.add(e, m.typ, m)
    
    #create player    
    #add components to the entity
    x=0.1#Window_x/2
    y=0.1#Window_y/2
    s = .1
    p = 100000000 #id of the player character; might create conflicts!
    b = CBody(x,y,s)
    m = CMove(0.00,0.00)


    cam = CCamera(1.0)     #create a camera
    man.add(p, cam.typ, cam)

    
    man.add(p, b.typ, b)
    man.add(p, m.typ, m)
    man.group_create('player',[p])

    
    #create systems
    sys_render = SRender(Texture("data/images/Acid.png"))
    sys_move = SMove()
    sys_human = SHuman(p)
    
    #some systems may need deltaT input
    deltaT = 0.0

    # -- MAINLOOP --
    while True:
        #move
        sys_move.step(man, deltaT)
               
        #send new positions to gpu and render them
        sys_render.step(man.get_all_components('body'), man.get(p,'body'), man.get(p,'camera'))

    # -- MAINLOOP END --
        user_input(man, sys_human)
        sys_screen.step()
        #limit the fps of the mainloop
        deltaT = sys_fps.step()
        deltaT = min(0.1,deltaT) #simulation runs at max with x seconds as deltaT

def user_input(man, sys_human):
    
        # event handling loop
        for event in pygame.event.get(): 
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                print('Exit Game')
                pygame.quit()
                sys.exit()

        #Player Movements
        pygame.event.pump()
        keyArray = pygame.key.get_pressed()
        
        #control x and y
        contx = 0.0
        conty = 0.0

        #check arrow and wasd keys
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
        sys_human.step(man, contx, conty)


if __name__ == '__main__':
    main()
