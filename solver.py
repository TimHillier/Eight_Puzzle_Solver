#solver for the puzzle
heuristics = ["manDistance","tOOP","custom"] #the heuristcs for best first search


#runs all solvers
def all(puzzle):
    breadthFirst(puzzle)
    aStar(puzzle)
    for x in heuristics:
        bestFirst(puzzle,x)

def breadthFirst(puzzle):
    print(puzzle)

def bestFirst(puzzle,heur):
    print(puzzle,heur)


def aStar(puzzle):
    print(puzzle)

def move(position,direction):
    print(position,direction)

def moveUp(position):
    swap(position,)
    print("MoveUp")

def moveDown(position):
    print("Move Down")

def moveRight(position):
    print("Move Right")

def moveLeft(position):
    print("Move Left")

#swap Position of two elements
def swap(posA,posB):
    return posB,posA
