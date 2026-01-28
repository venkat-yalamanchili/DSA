class Node:
    def __init__(self,value=None):
        self.value = value 
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Queue:
    def __init__(self):
        self.ll = LinkedList()  # here i am creating ll object using linkedlist class.
                                # so an empty queue is created using linkedlist
    def __str__(self):
        values = []
        curr = self.ll.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        return " ".join(values)
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.ll.head == None:
            self.ll.head = new_node
            self.ll.tail = new_node
        else:
            self.ll.tail.next = new_node
            self.ll.tail= new_node

    def dequeue(self):
        if self.isEmpty():
            return "Nothng in Queue"
        else:
            pop_node = self.ll.head
            if self.ll.head == self.ll.tail:
                self.ll.head = None
                self.ll.tail = None
            else:
                self.ll.head = self.ll.head.next
            return pop_node
    
    def peek(self):
        if self.isEmpty():
            return "Nothing in Queue"
        return self.ll.head
    
    def isEmpty(self):
        if self.ll.head == None:
            return True 
        else: 
            return False
              
    def delete(self):
        self.ll.head = None
        self.ll.tail = None


        

custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
custQueue.dequeue()
custQueue.dequeue()
custQueue.dequeue()
print(custQueue)
print(custQueue.ll.head)