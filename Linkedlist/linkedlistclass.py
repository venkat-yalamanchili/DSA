class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

# first for understanding we try to create a linkedlist just with one node(Head and tail both points to same node)
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 # we are just adding another attribute to the linked list which will be easy for us later to access the length of the linked list

new_linked_list = LinkedList(10)
print(new_linked_list)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)
print(new_linked_list.length)

# How to create an empty linked list
class EmptyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0