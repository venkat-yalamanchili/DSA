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
    
    def traverse(self):  # Travesing through linkedlist create a current node and use while loop similar to what we did in __str__ method
        current = self.head
        while current is not None:  # this can be written as while current: This is more python way
            print(current.value)
            current = current.next
    
    def search(self,target):
        current = self.head
        index = 0 ## if we want to return the index we will just initiate index = 0 and increment it every iteration
        while current:
            if current.value == target:
                return True # here we will return index
            current = current.next
            #index += 1
        return False
    
    def get(self,index):
        current = self.head
        if index < 0 or index>=self.length: # this will return None if we try to insert the given value at negative index or index greater than length of the linkedlist
            return None 
        else:
            for _ in range(index):
                current = current.next
            return current # it will return node object if you want value just write current.value
        

    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length == 0: # last edge case is we need to check if ll is empty
            return None
        popped_node = self.head
        if self.length == 1:  # Handle this edge case 
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        popped_node = self.tail
        if self.length == 1:  
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node
    
    def remove(self,index):
        pass

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

        
new_linkedlist = LinkedList()
new_linkedlist.append(10)
new_linkedlist.prepend(20)
new_linkedlist.insert(30,1)

print(new_linkedlist)

print(new_linkedlist.search(20))