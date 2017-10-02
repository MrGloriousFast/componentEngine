class Component_Base:
   def __init__(self):
        self.type = 'baseComponent'
        
class Component_Image(Component_Base):
    type = 'image'
    def __init__(self, png):
        self.image = png
        
class Component_Position(Component_Base):
    def __init__(self, x, y):
        self.type = 'position'
        self.posx = x
        self.posy = y
        self.posz = 0

class Component_Sound(Component_Base):
    def __init__(self, wav):
        self.type = 'sound'
        self.wav = wav
        
class Component_Body(Component_Base):
    def __init__(self, radius):
        self.type = 'radius'
        self.radius = radius

class Component_Player(Component_Base):
   def __init__(self):
        self.type = 'player1'
        
class Component_Npc(Component_Base):
   def __init__(self):
        self.type = 'npc'   

class Component_Speed(Component_Base):
    def __init__(self, speedx, speedy):
        self.type = 'speed'
        self.speedx = float(speedx)
        self.speedy = float(speedy)
        
class Component_Text(Component_Base):
    def __init__(self, text):
        self.type = 'text'
        self.text = text
        self.color = (100,100,100)
        self.size = 16
    
    
