'''
We need to do a level order traversal or BFS and get the average of each level

Time: O(n)
Space: O(n)

'''

from collections import deque

def average_value(root):
    if not root:
        return []

    avgs = []
    lsm = 0
    queue = deque([root])

    while queue:
        ls = len(queue)

        for _ in range(ls):
            node = queue.popleft()
            lsm += node.data

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        avg = lsm/ls
        avgs.append(avg)
    
    return avgs