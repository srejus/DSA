from collections import deque

def level_order_traversal(root):
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        level = []
        level_size = len(queue)
    
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        res.append(level)
    
    return res