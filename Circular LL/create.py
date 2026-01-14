class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLinkedList:     # this circular linked list with one element
    # def __init__(self,value):
    #       new_node = Node(value)
    #       new_node.next = new_node
    #       self.head = new_node
    #       self.tail = new_node
    #       self.length = 1
    
    def __init__ (self) : #this is to create a empty CSLL
        self.head = None
        self.tail = None
        self.length = 0

    def append (self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head, self.tail = new_node , new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += '->'
        return result
    
    def prepend (self,value):
        new_node = Node(value)
        if self.length == 0:  # here you can also use self.head is None
            self.head, self.tail = new_node , new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.length+=1


    
csll = CSLinkedList()
csll.append(10)
csll.append(20)
csll.append(30)
csll.append(40)
print(csll)            
            

          