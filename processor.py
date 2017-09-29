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
        
    def process(self, entity, entities):
        #get components we need        
        comp_npc = entity.get('npc')
        comp_posi = entity.get('position')
        comp_move = entity.get('speed')
        #do something with it
        counter = 0
        for e in entities:
            e_npc = e.get('npc')
            e_posi = e.get('position')
            e_move = e.get('speed')

            x1=comp_posi.posx
            y1=comp_posi.posy
            x2=e_posi.posx
            y2=e_posi.posy


            dis = self.distance(x1,y1, x2,y2)
            
            if dis < 500:
                #walk towards other entity
                y=y1-y2
                x=x1-x2
                
                comp_move.speedx -= x/10000.0 
                comp_move.speedy -= y/10000.0 
              
        #limit
        if(comp_posi.posx<0):
            comp_posi.posx=0
        if(comp_posi.posx>1000):
            comp_posi.posx-=1000
        if(comp_posi.posy<0):
            comp_posi.posy=0
        if(comp_posi.posy>1000):
            comp_posi.posy-=1000

    #returns the distance between two points
    #recives two tupel
    def distance(self, x1,y1,x2,y2 ):
        y=y1-y2
        x=x1-x2
        distance = (x**2 + y**2)**0.5
        return distance
        
class Processor_Follow(Processor_Base):
    #a follows b
    def process(self,entityA, entityB):
        #get components we need        
        a_posi = entityA.get('position')
        a_move = entityA.get('speed')
        b_posi = entityB.get('position')
        b_move = entityB.get('speed')

        #do something with it


        x1=a_posi.posx
        y1=a_posi.posy
        x2=b_posi.posx
        y2=b_posi.posy


        dis = self.distance(x1,y1, x2,y2)
            

        #walk towards other entity
        y=y1-y2
        x=x1-x2
            
        a_move.speedx -= x/(100*dis) 
        a_move.speedy -= y/(100*dis) 
           
    #returns the distance between two points
    #recives two tupel
    def distance(self, x1,y1,x2,y2 ):
        y=y1-y2
        x=x1-x2
        distance = (x**2 + y**2)**0.5
        return distance
        


class Processor_Sound(Processor_Base):
            
    def process(self, entity):
        comp_sound = entity.get('sound')
        comp_sound.wav.play()
        
class Processor_HumanControl(Processor_Base):
    def process(self,entity, dirx, diry):
        speed = entity.get('speed')        
        posi = entity.get('position')
        
        speed.speedx += dirx
        speed.speedy += diry
        
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



