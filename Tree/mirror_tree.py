'''
Invert binary Tree or Mirror binary Tree
'''

def mirror_tree(node):
    if not node:
        return None
    
    node.left, node.right = mirror_tree(node.right), mirror_tree(node.left)
    return node
    