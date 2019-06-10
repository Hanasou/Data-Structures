# Linked List implementation

class Node():
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList():
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

