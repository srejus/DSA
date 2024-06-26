'''
If the difference between left and right subtrees are <= 1 then it is balanced

Why we are using list (balanced[]) instead of varaible

-> since variable is immutable and we are using a helper function the variable value will remain same 
which result in incorect answer

'''

def is_balanced(root):
    balanced = [True]

    def height(root):
        if not root:
            return 0
        
        left_height = height(root.left)
        if balanced[0] is False:
            return 0
        
        right_height = height(root.right)

        if abs(left_height-right_height) > 1:
            balanced[0] = False
            return 0
        
        return 1 + max(left_height,right_height)

    height(root)
    return balanced[0]