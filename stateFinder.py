#moves the puzzle,creating children of the parent
def mover(puzzle):
    states = set()
    #lets get the index of the zero
    zeroLocation = getZero(puzzle)
    # print(zeroLocation)
    # print(zeroLocation%3)
    # print(puzzle)
    moveLeft(puzzle[:],zeroLocation) #this should pass it a new list, that is a copy of the old list
    # print(puzzle)
    moveRight(puzzle[:],zeroLocation)
    # print(puzzle)
    moveUp(puzzle[:],zeroLocation)
    # print(puzzle)
    moveDown(puzzle[:],zeroLocation)
    # print(puzzle)

def getZero(puzzle):
    return puzzle.index('0')


def moveLeft(puzzle,zeroLocation):
    if not zeroLocation % 3 == 0:
        puzzle[zeroLocation],puzzle[zeroLocation -1] = puzzle[zeroLocation-1],puzzle[zeroLocation]
    print("mL:",puzzle)
def moveRight(puzzle,zeroLocation):
    if not zeroLocation % 3 == 2:
        puzzle[zeroLocation],puzzle[zeroLocation +1] = puzzle[zeroLocation+1],puzzle[zeroLocation]
    print("mR:",puzzle)
def moveUp(puzzle,zeroLocation):
    if not zeroLocation < 3:
        puzzle[zeroLocation],puzzle[zeroLocation -3] = puzzle[zeroLocation-3],puzzle[zeroLocation]
    print("mU:",puzzle)
def moveDown(puzzle,zeroLocation):
    if not zeroLocation >= 6:
        puzzle[zeroLocation],puzzle[zeroLocation +3] = puzzle[zeroLocation+3],puzzle[zeroLocation]
    print("mD:",puzzle)
