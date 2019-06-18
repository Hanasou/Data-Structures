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
    
    def insert(self, n):
        pass
    
    def delete(self, n):
        pass
    
    def search(self, n):
        pass