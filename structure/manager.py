"""
This class will keep track of all components and entity ids.
"""

class Manager():
    """
    E_ID -> entity id
    C_T -> component type / or id
    C -> component

    """  
    def __init__(self):
        
        
        #dict{ E_ID : dict{C_T : C}}    
            #E_ID , C_T -> C
        self.e_id = {}        
        self.e_id[0] = {}
        
        #groups
        #dict{groupname:set{E_ID}}
        self.groups = {}
        self.groups[0]=set()
        
        #sometimes we need all entities that have C1,C5,C6
        #dict{C_T : E_ID}
            #C_T -> E_1, E_2, E_n
        self.c_id = {}
        self.c_id[0] = set()
    
    
        #the same as above. we want all components of type body for collision for example.
        self.component_typ = {}
        self.component_typ[0] = set()
    
    """
    component entity relationships
    """
    #creates Emtity E if not already created and gives it a component C of type C_T
    def add(self, E_ID, C_T, C):
        #print(C)

        #first check if we need to make new ones

        #add the E_ID to the component sorted dict
        if(C_T not in self.c_id):
            self.c_id[C_T] = set()
        self.c_id[C_T].add(E_ID)

        if(E_ID not in self.e_id):
            self.e_id[E_ID] = {}
        self.e_id[E_ID][C_T] = C

        if(C_T not in self.component_typ):
            self.component_typ[C_T] = set()
        self.component_typ[C_T].add(C)
        


    #returns the component that is of type C_T and is owned by E_ID
    def get(self, E_ID, C_T):
        return self.e_id[E_ID][C_T]
        
    """
    def get_all(self, E_ID, list_C_T):
        result = []
        for t in list_C_T:
            result.append(self.e_id[E_ID][t])
        return result
    """
        
    #returns all components that have this component type
    def get_all_type(self, C_T):
        return self.c_id[C_T]

    #returns entities that have all component types in the types list
    def get_all_type_list(self, types):
        if types[0] in self.c_id:
            result =  self.c_id[types[0]]
            for typ in types:
                result = result.intersection(self.c_id[typ])
            return result
        else:
            return {}

    """
    component typ relations
    """
    #returns all components of a type
    def get_all_components(self, typ):
        if typ in self.component_typ:
            return self.component_typ[typ]
        else:
            return {}

    """
    group membership
    """
    #create a new group
    def group_create(self, tag, e_list):
        self.groups[tag] = set(e_list)

    #add to the group
    def group_add(self, tag, e_list):
        if(tag not in self.groups):
            self.groups[tag] = set(e_list) 
        self.groups[tag].add(e_list)

    #get the group
    def group_get(self, tag):
        if tag in self.groups:
            return self.groups[tag]
        else:
            return set()    
        
        
        
        
        
        
        
        
        
        
