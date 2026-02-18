import QueueLinkedList as queue

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
        customeQueue = queue.Queue()
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



# preorderTraversal(newBT)
# print()
# inorderTraversal(newBT)
# print()
# postOrderTraversal(newBT)
levelOrderTraversal(newBT)
print(searchBT(newBT, "Coke"))