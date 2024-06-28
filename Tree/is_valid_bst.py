def is_valid_bst(root):
    def is_valid(node,minn,maxx):
        if not node:
            return True
        
        if node.data <= minn and node.data >= maxx:
            return False
    
        return is_valid(node.left,minn,maxx) and is_valid(node.right,minn,maxx)

    return is_valid(root,float('-inf'), float('inf'))


# Time: O(n)
# Space: O(h)