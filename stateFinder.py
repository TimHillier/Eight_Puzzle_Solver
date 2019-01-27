import numpy

def findNext(puzzle):
    nextStates = []
    Z = findZero(puzzle)



#this finds the zero in a 2d list
def findZero(puzzle):
    index = numpy.where(puzzle == '0')
    return index



#swamps elements of the puzzle
def moveUp(puzzle,zero):
    puzzle[zero[0], zero[1]], puzzle[zero[0]-1, zero[1]] = puzzle[zero[0]-1, zero[1]], puzzle[zero[0], zero[1]]

def moveleft(puzzle,zero):
    puzzle[zero[0], zero[1]], puzzle[zero[0], zero[1]-1] = puzzle[zero[0], zero[1]-1], puzzle[zero[0], zero[1]]

def movedown(puzzle,zero):
    puzzle[zero[0], zero[1]], puzzle[zero[0]+1, zero[1]] = puzzle[zero[0]+1, zero[1]], puzzle[zero[0], zero[1]]

def moveright(puzzle,zero):
    puzzle[zero[0], zero[1]], puzzle[zero[0], zero[1]+1] = puzzle[zero[0], zero[1]+1], puzzle[zero[0], zero[1]]
