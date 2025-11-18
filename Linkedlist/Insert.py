class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self,value,index): # Inserting an element at the given index
        new_node = Node(value) 
        if index < 0 or index>self.length: # this will return false if we try to insert the given value at negative index or index greater than length of the linkedlist
            return False
        if self.length == 0: # This will take care if the linkedlist is empty
            self.head = new_node 
            self.tail = new_node 
        elif index == 0: # This will take care if we want to insert at the start
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
        

new_linkedlist = LinkedList()
new_linkedlist.append(10)
new_linkedlist.prepend(20)
new_linkedlist.insert(30,1)

print(new_linkedlist)