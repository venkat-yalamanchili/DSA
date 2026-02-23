from collections import deque

class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if not rootNode.leftchild:
            rootNode.leftchild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftchild, nodeValue)
    else:
        if not rootNode.rightchild:
            rootNode.rightchild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightchild, nodeValue)
    return "The node has been successfully inserted"

def preorderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preorderTraversal(rootNode.leftchild)
    preorderTraversal(rootNode.rightchild)

def inorderTraversal(rootNode):
    pass
def postorderTraversal(rootNode):
    pass

def levelorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        queue = deque([rootNode])
        while queue:
            curr = queue.popleft()
            print(curr.data)
            if curr.leftchild:
                queue.append(curr.leftchild)
            if curr.rightchild:
                queue.append(curr.rightchild)

def search(rootNode, nodeValue):
    if not rootNode:
        return "Not Found"
    if rootNode.data == nodeValue:
        return "Found"
    elif nodeValue < rootNode.data:
        return search(rootNode.leftchild,nodeValue)
    else:
        return search(rootNode.rightchild, nodeValue)
    
def deleteNode(rootNode, nodeValue):
    pass

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftchild = None
    rootNode.rightchild = None
    return "The BST has been successfully deleted"


newBST = BSTNode(None)
insertNode(newBST,70)
insertNode(newBST,60)
insertNode(newBST,80)
print(newBST.data , newBST.leftchild.data, newBST.rightchild.data)
levelorderTraversal(newBST)
print(search(newBST, 40))