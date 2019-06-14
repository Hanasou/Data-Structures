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
    
    def search(self, search):
        search_node = self.head
        while search_node != None:
            if search_node.data == search:
                return search_node
            search_node = search_node.next
        return 'Not Found'
    
    def delete(self, delete):
        delete_me = self.search(delete)
        
        if delete_me == 'Not Found':
            return 'Not Found'
        
        if delete_me == self.head:
            self.head = delete_me.next
            self.head.prev = None
        elif delete_me == self.tail:
            self.tail = delete_me.prev
            self.tail.next = None
        else:
            delete_me.prev.next = delete_me.next
            delete_me.next.prev = delete_me.prev
        
        delete_me = None
    
    def display(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

sample = Node(1)
sample_list = LinkedList([1,2,3])

sample_list.delete(2)
sample_list.display()