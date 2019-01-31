import treeGen,stateFinder
import ephem,time
from anytree import RenderTree,Node,PreOrderIter
from queue import *
#solver for the puzzle
heuristics = ["Mann","TOOP"] #the heuristcs for best first search
# heuristics.append("Custom") #uncomment this if you want to do the custom search,
#runs all solvers
def all(puzzle,parent,goal):
    thisTree = stateFinder.mover(puzzle, parent,True)
    print("Breath First:--------------------")
    breadFirst(thisTree, treeGen.getRoot(),goal) # this works
    print("Best First:----------------------")
    for x in heuristics:
        print("----------",x,"----------------------------")
        bestFirst(thisTree,treeGen.getRoot(),x,goal)
    print("A Star------------------------------")
    aStar(thisTree,treeGen.getRoot(),goal)


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
            newList.append(list(map(int, a)))
        for a in newList:
            val=(sum(abs((val-1)%3-i%3) + abs((val-1)//3 - i//3) for i, val in enumerate(a) if val))
            if val < bestCost:
                bestCost = val
                bestNode = listofnodes[newList.index(a)]
        return bestNode

    elif heur == "TOOP":
        newList = []
        for l in listofnodes:
            a = getName(l)
            newList.append(list(map(int,a)))
        for a in newList:
            tiles = 0
            for i in range(0,7):
                if a[i] != i+1:
                    tiles +=1
            if a[8] != 0:
                tiles += 1
            if tiles < bestCost:
                bestCost = tiles
                bestNode = listofnodes[newList.index(a)]

        return bestNode

    #moves randomly based on the position of a Mercury
    elif heur == "Custom":
        planet = ephem.Mercury()
        planet.compute()
        c = str(planet.ra) + str(planet.dec)
        c = c.replace(':','')
        c = c.replace('.','')
        c = c.replace('-','')
        c = int(c) % len(listofnodes)
        return listofnodes[c]



def aStar(puzzle,rootNode,goal):
    rootNode = Node(rootNode.name,FCOST =0,GCOST=0,HCOST = 0)
    open_list = [rootNode]
    closed_list = set()
    currentNode = ''
    condition = True
    while condition:
        lowest_fcost = 9999999
        for n in open_list:
            if n.FCOST < lowest_fcost:
                lowest_fcost = n.FCOST
                currentNode = n
        open_list.remove(currentNode)
        closed_list.add(currentNode.name)

        if currentNode.name == ''.join(goal):
            print("YAAY!,you found the goal. Steps: ", currentNode.depth, ". You visited ", len(closed_list), " Nodes")
            condition = False
            # Get_Path(currentNode)

        children = generateChildren(currentNode,True)

        for ch in children:
            # print("ch",ch.name,closed_list)
            # if ch.name in closed_list:
            #     print("already checked",ch.name)
            #     break
            if ch.name == ''.join(goal):
                print("YAAY!,you found the goal. Steps: ", ch.depth, ". You visited ", len(closed_list) + 1, " Nodes")
                condition = False
                break
            else:
                ch.GCOST = ch.depth
                ch.HCOST = genHcost(ch)
                ch.FCOST = ch.GCOST + ch.HCOST
                if ch.name not in closed_list and ch.name not in open_list:
                    open_list.append(ch)

def genHcost(node):
    cost = 0
    node = node.name
    node = list(node)
    # print("n",node)
    for i in range(0, 7):
        if int(node[i]) != (i + 1):
            cost += 1
    if int(node[8]) != 0:
        cost += 1
    return cost


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


def Get_Path(current):
    while current.parent:
        print(current.parent)

