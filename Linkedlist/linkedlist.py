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
        
    
    def delete(self,data):
        if self.head is None:
            print("Empty List!")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next and curr.next.data != data:
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next
        else:
            print("Not found!")
            
    
    
        

    
