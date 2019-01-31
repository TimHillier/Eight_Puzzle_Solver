#Assignment 1 for AI
import solver,stateFinder,treeGen,output
from anytree import RenderTree

def main():
    output.initFile()
    getPuzzle("puzzles.txt")
    print("Done")


#i know the puzzle i submitted is not solvable, so lets check for that
def isSolvable(puzzle):
    inversions =0

    for i in range(0,len(puzzle)-1):
        for j in range(i+1,len(puzzle)):
            if int(puzzle[i]) > int(puzzle[j]):
                inversions += 1

        if int(puzzle[i]) == 0 and i%2 ==1:
            inversions += 1


    return (inversions %2 == 0)
#gets the next puzzle from the file.
def getPuzzle(fileName):
    with open(fileName) as f:
        #get the goal state which will be the first element in the puzzle.txt
        goal = f.readline().split()
        # print("Goal:",goal)

        #get the puzzle and turn it into a list
        content = f.readline().split()
        while content:
            output.writeToFile("Current Puzzle:" + ''.join(content))
            print("Current Puzzle:",content)
            if(isSolvable(content)):
                root = treeGen.generateTree(''.join(content))
                solver.all(content,root,goal)
                content = f.readline().split()
            else:
                output.writeToFile("Current Puzzle: Not Solvable")
                print("Current Puzzle: not solvable")
                content = f.readline().split()
main()


