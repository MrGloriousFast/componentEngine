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
        
class Processor_Text(Processor_Base):

    def __init__(self, surface, fontObj):
        self.display = surface
        self.fontObj = fontObj #pygame.font.Font('freesansbold.ttf', 16)

    def process(self, comp_text, comp_posi):
        color = comp_text.color
        if (comp_text.size != 16):
            fontObj2 = pygame.font.Font('freesansbold.ttf', size)#very slow!
            textSurfaceObj = fontObj2.render(text, False, color)
        else:
            textSurfaceObj = self.fontObj.render(comp_text.text, False, color)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (comp_posi.posx,comp_posi.posy)
        self.display.blit(textSurfaceObj, textRectObj)        



