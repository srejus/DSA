from collections import deque

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

    def tree_height(self,node=None):
        if node is None:
            return 0
        
        left_height = self.tree_height(node.left)
        right_height = self.tree_height(node.right)
        return 1 + max(left_height,right_height)
    

    def delete_node(self,node,key):
        if not node:
            return node
        
        if key < node.data:
            node.left = self.delete_node(node.left,key)
        elif key > node.data:
            node.right = self.delete_node(node.right,key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            curr = node
            while curr.left:
                curr.left
            
            node.data = curr.data
            node.right = self.delete_node(node.right,node.data)
        return node

    def level_order_traversal(self,root):
        if not root:
            return []
    
        res = []
        queue = deque([root])

        while queue:
            level = []
            level_size = len(queue)
        
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level)
        
        return res

    
    


x = BinarySearchTree(10)
x.add_child(5)
x.add_child(15)
data = x.get_data()
height = x.tree_height(x.root)

lvl = x.level_order_traversal(x.root)
print(lvl)


print(data)
print(height)
        
        
        
        
        
        
        
        