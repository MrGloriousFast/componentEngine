"""
components are little data packets or structs.
Each entity is a collection of components and can have more than one

konvention:
Component classes start with a C

"""

class CBase:
    """
    may need to give components id numbers later on.
    This class is a base class for each component so
    we can add those kind of stuff later on
    """
    typ = 'baseComponent'

class CQuad(CBase):
    typ = 'quad'
    #basically two triangles making one quad
    def __init__(self):
        self.verticies = [
              -0.5, -0.5 ,  0.0,
               0.5, -0.5 ,  0.0,
               0.5,  0.5 ,  0.0,
               
               0.5,  0.5 ,  0.0,
              -0.5,  0.5 ,  0.0,
              -0.5, -0.5 ,  0.0]
               
        self.texcords =[  
              0.0,  0.0,
              1.0,  0.0,
              1.0,  1.0,
              
              1.0,  1.0,
              0.0,  1.0,
              0.0,  0.0]
        
        i = [0,1,2,
             2,3,0]

class CImage(CBase):
    typ = 'image'
    def __init__(self, png):
        self.image = png
        
class CBody(CBase):
    typ = 'body'
    def __init__(self, x, y):
        self.pos = [x,y,0]
        self.rot  = 0.0 #in pi
        self.scale= 1.0 
        self.radius = 10 #in pixel

class CSound(CBase):
    typ = 'sound'
    def __init__(self, wav):
        self.wav = wav
        
class CTeam(CBase):
    typ = 'team'
    def __init__(self):
        self.team = 'player1'   
        
class CMove(CBase):
    typ = 'move'
    def __init__(self, x,y):
        self.x = float(x)
        self.y = float(y)
        self.max = 10
        
        
class CText(CBase):
    typ = 'text'
    def __init__(self, text):
        self.text = text
        self.color = (100,100,100)
        self.size = 16
    
    
