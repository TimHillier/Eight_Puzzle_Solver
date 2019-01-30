import treeGen,numpy,stateFinder
#solver for the puzzle
heuristics = ["manDistance","tOOP","custom"] #the heuristcs for best first search


#runs all solvers
def all(puzzle):
    # print(puzzle)
    thisTree = treeGen.generateTree(puzzle) #init the tree
    thisTree = stateFinder.findNext(puzzle,thisTree) #complete the tree
    # breadthFirst(thisTree)
    # aStar(thisTree)
    # for x in heuristics:
    #     bestFirst(thisTree,x)

def breadthFirst(puzzle):
    print(puzzle)

def bestFirst(puzzle,heur):
    print(puzzle,heur)


def aStar(puzzle):
    print(puzzle)






#swap Position of two elements
def swap(posA,posB):
    return posB,posA
