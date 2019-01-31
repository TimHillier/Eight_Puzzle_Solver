#moves the puzzle,creating children of the parent
import treeGen
from anytree import Node
states = set()
def mover(puzzle,parent,checker):
    global states
    #some checks
    if isinstance(puzzle,Node):
        puzzle = puzzle.name

    if not isinstance(puzzle,list):
        if isinstance(puzzle,Node):
            puzzle = puzzle.name

        puzzle = list(puzzle.split()[0])

    if len(states) > 0:
        states = set()

    #lets get the index of the zero
    zeroLocation = getZero(puzzle)

    #move the zero
    moveLeft(puzzle[:],zeroLocation)
    moveRight(puzzle[:],zeroLocation)
    moveUp(puzzle[:],zeroLocation)
    moveDown(puzzle[:],zeroLocation)
    # print(states)

    if not checker:
        #only use in bread
        for x in states:
            treeGen.addNode(x[:9],parent,x[-1:])

    elif checker:
        #should only go in here in best first
        for x in states:
            treeGen.addNodeBest(x[:9],parent,x[-1:])

    return parent

def getZero(puzzle):
    return puzzle.index('0')


def moveLeft(puzzle,zeroLocation):
    if not zeroLocation % 3 == 0:
        puzzle[zeroLocation],puzzle[zeroLocation -1] = puzzle[zeroLocation-1],puzzle[zeroLocation]
        states.add(''.join(puzzle)+"L")
def moveRight(puzzle,zeroLocation):
    if not zeroLocation % 3 == 2:
        puzzle[zeroLocation],puzzle[zeroLocation +1] = puzzle[zeroLocation+1],puzzle[zeroLocation]
        states.add(''.join(puzzle)+"R")
def moveUp(puzzle,zeroLocation):
    if not zeroLocation < 3:
        puzzle[zeroLocation],puzzle[zeroLocation -3] = puzzle[zeroLocation-3],puzzle[zeroLocation]
        states.add(''.join(puzzle)+"U")
def moveDown(puzzle,zeroLocation):
    if not zeroLocation >= 6:
        puzzle[zeroLocation],puzzle[zeroLocation +3] = puzzle[zeroLocation+3],puzzle[zeroLocation]
        states.add(''.join(puzzle)+"D")
