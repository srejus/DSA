class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self,data):
        self.root = TreeNode(data)
    
    def add_child(self,data,node=None):
        if not node:
            node = self.root
        node_data = node.data
        if data == node_data:
            return
        
        if data < node_data:
            if node.left is None:
                new_node = TreeNode(data)
                node.left = new_node
            else:
                self.add_child(data,self.left)
        else:
            if node.right is None:
                new_node = TreeNode(data)
                node.right = new_node
            else:
                self.add_child(data,self.right)
                
                
                
    def get_data(self,res=[],node=None):
        if node is None:
            node = self.root
        
        if node:
            res.append(node.data)
            if node.left:
                self.get_data(res,node.left)
            if node.right:
                self.get_data(res,node.right)
            
        return res
    
    


x = BinarySearchTree(10)
x.add_child(5)
x.add_child(15)
data = x.get_data()
print(data)
        
        
        
        
        
        
        
        