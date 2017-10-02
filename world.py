class World:

    def __init__(self):
        self.chunks = []
        for i in range(0,3):
            self.chunks.append(Chunk())
        
    
        
        
class Chunk:
    def __init__(self):
        self.size = 32
        self.w = 3
        self.h = 3
        self.entities = []
        self.genLevel()
        
        
    def genLevel(self):
        #init level with 0
        self.level = [[0 for x in range(self.w)] for y in range(self.h)] 
