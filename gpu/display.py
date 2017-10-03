import pygame, time, select
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *

def getTime():
    #print(time.clock(),time.perf_counter()) #4.70512 , 8074.099998122
    #return time.clock() #71
    #return time.process_time() #72
    return  time.perf_counter() #83
    #return time.time()#82

class Display():
    def __init__(self, width, height, title = "TITLE", fps = 30, clearColor = (0.0, 0.0, 0.05, 0.0)):
        pygame.display.init()
        pygame.display.set_caption(title)

        self.w = width
        self.h = height

        self.fps = fps
        self.deltaT = float(1000./fps)#just a good guess for the first loop

        self.frameTime = float(1./fps) #that much time for one frame in s
        print(self.frameTime,' seconds for one frame')
        self.frameCount = 0
        self.frameCountOld = 0
        self.frameCountTimer = 0


        screen = pygame.display.set_mode((self.w,self.h), DOUBLEBUF|OPENGL)
        
        glEnable(GL_DEPTH_TEST) #unfuck 3d surfaces, might make it slower
        glClearColor(*clearColor)# that star just unpacks a tuple
        
        self.start_time = -1
        self.end_time = 0
       
       
    def begin_frame(self):
        self.start_time = self.end_time
        if(self.start_time == -1):
            self.start_time = getTime()
        self.clear()
    
    def finish_frame(self):
        self.end_time = getTime()
        self.deltaT = self.end_time - self.start_time       

        if(self.deltaT < self.frameTime):
            
            delay = ( self.frameTime- self.deltaT)    
            #print(self.deltaT, self.frameTime, delay)
            time.sleep(delay)
    
        self.end_time = getTime()


       
    def clear(self):    
        #make the screen blank
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        self.getActualFps() 
        
    def flip(self):
 
        self.frameCount +=1
        pygame.display.flip()
       
    def getActualFps(self):

        if (getTime() > 1+self.frameCountTimer):
            #update timer
            delta = getTime() - self.frameCountTimer
            self.frameCountTimer = getTime()
            #
            print("fps: ", str((self.frameCount - self.frameCountOld)/delta)[0:3],"deltaT:" ,str(self.deltaT*1000)[0:5], "ms")
            self.frameCountOld = self.frameCount

        
    def polygonMode(self, mode):
        if mode == 'line':
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        if mode == 'point':
            glPolygonMode(GL_FRONT_AND_BACK, GL_POINT)
        if mode == 'fill':
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)    
            
