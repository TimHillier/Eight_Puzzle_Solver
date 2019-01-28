import numpy

states = {} #should hold the states we have been to so far?


def findNext(puzzle,tree):
    nextStates = []
    Z = findZero(puzzle)
    move(puzzle,Z)

    return tree



#this finds the zero in a 2d list
def findZero(puzzle):
    index = numpy.where(puzzle == '0')
    return index


def move(startpuzzle,zero):
    puzzle = startpuzzle
    if(numpy.fromstring(zero[1].tostring(),dtype=int) == 0):
        #at this point, the zero can move [right,down,up]
        print("MOVEING")
        moveright(puzzle, zero)
    if(numpy.fromstring(zero[1].tostring(),dtype=int) == 1):
        #at this point, the zero can move [right,left,up,down]
        moveright(puzzle, zero)
        print(puzzle)
        # moveleft(puzzle, zero)
        # print(puzzle)
    if(numpy.fromstring(zero[1].tostring(),dtype=int) == 2):
        #at this point, the zero can move [left,down,up]
        moveleft(puzzle, zero)
        print(puzzle)




#swamps elements of the puzzle
def moveUp(puzzle,zero):
    puzzle[zero[0], zero[1]], puzzle[zero[0]-1, zero[1]] = puzzle[zero[0]-1, zero[1]], puzzle[zero[0], zero[1]]

def moveleft(puzzle,zero):
    puzzle[zero[0], zero[1]], puzzle[zero[0], zero[1]-1] = puzzle[zero[0], zero[1]-1], puzzle[zero[0], zero[1]]

def movedown(puzzle,zero):
    puzzle[zero[0], zero[1]], puzzle[zero[0]+1, zero[1]] = puzzle[zero[0]+1, zero[1]], puzzle[zero[0], zero[1]]

def moveright(puzzle,zero):
    puzzle[zero[0], zero[1]], puzzle[zero[0], zero[1]+1] = puzzle[zero[0], zero[1]+1], puzzle[zero[0], zero[1]]

