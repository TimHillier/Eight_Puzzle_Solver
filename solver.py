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
