class SHuman():
    def __init__(self, e_id, speed = 1.0):
        self.e_id = e_id
        self.speed = speed

    def step(self, man, dirx, diry):
        man.get(self.e_id, 'move').x = self.speed*dirx
        man.get(self.e_id, 'move').y = self.speed*diry
    
