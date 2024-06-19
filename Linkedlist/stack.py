class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,data):
        if self.top is None:
            self.top = Node(data)
            return
        
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top is None:
            return 
        
        data = self.top.data
        self.top = self.top.next
        return data

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return
        data = self.top.data
        return data
    