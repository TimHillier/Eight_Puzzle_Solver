import numpy

states = set()  # should hold the states we have been to so far?


def findNext(puzzle, tree):
    global states
    #reset states on new puzzle
    if(len(states) != 0):
        states = set()
    addToStates(puzzle)
    print("states",states)
    nextStates = []
    Z = findZero(puzzle)
    move(puzzle, Z)

    return tree


# this finds the zero in a 2d list
def findZero(puzzle):
    index = numpy.where(puzzle == '0')
    return index

#i hate this, why cant i find a nice way to do this.  ugh.
def move(puzzle, zero):
    newPuzzle = puzzle
    if (numpy.fromstring(zero[1].tostring(), dtype=int) == 0):
        # at this point, the zero can move [right,down,up]
        if (numpy.fromstring(zero[0].tostring(), dtype=int) == 0):
            print("Stupid")
            # if its [0,0] it needs to move right and down
        if (numpy.fromstring(zero[0].tostring(), dtype=int) == 1):
            print("Stupid")
            # if it is [1,0] it needs to move up, right, and down
        if (numpy.fromstring(zero[0].tostring(), dtype=int) == 2):
            print("Stupid")
            # if it is [2,0] it needs to move up and right

    if (numpy.fromstring(zero[1].tostring(), dtype=int) == 1):
        # at this point, the zero can move [right,left,up,down]
        if (numpy.fromstring(zero[0].tostring(), dtype=int) == 0):
            # if its [0,1] it needs to move left, down and right
            print("Stupid")
        if (numpy.fromstring(zero[0].tostring(), dtype=int) == 1):
            # if it is [1,1] it needs to move left, down, up, right
            print("Stupid")
        if (numpy.fromstring(zero[0].tostring(), dtype=int) == 2):
            # if it is [2,1] it needs to move left,right,up
            print("Stupid")

    if (numpy.fromstring(zero[1].tostring(), dtype=int) == 2):
        # at this point, the zero can move [left,down,up]
        if (numpy.fromstring(zero[0].tostring(), dtype=int) == 0):
            print("Stupid")
            # if it is [0,2] it can move left and down
        if (numpy.fromstring(zero[0].tostring(), dtype=int) == 1):
            print("Stupid")
            # if it is [1,2] it can move up, left, and down
        if (numpy.fromstring(zero[0].tostring(), dtype=int) == 2):
            print("Stupid")
            # if it is [2,2] it can move up and left


# swamps elements of the puzzle
def moveUp(puzzle, zero):
    puzzle[zero[0], zero[1]], puzzle[zero[0] - 1, zero[1]] = puzzle[zero[0] - 1, zero[1]], puzzle[zero[0], zero[1]]


def moveleft(puzzle, zero):
    puzzle[zero[0], zero[1]], puzzle[zero[0], zero[1] - 1] = puzzle[zero[0], zero[1] - 1], puzzle[zero[0], zero[1]]


def movedown(puzzle, zero):
    puzzle[zero[0], zero[1]], puzzle[zero[0] + 1, zero[1]] = puzzle[zero[0] + 1, zero[1]], puzzle[zero[0], zero[1]]


def moveright(puzzle, zero):
    puzzle[zero[0], zero[1]], puzzle[zero[0], zero[1] + 1] = puzzle[zero[0], zero[1] + 1], puzzle[zero[0], zero[1]]


def addToStates(currentState):
    states.add(numpy.array2string(currentState))