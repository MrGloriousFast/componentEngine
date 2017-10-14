import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *


class SScreen():
    def __init__(self, width, height, title = "TITLE", clearColor = (0.0, 0.0, 0.05, 0.0)):
        pygame.display.init()
        pygame.display.set_caption(title)

        self.w = width
        self.h = height

        pygame.display.set_mode((self.w,self.h), DOUBLEBUF|OPENGL|FULLSCREEN)
        
        glEnable(GL_DEPTH_TEST) #unfuck 3d surfaces, might make it slower
        glClearColor(*clearColor)# that star just unpacks a tuple
        
    def clear(self):    
        #make the screen blank
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
    def step(self):
        #flip the buffer
        #show us all new rendered images
        pygame.display.flip()
        #clear the drawing board for new drawings
        self.clear()       

        
    def polygonMode(self, mode):
        if mode == 'line':
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        if mode == 'point':
            glPolygonMode(GL_FRONT_AND_BACK, GL_POINT)
        if mode == 'fill':
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)    
            
