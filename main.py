#Assignment 1 for AI
import solver,stateFinder
import numpy as np

def main():
    getPuzzle("puzzles.txt")

#gets the next puzzle from the file.
def getPuzzle(fileName):
    with open(fileName) as f:
        #get the puzzle and turn it into a list
        content = f.readline().split()
        while content:
            print("CP:",content)
            stateFinder.mover(content)
            content = f.readline().split()
            print("__________________________________________________")

main()
