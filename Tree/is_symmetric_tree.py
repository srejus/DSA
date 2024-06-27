def is_symmetric(root):
    def same(root1,root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False
    
        if root1.data != root2.data:
            return False
    
        return same(root1.left,root2.right) and same(root1.right,root2.left)

    return same(root,root)


# Time: O(n)
# Space: O(n)
