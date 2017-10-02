

def load(path):

    verticies = []
    indicies = []
    normals = []

    with open(path) as f:
        for line in f:
            if len(line)<4:continue
            c = line.split() 
                        
            if c[0] == 'vn':
                normals.append([ float(c[1]), float(c[2]), float(c[3]) ])
            if c[0] == 'v':
                verticies.append([float(c[1]), float(c[2]), float(c[3])])
            if c[0] == 'f':
                print( [int(c[1].split("//")[0]) , int(c[1].split("//")[1]),
                        int(c[2].split("//")[0]) , int(c[2].split("//")[1]),
                        int(c[3].split("//")[0]) , int(c[3].split("//")[1])])
#                indicies.append([int(c[1]), int(c[2]), int(c[3])])

    print("verticies")
    for i in verticies:
        print(i)
        
    print("normals")
    for i in normals:
        print(i)
        

    print("indicies")
    for i in indicies:
        print(i)
        


    return [verticies, normals, indicies]
