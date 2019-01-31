from anytree import Node,RenderTree
Root = ""

def generateTree(puzzle):
    global Root
    Root = Node(puzzle)
    return Root

def addNode(node,parent,move):
    #need to make sure that node is in fact a node
    if not isinstance(node,Node):
        node = Node(node)

    if not isinstance(parent,Node):
        parent = Node(parent)

    Node(node,parent=parent,MOVE=move,FCOST=node.depth,GCOST=node.depth,HCOST =0)


def addNodeBest(node,parent,move):
    #need to make sure that node is in fact a node
    if not isinstance(node,Node):
        node = Node(node)

    if not isinstance(parent,Node):
        parent = Node(parent)

    Node(node.name,parent=parent,MOVE=move)

def getRoot():
    return Root
