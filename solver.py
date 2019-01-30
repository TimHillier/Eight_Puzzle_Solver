import treeGen,stateFinder
from queue import *
#solver for the puzzle
heuristics = ["manDistance","tOOP","custom"] #the heuristcs for best first search


#runs all solvers
def all(puzzle,parent):
    thisTree = stateFinder.mover(puzzle, parent)
    breadthFirst(thisTree, treeGen.getRoot())
    # aStar(thisTree)
    # for x in heuristics:
    #     bestFirst(thisTree,x)

def breadthFirst(puzzle,source):
    q = Queue(maxsize=0)
    visited = [] # visited
    visited.append(source)
    q.put(source)
    while not q.empty():
        v = q.get()

        # i nee

    

    print("root: ",source)
    print(puzzle)

def bestFirst(puzzle,heur):
    print(puzzle,heur)


def aStar(puzzle):
    print(puzzle)


def generateChildren():
    print("Ah")

