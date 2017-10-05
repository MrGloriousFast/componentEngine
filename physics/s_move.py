class SMove(): 
    def step(self,man, deltaT = 1.0):    

        #get all needed entities that have a body and a move component
        e_list = man.get_all_type(['body', 'move'])

        #for all entities get the correct components
        for e_id in e_list: 
            body = man.get(e_id,'body')
            move = man.get(e_id,'move')
    
            #do something with them
            body.pos[0] += move.x *deltaT
            body.pos[1] += move.y *deltaT

