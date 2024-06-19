class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    
class BST:
    def __init__(self,data):
        self.root = TreeNode(data)
    
    def add_child(self,data,node=None):
        if not node:
            node = self.root
        
        if node.data == data:
            return
        
        if data < node.data:
            if node.left:
                self.add_child(data,node.left)
            else:
                node.left = TreeNode(data)
        else:
            if node.right:
                self.add_child(data,node.right)
            else:
                node.right = TreeNode(data)