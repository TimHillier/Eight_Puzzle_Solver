from anytree import Node,RenderTree
Root = ""

def generateTree(puzzle):
    global Root
    Root = Node(puzzle)
    return Root

def addNode(node,parent):
    Node(node,parent=parent)

def getRoot():
    return Root
