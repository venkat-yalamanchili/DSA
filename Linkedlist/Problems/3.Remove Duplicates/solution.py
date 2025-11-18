
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
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def remove_duplicates(self):
        if not self.head:
            return None
        node_values = set()
        curr = self.head
        node_values.add(curr.value)
        while curr.next:
            if curr.next.value in node_values:
                curr.next = curr.next.next
                self.length -= 1
            else:
                curr = curr.next
                node_values.add(curr.value)
        self.tail = curr

    # for the 2nd version if the given linked list is sorted
    def deleteDuplicates(self, head):
        if not head:
            return None
        curr = head
        while curr.next:
            if curr.val == curr.next.val: # since it is sorted duplicates will be adjacent to each other
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head