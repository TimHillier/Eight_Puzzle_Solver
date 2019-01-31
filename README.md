# Project Title

Eight Puzzle Solver for CPSC 371 

## Getting Started

Should be able to give it a file of puzzles and will be able to solve them. 
The puzzles are in the "Puzzles.txt" file. You can add more puzzles if you would like
```
The FIRST line of "Puzzles.txt" is the goal. 
```


##Notes On Custom heuristic for Best First Search
My custom search gets the position of the planet mercury, mods the result by the number of nodes, in the list, 
and then moves to that node in the list. Its basically a random search with a unnecessarly weird, complex randomizer. 
Due to this I have commented it out as to avoid the program not finishing. 
```
If you would like to run the random search Uncomment line 7 in the Solver.py file. 
Warning that this could run a while until it finds the goal.
```