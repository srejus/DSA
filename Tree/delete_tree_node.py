'''
Delete node from BST
'''

def delete_node(node,key):
    if not node:
        return node
    
    if key < node.data:
        node.left = delete_node(node.left,key)
    elif key > node.data:
        node.right = delete_node(node.right,key)
    else:
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        
        curr = node
        while curr.left:
            curr.left
        
        node.data = curr.data
        node.right = delete_node(node.right,node.data)
    return node