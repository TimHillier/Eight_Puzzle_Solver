#moves the puzzle,creating children of the parent
import treeGen
states = set()
def mover(puzzle,parent):
    global states
    #lets get the index of the zero
    if not isinstance(puzzle,list):
        puzzle = puzzle.split()
    if len(states) > 0:
        states = set()
    zeroLocation = getZero(puzzle)
    #move the zero
    moveLeft(puzzle[:],zeroLocation) #this should pass it a new list, that is a copy of the old list
    moveRight(puzzle[:],zeroLocation)
    moveUp(puzzle[:],zeroLocation)
    moveDown(puzzle[:],zeroLocation)
    print(states)

    for x in states:
        treeGen.addNode(x,parent)

def getZero(puzzle):
    return puzzle.index('0')


def moveLeft(puzzle,zeroLocation):
    if not zeroLocation % 3 == 0:
        puzzle[zeroLocation],puzzle[zeroLocation -1] = puzzle[zeroLocation-1],puzzle[zeroLocation]
        states.add(''.join(puzzle))
def moveRight(puzzle,zeroLocation):
    if not zeroLocation % 3 == 2:
        puzzle[zeroLocation],puzzle[zeroLocation +1] = puzzle[zeroLocation+1],puzzle[zeroLocation]
        states.add(''.join(puzzle))
def moveUp(puzzle,zeroLocation):
    if not zeroLocation < 3:
        puzzle[zeroLocation],puzzle[zeroLocation -3] = puzzle[zeroLocation-3],puzzle[zeroLocation]
        states.add(''.join(puzzle))
def moveDown(puzzle,zeroLocation):
    if not zeroLocation >= 6:
        puzzle[zeroLocation],puzzle[zeroLocation +3] = puzzle[zeroLocation+3],puzzle[zeroLocation]
        states.add(''.join(puzzle))
