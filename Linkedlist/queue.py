class Node:
    def __init__(self,data):
        self.data = data
        self.front = None
        self.rear = None
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.front is None:
            return
        
        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return data