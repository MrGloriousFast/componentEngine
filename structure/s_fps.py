import  time, select

def getTime():
    #print(time.clock(),time.perf_counter()) #4.70512 , 8074.099998122
    #return time.clock() #71
    #return time.process_time() #72
    return  time.perf_counter() #83
    #return time.time()#82


class SFps():
    def __init__(self, fps = 30):

        self.fps = fps
        self.deltaT = float(1000./fps)#just a good guess for the first loop

        self.frameTime = float(1./fps) #that much time for one frame in s
        #print(self.frameTime,' seconds for one frame')
        
        self.frameCount = 0
        self.frameCountOld = 0
        self.frameCountTimer = 0

        self.start_time = -1
        self.end_time = 0

    def _getActualFps(self):
        interval = 1 #seconds
        if (getTime() > interval+self.frameCountTimer):
            #update timer
            delta = getTime() - self.frameCountTimer
            self.frameCountTimer = getTime()
            #
            #print("fps: ", str((self.frameCount - self.frameCountOld)/delta)[0:3],"deltaT:" ,str(self.deltaT*1000)[0:5], "ms")
            self.frameCountOld = self.frameCount

    def step(self):
        #count one frame    
        self.frameCount +=1
        #calculate the frames per second
        self._getActualFps()
        
        #wait additional time if we are faster than the framelimit
        temp = getTime()
        self.deltaT = temp - self.start_time
        if(self.deltaT < self.frameTime):
            delay = ( self.frameTime- self.deltaT)    
            time.sleep(delay)
    
        #save the endtime of the frame
        self.end_time = getTime()
    
        #begin counting for a new frame
        self.start_time = self.end_time
        if(self.start_time == -1):
            self.start_time = getTime()
    
        #return the elapsed time in the last frame
        return self.deltaT
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
