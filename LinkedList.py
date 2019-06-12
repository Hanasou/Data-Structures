# Linked List implementation

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList():
    def __init__(self, array = None):
        self.head = None
        self.tail = None

        if array != None:
            for num in array:
                self.append(num)
        pass

    def append(self, insert):
        insert_node = Node(insert)
        if self.head == None:
            self.head = insert_node
            self.tail = insert_node
        else:
            self.tail.next = insert_node
            insert_node.prev = self.tail
            self.tail = insert_node
        pass
    
    def display(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

sample = Node(1)
sample_list = LinkedList([1,2,3])

sample_list.display()