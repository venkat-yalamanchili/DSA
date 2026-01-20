class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self,value):
        new_node = Node (value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def __str__ (self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.value)
            if temp.next:
                result += ' <-> '
            temp = temp.next
        return result
    
    def prepend (self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

    def reverse_traverse(self):
        curr = self.tail
        while curr:
            print(curr.value)
            curr = curr.prev


new = DoubleLinkedList()
new.append(10)
new.append(20)
new.append(30)
print(new.tail)
new.prepend(60)
print(new)
new.traverse()
new.reverse_traverse()