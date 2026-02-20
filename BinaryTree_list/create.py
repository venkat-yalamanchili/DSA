class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self,value):
        if self.lastUsedIndex+1 == self.maxSize:
            return "Binary tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"
    
    def searchNode(self,nodevalue) :
        for i in range (len(self.customList)):
            if self.customList[i] == nodevalue:
                return "Success"
        return "Not Found"
    
    def preorderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preorderTraversal(index*2)
        self.preorderTraversal(index*2 +1)

    def inorderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.inorderTraversal(index*2)
        print(self.customList[index])
        self.inorderTraversal(index*2 +1)

    def postorderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.postorderTraversal(index*2)
        self.postorderTraversal(index*2 +1)
        print(self.customList[index])

    def levelordertraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return 
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -=1
                return "Success"
    
    def deleteBT(self):
        self.customList = None
        return "Binary tree has been deleted"


newBT = BinaryTree(6)
        
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffe")
newBT.preorderTraversal(1)
print()
newBT.inorderTraversal(1)
print()
newBT.postorderTraversal(1)