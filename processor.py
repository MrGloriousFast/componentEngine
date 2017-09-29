from pygame.locals import *






class Processor_Base:
    def __init__(self):
        self.test = 0
        
    def process(self, component):
        print("processing...")   
    
class Processor_Painter(Processor_Base):

    def __init__(self, surface):
        self.display = surface
    
    def process(self, entity):
        #extract components we need from the entity
        comp_image= entity.get('image')
        posi = entity.get('position')
        
        #use the data
        self.drawImage(comp_image.image, posi.posx,posi.posy)
        
   #helper function
    def drawImage(self, image , xx ,yy):
        (xsize, ysize) = image.get_size()
        self.display.blit(image, (int(xx-xsize/2),int(yy-ysize/2)))

class Processor_Artificial(Processor_Base):

    def __init__(self):
        self.intelligent = True
        
    def process(self, entity):
        #get components we need        
        comp_npc = entity.get('npc')
        comp_posi = entity.get('position')
        comp_move = entity.get('move')
        #do something with it
        self.input(comp_npc, comp_posi, comp_move)
        
    #basic ai input
    #with side effects (may want to define output seperatly instead of having side effects directly)
    def input(self, comp_npc, comp_posi, comp_move):
        #just jump around
        if(comp_posi.posx >400):
            comp_posi.posx = 100
        if(comp_posi.posy >400):
            comp_posi.posy = 100

class Processor_Sound(Processor_Base):
            
    def process(self, entity):
        comp_sound = entity.get('sound')
        comp_sound.wav.play()
        
class Processor_Move(Processor_Base):
    def process(self,entity):
        #get components we need
        comp_posi = entity.get('position')
        comp_speed = entity.get('speed')
        #do something with them
        comp_posi.posx += comp_speed.speedx
        comp_posi.posy += comp_speed.speedy
        
class Processor_Text(Processor_Base):

    def __init__(self, surface, fontObj):
        self.display = surface
        self.fontObj = fontObj #pygame.font.Font('freesansbold.ttf', 16)

    def process(self, entity):
    
        #get components we need
        comp_text = entity.get('text')
        comp_posi = entity.get('position')

        #process them and change them
        color = comp_text.color
        if (comp_text.size != 16):
            fontObj2 = pygame.font.Font('freesansbold.ttf', size)#very slow!
            textSurfaceObj = fontObj2.render(text, False, color)
        else:
            textSurfaceObj = self.fontObj.render(comp_text.text, False, color)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (comp_posi.posx,comp_posi.posy)
        self.display.blit(textSurfaceObj, textRectObj)        



