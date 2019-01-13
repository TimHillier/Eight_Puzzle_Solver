#Assignment 1 for AI
import solver

def main():
    print("main")
    getPuzzle("puzzles.txt")

#gets the next puzzle from the file.
def getPuzzle(fileName):
    with open(fileName) as f:
        content = f.readline()
        while content:
            solver.all(content)
            content = f.readline()

main()
