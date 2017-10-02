import random, pygame, math, sys, os, datetime
from pygame.locals import *
from pygame import mixer

#init pygame stuff
pygame.init()
mixer.init()

#import my component stuff
from entity import *
from component import *
from processor import *
from world import *
from loader import *


#set up the window
FPS = 30
Window_y = 1080
Window_x = 1920


#
#2017-09-29
#todo:
#
#multithreading?
#some components should be global
#fix inheritance from those base calsses
#openGL instead of blit
#code cleanup
#make enemies and player collide
#add background
#add camera
#chunks/checkerboard world maps?
#different image depending on the move direction
#remove enemy / kill / delete
#hp component
#write loader class
#




def main():
    #create our main surface
    DISPLAYSURF = pygame.display.set_mode((Window_x,Window_y),pygame.FULLSCREEN)
    pygame.display.set_caption('BasicEngine')
    BGCOLOR = (10,10,10)

    #create a clock object:
    DELTAT = 0
    FPSCLOCK = pygame.time.Clock()
    DeltaClock = pygame.time.Clock()
    FpsUpdateClock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT+1, 500)#how often shall the fps clock get updated?
    frames = 0

    fps = FpsTimer(5,5,"FPS: ",16)

    

    #load image
    data=Data()
    data.load_all_images()
    

    #load sound
    wavPath = os.path.join("art","sound","test.wav")
    wav = pygame.mixer.Sound(wavPath)

    #create test enemies
    enemies = []
    for i in range(0,500):
        temp = Enemy(random.uniform(0,Window_x), random.uniform(0,Window_y), data.img['enemy'], wav)
        enemies.append(temp)
    
    #create player
    player = Player(1000, 500, data.img['player'], wav)
    
    #create processors
    pro_painter = Processor_Painter(DISPLAYSURF)
    pro_audio = Processor_Sound()
    pro_move = Processor_Move()
    pro_text = Processor_Text(DISPLAYSURF, pygame.font.Font('freesansbold.ttf', 16))
    pro_ai = Processor_Artificial()
    pro_ai2 = Processor_Follow()

    pro_control = Processor_HumanControl()

    #create a world
    w = World()

    while True:

        DISPLAYSURF.fill(BGCOLOR)
        Time = FPSCLOCK.get_time()
        if(Time>0):
            fps.updateText(str(1000/Time))

        # MAINLOOP
        for tom in enemies:
            pro_painter.process(tom)
            #pro_audio.process(tom)
            #pro_ai.process(tom, enemies)
            pro_ai2.process(tom, player)
            pro_move.process(tom)

        pro_painter.process(player)
        #pro_audio.process(player)
        pro_move.process(player)
        pro_text.process(player)

        pro_text.process(fps)
        # MAINLOOP END

              
        # event handling loop
        for event in pygame.event.get(): 
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                print('Exit Game')
                pygame.quit()
                sys.exit()
                
        #Player Movements
        pygame.event.pump()
        keyArray = pygame.key.get_pressed()
        
        contx= 0.0
        conty=0.0
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
        
        pro_control.process(player,contx, conty)
                
                
        #Redraw the screen and wait a clock tick.
        pygame.display.update()
        pygame.time.wait(1)
        frames +=1
        FPSCLOCK.tick(FPS)

        #Deltat = the amount of time wich has passed since last delta.Clock.tick() call:
        DELTAT = DeltaClock.tick()
        

if __name__ == '__main__':
    main()
