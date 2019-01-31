import treeGen,stateFinder
from anytree import RenderTree,Node,PreOrderIter
from queue import *
#solver for the puzzle
# heuristics = ["Mann","tOOP","custom"] #the heuristcs for best first search
heuristics = ["Mann"]

#runs all solvers
def all(puzzle,parent,goal):
    thisTree = stateFinder.mover(puzzle, parent)
    print("Breath First:--------------------")
    breadFirst(thisTree, treeGen.getRoot(),goal) # this works
    # aStar(thisTree)
    # print("Best First:----------------------")
    # for x in heuristics:
    #     print("----------",x,"----------------------------")
    #     bestFirst(thisTree,treeGen.getRoot(),x,goal)


def breadFirst(BaseTree,rootNode,goal): #some whole wheat action
    q = Queue()
    for children in PreOrderIter(BaseTree):
        q.put(children)

    visited = set()  # visited
    visited.add(rootNode.name)  #visited source

    while not q.empty():
        # print("Size Q:",q.qsize())
        # print("Size vis",visited)
        v = q.get()

        #this means that we can skip it
        if v.name in visited:
            continue
        visited.add(v.name.name)

        #if it is the goal we win
        if v.name.name == ''.join(goal):
            print("YAY!,you found the goal. Steps: ",v.depth ,". You visited ",len(visited)," Nodes")
            break
        #add the current thing to the node
        # print("Adding to Visited")
        # add the children nodes to the queue
        children = generateChildren(v,False)
        for ch in children:
            if ch.name.name not in visited:
                q.put(ch)




def bestFirst(BaseTree,rootNode,heur,goal):
    closed_List = set()
    open_list = [rootNode]
    condition = True

    while condition:
        bestNode = calcHeuristic(open_list,heur)

        closed_List.add(bestNode.name)
        # print("length",len(closed_List))
        open_list.remove(bestNode)

        # print(bestNode.name,''.join(goal))

        if bestNode.name == ''.join(goal):
            print("YAY!,you found the goal. Steps: ",bestNode.depth ,". You visited ",len(closed_List)," Nodes")
            break

        # print("aaaa",bestNode)
        children = generateChildren(bestNode,True)
        # print("ze child",children[0])

        for ch in children:
            # print(ch.name,''.join(goal))
            if ch.name == ''.join(goal):
                print("YAAY!,you found the goal. Steps: ",ch.depth ,". You visited ",len(closed_List)+1," Nodes")
                condition = False
                break

            # print("sanity",ch not in closed_List and ch not in open_list)
            elif ch.name not in closed_List and ch.name not in open_list:
                # print("append",ch)
                open_list.append(ch)



def calcHeuristic(listofnodes,heur):
    bestNode = ""
    bestCost = 99999
    if heur == "Mann":
        newList =[]
        for l in listofnodes:
            a = getName(l)
            # print("here",type(a))
            newList.append(list(map(int, a)))
        for a in newList:
            val=(sum(abs((val-1)%3-i%3) + abs((val-1)//3 - i//3) for i, val in enumerate(a) if val))
            if val < bestCost:
                bestCost = val
                bestNode = listofnodes[newList.index(a)]
        return bestNode

def aStar(puzzle):
    print(puzzle)


def generateChildren(currentParent,check):
    #so current parent is not a parent or a node we gotta make it a node fam
    parent = stateFinder.mover(currentParent,currentParent,check)
    # print("par",parent)
    nextStates = []
    for ch in parent.children:
        nextStates.append(ch)
    return nextStates

def getName(node):
    if isinstance(node.name, str):
        return node.name
    else:
        getName(node.name)

