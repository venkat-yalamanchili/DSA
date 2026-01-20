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
    
    def search(self,target):
        curr = self.head
        index = 0
        while curr:
            if curr.value == target:
                return index
            curr = curr.next
            index += 1
        return False

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            curr = self.head
            for _ in range (index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range (self.length-1, index, -1):
                curr = curr.prev
        return curr
    
    def set(self,index,value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    def insert(self,index,value):
        new_node = Node(value)
        if index < 0 or index >self.length:
            return IndexError("Index out of range")
        if index == 0:
            if not self.head:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            temp = self.get(index-1)
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
        self.length += 1

    def pop_first(self):
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if not self.head:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        pass 


new = DoubleLinkedList()
new.append(10)
new.append(20)
new.append(30)
new.append(40)
new.insert(4,50)
# print(new.tail)
# new.prepend(60)
print(new)
# new.traverse()
# new.reverse_traverse()
# print(new.search(20))
# print(new.get(2))