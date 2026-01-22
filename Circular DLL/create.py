class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class CircularDLL:  # first we create empty then we write methods to insert  
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head, self.tail = new_node, new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr:
            result += str(curr.value)
            curr = curr.next
            if curr == self.head:
                break
            result += " <-> "
        return result
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head, self.tail = new_node, new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.head = new_node
        self.length += 1

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            if temp == self.head: break

    def reverse_traverse(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.prev
            if temp == self.tail: break

    def search(self,target):
        temp = self.head
        while temp:
            if temp.value == target:
                return True
            temp = temp.next
            if temp == self.head:break
        return False
    
    def get(self,index):
        if index<0 or index >= self.length:
            return None
        if index < self.length // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.length-1, index, -1):
                curr = curr.prev
        return curr
    
    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index<0 or index>self.length:
            print("Index out of range")
            return
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head,self.tail = None, None
        else:
            self.head = self.head.next
            popped_node.next = None
            popped_node.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            popped_node.next = None
            popped_node.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
        return popped_node
    
    def remove(self,index):
        if index<0 or index>=self.length:
            print("Index out of range")
            return
        if index == 0:
            self.pop_first
            return
        if index == self.length-1:
            self.pop()
            return
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        self.length-=1
        return popped_node
    
    def delete_all(self):
        self.head = self.tail = None
        self.length = 0
            

new = CircularDLL()
new.append(10)
new.append(20)
new.append(30)
new.prepend(40)
print(new)
new.set(2,90)
print(new)
# new.traverse()
# new.reverse_traverse()
# print(new.head)
# print(new.tail)
print(new.get(3))