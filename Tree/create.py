class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children
    
    def __str__(self,level=0):
        ret = " "*level+str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret 
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

root = TreeNode("Drinks",[])
c1 = TreeNode("Cold", []) 
c2 = TreeNode("Hot", [])
c11 = TreeNode("Tea", []) 
root.addChild(c1)
root.addChild(c2)
c2.addChild(c11)

print(root)