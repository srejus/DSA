class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    

class BinaryTree:
    def __init__(self,root_data):
        self.root = TreeNode(root_data)
    
    def insert_left(self,node,data):
        if node.left is None:
            node.left = TreeNode(data)
            return
        new_node = TreeNode(data)
        new_node.left = node.left
        node.left = new_node
    
    def insert_right(self,node,data):
        if node.right is None:
            node.right = TreeNode(data)
            return
        new_node = TreeNode(data)
        new_node.right = node.right
        node.right = new_node

    def pre_order_traversal(self,node,res=[]):
        # Root -> Left -> Right
        if node:
            res.append(node.data)
            self.pre_order_traversal(node.left,res)
            self.pre_order_traversal(node.right,res)
        
        return res

    def in_order_traversal(self,node,res=[]):
        # Left -> Root -> Right
        if node:
            self.pre_order_traversal(node.left,res)
            res.append(node.data)
            self.pre_order_traversal(node.right,res)
        
        return res

    def post_order_traversal(self,node,res=[]):
        # Left -> Right - Root
        if node:
            self.pre_order_traversal(node.left,res)
            self.pre_order_traversal(node.right,res)
            res.append(node.data)
        
        return res


bt = BinaryTree(1)
bt.insert_left(bt.root, 2)
bt.insert_right(bt.root, 3)
bt.insert_left(bt.root.left, 4)
bt.insert_right(bt.root.left, 5)

print("Pre-order Traversal:", bt.pre_order_traversal(bt.root, []))
print("In-order Traversal:", bt.in_order_traversal(bt.root, []))
print("Post-order Traversal:", bt.post_order_traversal(bt.root, []))