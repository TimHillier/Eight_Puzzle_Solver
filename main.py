#Assignment 1 for AI
import solver,stateFinder,treeGen
from anytree import RenderTree
import numpy as np

def main():
    getPuzzle("puzzles.txt")

#gets the next puzzle from the file.
def getPuzzle(fileName):
    with open(fileName) as f:
        #get the puzzle and turn it into a list
        content = f.readline().split()
        while content:
            root = treeGen.generateTree(''.join(content))
            stateFinder.mover(content,root)
            content = f.readline().split()
            print(RenderTree(root))
main()
