#Assignment 1 for AI
import solver,stateFinder,treeGen
from anytree import RenderTree

def main():
    getPuzzle("puzzles.txt")

#gets the next puzzle from the file.
def getPuzzle(fileName):
    with open(fileName) as f:
        #get the goal state which will be the first element in the puzzle.txt
        goal = f.readline().split()
        print("Goal:",goal)
        #get the puzzle and turn it into a list
        content = f.readline().split()
        while content:
            root = treeGen.generateTree(''.join(content))
            solver.all(content,root)
            # stateFinder.mover(content,root)
            content = f.readline().split()
            print(RenderTree(root))
main()
