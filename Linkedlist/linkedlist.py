class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
    
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = new_node
        return
    
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def print_data(self):
        if self.head is None:
            return None
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
    
    
        

    
