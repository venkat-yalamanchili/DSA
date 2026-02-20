import QueueLinkedList as queue
from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

        
newBT = TreeNode("Drinks")
newBT.leftchild = TreeNode("Hot")
newBT.rightchild = TreeNode("Cold")
newBT.leftchild.leftchild = TreeNode("Tea")
newBT.leftchild.rightchild = TreeNode("Coffe")
newBT.rightchild.leftchild = TreeNode("Coke")
newBT.rightchild.rightchild = TreeNode("Pepsi")


def preorderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preorderTraversal(rootNode.leftchild)
    preorderTraversal(rootNode.rightchild)

def inorderTraversal(rootNode):
    if not rootNode: 
        return 
    inorderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inorderTraversal(rootNode.rightchild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customeQueue = queue.Queue()  # here we are using the queue data structure that we created using linkedlist
        customeQueue.enqueue(rootNode)
        while not(customeQueue.isEmpty()):
            root = customeQueue.dequeue()
            print(root.value.data)
            if (root.value.leftchild is not None):
                customeQueue.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                customeQueue.enqueue(root.value.rightchild)

def searchBT(rootNode,nodeValue):
    if not rootNode:
        return
    else:
        customeQueue = queue.Queue()
        customeQueue.enqueue(rootNode)
        while not(customeQueue.isEmpty()):
            root = customeQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.leftchild is not None):
                customeQueue.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                customeQueue.enqueue(root.value.rightchild)
        return "Not Found"
    
def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        queue = deque([rootNode])  # here we are creating the queue using deque from collections
        while queue:               # just to get familiar with both ways
            current = queue.popleft()
            if current.leftchild:
                queue.append(current.leftchild)
            else:
                current.leftchild = newNode
                return "Sucess"
            if current.rightchild:
                queue.append(current.rightchild)
            else:
                current.rightchild = newNode
                return "Sucess"

def getdeepestNode(rootNode):
    if not rootNode:
        rootNode 
    else:
        queue = deque([rootNode])
        while queue:
            current = queue.popleft()
            if current.leftchild:
                queue.append(current.leftchild)
            if current.rightchild:
                queue.append(current.rightchild)
        return current

def deletedeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        queue = deque([rootNode])
        while queue:
            current = queue.popleft()
            if current is dNode:
                current = None
                return
            if current.rightchild:
                if current.rightchild is dNode:
                    current.rightchild = None
                    return
                else:
                    queue.append(current.rightchild)
            if current.leftchild:
                if current.leftchild is dNode:
                    current.leftchild = None
                    return
                else:
                    queue.append(current.leftchild)

def deleteNodeBT(rootNode,node):
    if not rootNode:
        return "The BT does not exist"
    else:
        queue = deque([rootNode])
        while queue:
            current = queue.popleft()
            if current.data == node:
                dNode = getdeepestNode(rootNode)
                current.data = dNode.data  # to delete a binary node we first copy the deepestnode value then we 
                deletedeepestNode(rootNode, dNode)   # delete the deepest node
                return "The node has been successfully deleted"
            if current.leftchild:
                queue.append(current.leftchild)
            if current.rightchild:
                queue.append(current.rightchild)
        return "Failed to delete"
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftchild = None
    rootNode.rightchild = None
    return
# postOrderTraversal(newBT)
# print()
# inorderTraversal(newBT)
# print()
# postOrderTraversal(newBT)
levelOrderTraversal(newBT)
# print(searchBT(newBT, "Coke"))
# newNode = TreeNode("Black")
# insertNode(newBT,newNode)
# print(getdeepestNode(newBT).data) #because this returns the node to print out the value we need .data
# newNode = getdeepestNode(newBT)
# deletedeepestNode(newBT,newNode)
# levelOrderTraversal(newBT)

deleteNodeBT(newBT,'Hot')
levelOrderTraversal(newBT)