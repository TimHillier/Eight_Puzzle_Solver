from anytree import Node,RenderTree

def generateTree(puzzle):
    root = Node(puzzle)
    print(RenderTree(root))
    return root

def addNode(node,parent):
    Node(node,parent=parent)

def generateChildren(parent):
    print(parent)

