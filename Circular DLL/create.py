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

new = CircularDLL()
new.append(10)
new.append(20)
new.append(30)
new.prepend(40)
print(new)
new.traverse()
new.reverse_traverse()
# print(new.head)
# print(new.tail)