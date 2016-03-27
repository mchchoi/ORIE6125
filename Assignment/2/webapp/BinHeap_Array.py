import random
import time

"""Implement a binary heap using array"""
class BinHeap_Array:
    def __init__(self):
        self.heap = [0]
        self.size = 0
    
    def peek(self):
        """Peek the top element of the heap"""
        """Raise exception if the heap is empty"""
        if self.size > 0:
            return self.heap[1]
        else:
            raise Exception
    
    def insert(self,k):
        """Insert element k to the heap"""
        self.heap.append(k)
        self.size = self.size + 1
        self.heapify_insert()
    
    def heapify_insert(self):
        """Heapify the array after insertion of element k"""
        i = self.size
        while (i // 2 > 0):
            if (self.heap[i//2] > self.heap[i]):
                self.swap(i//2,i)
            i = i // 2
    
    def swap(self,i,j):
        """Swap position i and j in the heap array"""
        tmp = self.heap[j]
        self.heap[j] = self.heap[i]
        self.heap[i] = tmp
        
    def remove(self):
        """Remove the smallest element in the heap (i.e. the root)
        Raise exception if the heap is empty"""
        if self.size > 0:
            root = self.heap[1]
            self.heapify_remove()
            return root
        else:
            raise Exception
    
    def findminchild(self,i):
        """Given position i in the heap, return the index of the minimum of its child
        Return -1 if the node is a leaf"""
        left = self.heap[min(2*i,self.size)]
        right = self.heap[min(2*i+1,self.size)]
        if (min(2*i,self.size) == min(2*i+1,self.size)):
            return -1
        else:
            return min(2*i,self.size) if (left < right) else min(2*i+1,self.size)
    
    def heapify_remove(self):
        """Heapify the array after removal of the smallest element"""
        self.heap[1] = self.heap[self.size]
        self.heap.pop(self.size)
        self.size = self.size - 1
        i = 1
        while (i < self.size):
            j = self.findminchild(i)
            if (j != -1 and self.heap[i] > self.heap[j]):
                self.swap(i,j)
            if (j == -1):
                i = self.size
            else:
                i = j
    
    def heapify(self,array):
        """Build heap from array"""
        self.heap = self.heap + array
        self.size = self.size + len(array)
        i = self.size
        while (i > 0):
            tmp = i
            while (tmp < self.size):
                j = self.findminchild(tmp)
                if (j != -1 and self.heap[tmp] > self.heap[j]):
                    self.swap(tmp,j)
                if (j == -1):
                    tmp = self.size
                else:
                    tmp = j
            i = i - 1
            
    def _print(self):
        """Print heap"""
        return self.heap[1:]

    def rand(self,LENGTH,SEED):
        """Time the insertion and popping process"""
        random.seed(SEED)
        heap1 = BinHeap_Array()

        # Time the insertion process
        start = time.time()
        for i in range(0,LENGTH):
            heap1.insert(random.randint(0,2*LENGTH))
        end = time.time()
        insert_time = end - start

        # Time the removal process
        start = time.time()
        for i in range(0,LENGTH):
            heap1.remove()
        end = time.time()
        remove_time = end - start
        return (insert_time, remove_time)


