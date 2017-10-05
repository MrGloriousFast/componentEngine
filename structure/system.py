


class SystemBase:
    def __init__(self):
        #init stuff you need here
        pass

    #insertion of data that will be automatically be used in step
    def insert(self,e_1,c_1):
        pass

    #insertion of data that will have to be inserted before each step
    def stream(self,e_1,c_1):
        e_1 #just a step to get components
        pass
        
    #one step of calculation
    #will have side effects
    #might return something
    def step(self,dt):        
        pass
        
    #stream to chain system together into pipes
    #might overlap with return from step
    def out():
        pass
        
