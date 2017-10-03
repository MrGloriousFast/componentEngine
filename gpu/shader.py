from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *
import numpy, pyrr, os


class AShader():
    def __init__(self, name):
        
        path_v = os.path.join('gpu','shaders', str(name) +'.vert')
        path_f = os.path.join('gpu','shaders', str(name) +'.frag')
        
        self.program = glCreateProgram()
        self.s = []
        self.s.append(self.createShader(self.read(path_v), GL_VERTEX_SHADER))
        self.s.append(self.createShader(self.read(path_f), GL_FRAGMENT_SHADER))
    
        for shad in self.s:
            glAttachShader(self.program, shad)
    
        self.shader = OpenGL.GL.shaders.compileProgram(self.s[0], self.s[1])
    
        glBindAttribLocation(self.program, 0, "inposition")
        glBindAttribLocation(self.program, 1, "intexcord")
        glBindAttribLocation(self.program, 2, "incord")
        glBindAttribLocation(self.program, 3, "scale")
        
        glLinkProgram(self.program)
        glValidateProgram(self.program)
    
    #openGl use this shader!
    def use(self):
        glUseProgram(self.program)
        
    #create a new shader
    def createShader(self, text, shaderType):
        shader = glCreateShader(shaderType)
        if(shader == 0):
            print("shader creation failed!")

        #compile shader
        shader = OpenGL.GL.shaders.compileShader(text,shaderType)
        return shader
        
    #just opens a shader file
    def read(self, path):
        return open(path,'r').readlines()
