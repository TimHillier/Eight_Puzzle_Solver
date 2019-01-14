#Assignment 1 for AI
import solver
import numpy as np

def main():
    getPuzzle("puzzles.txt")

#gets the next puzzle from the file.
def getPuzzle(fileName):
    with open(fileName) as f:
        content = f.readline()
        while content:
            solver.all(twoDify(content))
            content = f.readline()


#turns the 1d array into a 2d array
def twoDify(puzzle):
    p = puzzle.split()
    return(np.reshape(p,(3,3)))
    # return puzzle.reshape((3,3))


main()
