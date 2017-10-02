from OpenGL.GL import *
from OpenGL.GLU import *
from texture import *
from shader import AShader
import numpy as np

def mat_to_array(mat):
    temp = []
    for i in mat:
        for j in i.get():
            temp.extend(j)
    return temp

class Instances:
    def __init__(self, verticies, texcords, shader, texture):
        #everyhting they share
        self.verticies = verticies
        self.texcords  = texcords
        self.shader    = shader
        self.texture   = texture

        #all world positions, empty in init
        self.inst_pos = []
        self.instances = 0
    
        #create all static buffers
        self.createBuffer()
        self.createBuffer_pos()

    #add another instance
    def append(self, pos):
        #needs the pos in a list [x,y,z]
        self.inst_pos.extend(pos)
        self.instances += 1
        #self.createBuffer_pos()
        #self.createBuffer_pos()

    def updateShader(self, cam):
        self.shader.use()
    
    """
    buffer for static data (everything that is the same for each instance)
    """
    def createBuffer(self):
            
        #create a buffer
        # we will use only one buffer for all static things that are the same for each instance
        self.buffer = glGenBuffers(1)

        #bind it, aka use it
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer)

        #sort the data
        interleaved = []
        for i in range(0,int(len(self.verticies)/3)):
            #all three vertex floats afet each other
            interleaved.append(self.verticies[i*3])
            interleaved.append(self.verticies[i*3+1])
            interleaved.append(self.verticies[i*3+2])
            #all two texture coords after each other
            interleaved.append(self.texcords[i*2])
            interleaved.append(self.texcords[i*2+1])
        
        
        
        
        
        #make this list so that openGl can read it
        inter = np.array(interleaved, dtype="float32")
        self.size = 4 #bytes  

        #print("inter.shape[0]", inter.shape[0])
        #print("divided by 4:", inter.shape[0]/8)
        #print('inter: ' + str(inter))

        #fill the buffer
        glBufferData(GL_ARRAY_BUFFER, self.size*inter.shape[0], inter, GL_STATIC_DRAW)

        #24 floats with 4 byte each
        #vec3 inposition      3
        #vec2 intexcord       2
        self.buffer_step = self.size*5

        glEnableVertexAttribArray(0) #inposition
        glEnableVertexAttribArray(1) #intexcords
        #glEnableVertexAttribArray(2) 

        #unbind it, i dont know why, just do it
        glBindBuffer(GL_ARRAY_BUFFER, 0)



    """
    buffer for changing data
    it can be bigger or smaller than the other buffer, depending on the number of instances.
    (positions for each is different)
    """
    def createBuffer_pos(self):
        
        #we will use another buffer for all data that changes often (aka world position)
        self.buffer_pos = glGenBuffers(1)

        #bind it, aka use it
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_pos)

        self.size = 4 #bytes aka 32bit per number
        #how much data is in one "step" or stride
        self.buffer_step_pos = self.size*3 #three positions data x y z

        #make this list so that openGl can read it
        #print('self.inst_pos ' + str(self.inst_pos))
        inter = np.array(self.inst_pos, dtype="float32")


        #fill the buffer
        glBufferData(GL_ARRAY_BUFFER, self.size*3, inter, GL_DYNAMIC_DRAW) 

        glEnableVertexAttribArray(2)#incord #coordinates we sed to the gpu on array 2

        #unbind it, i dont know why, just do it
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def bind(self):
        #make sure we use the correct shader and texture
        self.shader.use()
        self.texture.bind()

        """ STATIC MODEL """    
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer)

        #now we need to specify where to look into the buffer if you want one specific float:
        #vertex data
        offset = 0
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.buffer_step, ctypes.c_void_p(offset))
        #texture data
        offset = 3 * self.size
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.buffer_step, ctypes.c_void_p(offset))

        #tell open gl that we change these with each vertex loop (x,0)
        glVertexAttribDivisor(0,0) #inposition
        glVertexAttribDivisor(1,0) #intexcord

        """ POSITION """
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_pos)
        
        #set the pointer correctly
        #position of the instance
        offset = 0 
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.buffer_step_pos, ctypes.c_void_p(offset))

        #these the ones we want to change only once per instance (x,1)
        glVertexAttribDivisor(2,1) #incord
        
    def render(self):
    
        #use all correct pointer and shader etc
        self.bind()
        
        #draw ett!
        #mode = GL_TRIANGLES
        first = 0
        num_verticies = len(self.verticies)
        num_instances = self.instances
        
        #print(num_instances)
        
        #print('rendering :' + ' num_verticies '+str(num_verticies) +' num_instances '+ str(num_instances))
        glDrawArraysInstanced(GL_TRIANGLES, first, num_verticies, num_instances)
        
        #unbind it, i dont know why, just do it
        glBindBuffer(GL_ARRAY_BUFFER, 0)

        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
