class Node:
    def __init__(self, data):
    
        self.data = data
        self.next = None
    
class Linked_list:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
            
    def print_list(self):
        current = self.head
        
        while current is not None:
            print(current.data)
            current = current.next
            
s = Linked_list()
s.append('Fruit')
s.append(1)
s.print_list()
