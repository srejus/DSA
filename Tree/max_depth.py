'''
Height of a tree or Maximum depth of a tree

Time: O(n)
space: O(h)

'''

def max_depth(node):
    if not node:
        return 0
    
    left = max_depth(node.left)
    right = max_depth(node.right)
    return 1 + max(left,right)