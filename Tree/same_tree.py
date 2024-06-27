'''
Given p and q are 2 trees we need to return True if both of them looks same else False

Here we are using helper function to make it more readable we can diretly use the main function
Time: O(n)
Space: O(h)
'''

def is_same_tree(p,q):
    def is_same(p,q):
        if not p and not q:
            return True
        
        if(p and not q) or (not p and q):
            return False
        
        if p.data != q.data:
            return False
    
        return is_same(p.left,q.left) and is_same(p.right,q.right)

    return is_same(p,q)