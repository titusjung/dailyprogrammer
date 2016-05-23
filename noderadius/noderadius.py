import os
import math 
 
def main():
    os.path.dirname(os.path.realpath(__file__))
    print(os.getcwd())
    file = open("noderadius/input.txt")
    nNodes = int(file.readline())
    degreeCount = [0] *nNodes
    print("Number of nodes: ",nNodes)
    matrix = [[math.inf for x in range(nNodes)]for y in range(nNodes)]
    for i in range(nNodes):
        matrix[i][i] = 0
    for line in file:
        split = line.split()
        x1 = int(split[0])-1
        x2 = int(split[1])-1
        #nodeList[x1-1].AddEdge(nodeList[x2-1])
        #nodeList[x2-1].AddEdge(nodeList[x1-1])
        matrix[x1][x2] = 1
        matrix[x2][x1] = 1
        degreeCount[x1]+=1
        degreeCount[x2]+=1
    #print([i for i in range(0,nNodes)])
    i=0
    for x in matrix:
        #print(" ",x)
        i+=1
    i=1
    diameter =0
    radius = math.inf
    for k in range(0,nNodes):
        for i in range(0,nNodes):
            for j in range(0,nNodes):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    radius = math.inf
    diameter = 0
    for x in matrix:
        ecc = 0
        for y in x:
           if y>ecc and not math.isinf(y):
                ecc = y
        if radius>ecc and ecc is not 0: 
            radius = ecc
        if diameter<ecc:
            diameter = ecc
    print(" ")
    #for x in matrix:
       # print(" ",x)
        #i+=1
    #for degree in degreeCount:
        #print("Node ",i," has ",degree, " degrees ")
        #i+=1
    print("radius is ",radius)
    print("diamter is ",diameter)
    


if __name__ == "__main__":
    main()