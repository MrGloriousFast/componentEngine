from pygame.locals import *

class Processor_Base:
    def __init__(self):
        self.test = 0
        
    def process(self, component):
        print("processing...")   
    
class Processor_Painter(Processor_Base):

    def __init__(self, surface):
        self.display = surface
    
    def process(self, comp_image, posi):
        self.drawImage(comp_image.image, posi.posx,posi.posy)
        
    def drawImage(self, image , xx ,yy):
        (xsize, ysize) = image.get_size()
        self.display.blit(image, (int(xx-xsize/2),int(yy-ysize/2)))

class Processor_Sound(Processor_Base):
            
    def process(self, comp_sound):
        comp_sound.wav.play()
        
class Processor_Move(Processor_Base):
    def process(self,comp_posi, comp_speed):
        comp_posi.posx += comp_speed.speedx
        comp_posi.posy += comp_speed.speedy
