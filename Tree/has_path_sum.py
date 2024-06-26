'''Problem 7: Path Sum

Explanation: Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up 
all the values along the path equals the given sum.'''


def has_path_sum(node,sm):
    if not node:
        return False
    
    if not node.left and not node.right:
        return sm == node.data
    
    return has_path_sum(node.left,sm-node.data) or has_path_sum(node.right,sm-node.data)

