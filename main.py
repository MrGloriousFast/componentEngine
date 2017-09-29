import random, pygame, math, sys, os, datetime
from pygame.locals import *
from pygame import mixer

#init pygame stuff
pygame.init()
mixer.init()

#import my component stuff
from entity import *
from compManager import *
from component import *
from processor import *
from enemy import *

#set up the window
FPS = 60
Window_y = 720#1080
Window_x = 1280#1920


#
#2017-09-29
#todo:
#
#components have to be easier to get
#
#
#
#
#
#
#




def main():
    #create our main surface
    DISPLAYSURF = pygame.display.set_mode((Window_x,Window_y),pygame.FULLSCREEN)
    pygame.display.set_caption('BasicEngine')

    #create a clock object:
    DELTAT = 0
    FPSCLOCK = pygame.time.Clock()
    DeltaClock = pygame.time.Clock()
    FpsUpdateClock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT+1, 500)#how often shall the fps clock updated?
    frames = 0

    #load image
    imgPath = os.path.join("art","graphic","test.png")
    img = pygame.image.load(imgPath).convert()
    img.set_colorkey((200,0,200))

    #load sound
    wavPath = os.path.join("art","sound","test.wav")
    wav = pygame.mixer.Sound(wavPath)
       
    #create test enemy
    tom = Enemy(200, 200, img, wav)
    
    #create processors
    pro_painter = Processor_Painter(DISPLAYSURF)
    pro_audio = Processor_Sound()
    pro_move = Processor_Move()
    pro_text = Processor_Text(DISPLAYSURF, pygame.font.Font('freesansbold.ttf', 16))
    pro_ai = Processor_Artificial()

    while True:

        # MAINLOOP
        pro_painter.process(tom)
        #pro_audio.process(tom)
        pro_ai.process(tom)
        pro_move.process(tom)
        pro_text.process(tom)
        
        # MAINLOOP END
              
        # event handling loop
        pygame.event.pump()
        for event in pygame.event.get(): 
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                print('Exit Game')
                pygame.quit()
                sys.exit()

        #Redraw the screen and wait a clock tick.
        pygame.display.update()
        pygame.time.wait(1)
        frames +=1
        FPSCLOCK.tick(FPS)

        #Deltat = the amount of time wich has passed since last delta.Clock.tick() call:
        DELTAT = DeltaClock.tick()

if __name__ == '__main__':
    main()
