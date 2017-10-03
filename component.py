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

class CImage(CBase):
    typ = 'image'
    def __init__(self, png):
        self.image = png
        
class CBody(CBase):
    typ = 'body'
    def __init__(self, x, y, s=1.0):
        self.pos = [x,y,0]
        self.rot  = 0.0 #in pi
        self.scale= s 
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
    
    
