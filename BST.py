# Binary Search Tree

class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    
    def is_leaf(self):
        if self.left == None and self.right == None:
            return True
        else:
            return False

class BST():
    def __init__(self):
        self.root = None
        pass
    
    def search(self, n):
        curr_node = self.root
        if curr_node == None:
            return None
        if curr_node.val == n:
            return curr_node
        
        if curr_node.val > n:
            pass
    
    def insert(self, n):
        pass
    
    def delete(self, n):
        pass