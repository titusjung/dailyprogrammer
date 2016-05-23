import os
class Node:
    def __init__(self):
        degrees =0
        edges = {}
        
def main():
    os.path.dirname(os.path.realpath(__file__))
    print(os.getcwd())
    file = open("nodedegress/input.txt")
    nNodes = int(file.readline())
    degreeCount = [0] *nNodes
    print("Number of nodes: ",nNodes)
    for line in file:
        split = line.split()
        x1 = int(split[0])
        x2 = int(split[1])
        degreeCount[x1-1]+=1
        degreeCount[x2-1]+=1
    i=1
    for degree in degreeCount:
        print("Node ",i," has ",degree, " degrees ")
        i+=1
        
    


if __name__ == "__main__":
    main()