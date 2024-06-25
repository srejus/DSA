'''
Give a list of operators

'+' - need to add last 2 integers in the stack
'D' - need to get last integer and *2
'C' - remove last integer from stack
if its a integer then add to the stack

return the sum of stack 

'''

def func(operations):
    stk = []
    
    for op in operations:
        if op == '+':
            stk.append(stk[-1]+stk[-2])
        elif op == 'D':
            stk.append(stk[-1]*2)
        elif op == 'C':
            stk.pop()
        else:
            stk.append(int(op))
    
    return sum(stk)

operations = ['5','-2','4','C','D','9','+','+']

x = func(operations)
print(x)
