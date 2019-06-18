# Heap Implementaiton
import random

class Heap():

    def __init__(self, array = None):
        if array == None:
            self.array = []
        else:
            self.array = array
            for i in range(0, len(array) // 2)[::-1]:
                self.max_heapify(i)
        pass

    def parent_index(self, index):
        return index // 2
    
    def left_index(self, index):
        return 2 * index
    
    def right_index(self, index):
        return (2 * index) + 1
    
    def max_heapify(self, index):
        pass
        left = self.left_index(index)
        right = self.right_index(index)
        
        if left <= len(self.array) and self.array[left] > self.array[index]:
            largest = left
        else:
            largest = index
        
        if right <= len(self.array) and self.array[right] > self.array[index]:
            largest = right
        
        if largest != index:
            self.array[index], self.array[largest] = self.array[largest], self.array[index]
            self.max_heapify(largest)
    
    def increase_key(self, index, key):
        self.array[index] = self.array[index] + key
        while index > 0 and self.array[self.parent_index(index)] < self.array[index]:
            self.array[index], self.array[self.parent_index(index)] = self.array[self.parent_index(index)], self.array[index]
            index = self.parent_index(index)
        pass
    
    def insert(self, data):
        self.array.append(0)
        self.increase_key(len(self.array) - 1, data)
    
    def extract_max(self):
        max_val = self.array[0]
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        self.max_heapify(1)
        self.array.pop(-1)
        return max_val
        pass

heap = Heap([random.randint(0, 20) for i in range(20)])