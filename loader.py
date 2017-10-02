import os
import pygame

class Data:

    _colorkey = (200,0,200)
       
    def __init__(self):
        self.img = {}
        self.audio = {}
    
    #input a name. example: 'dino'
    #and a path as a list ['c','documents','user','image.png']
    def load(self, name, path):
    
        path = os.path.join(*path)
        pic = pygame.image.load(path).convert()
        pic.set_colorkey(self._colorkey)
        self.img[name] = pic
        
    def load_all_images(self):
        self.load('player2', ["art","graphic","test.png"])
        self.load('player' , ["art","graphic","test2.png"])
        self.load('enemy'  , ["art","graphic","TerrAk47.png"])
         
