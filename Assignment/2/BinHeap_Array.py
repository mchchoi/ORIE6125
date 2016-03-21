import unittest

"""Implement a binary heap using array"""
class BinHeap_Array:
    def __init__(self):
        self.heap = [0]
        self.size = 0
    
    """Peek the top element of the heap"""
    """Raise exception if the heap is empty"""
    def peek(self):
        if self.size > 0:
            return self.heap[1]
        else:
            raise Exception
    
    """Insert element k to the heap"""
    def insert(self,k):
        self.heap.append(k)
        self.size = self.size + 1
        self.heapify_insert()
    
    """Heapify the array after insertion of element k"""
    def heapify_insert(self):
        i = self.size
        while (i // 2 > 0):
            if (self.heap[i//2] > self.heap[i]):
                self.swap(i//2,i)
            i = i // 2
    
    """Swap position i and j in the heap array"""
    def swap(self,i,j):
        tmp = self.heap[j]
        self.heap[j] = self.heap[i]
        self.heap[i] = tmp
        
    """Remove the smallest element in the heap (i.e. the root)"""
    """Raise exception if the heap is empty"""
    def remove(self):
        if self.size > 0:
            root = self.heap[1]
            self.heapify_remove()
            return root
        else:
            raise Exception
    
    """Given position i in the heap, return the index of the minimum of its child"""
    """Return -1 if the node is a leaf"""
    def findminchild(self,i):
        left = self.heap[min(2*i,self.size)]
        right = self.heap[min(2*i+1,self.size)]
        if (min(2*i,self.size) == min(2*i+1,self.size)):
            return -1
        else:
            return min(2*i,self.size) if (left < right) else min(2*i+1,self.size)
    
    """Heapify the array after removal of the smallest element"""
    def heapify_remove(self):
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
    
    """Build heap from array"""
    def heapify(self,array):
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
            
    """Print heap"""
    def _print(self):
        return self.heap[1:]
    
    """Time and print the insertion and popping process"""
    def rand(self,LENGTH,SEED):
        random.seed(SEED)
        heap1 = BinHeap_Array()

        # Time the insertion process
        start = time.time()
        for i in range(0,LENGTH):
            heap1.insert(random.randint(0,2*LENGTH))
        end = time.time()
        print("Insertion time: %.2f" %(end-start))

        # Time the removal process
        start = time.time()
        for i in range(0,LENGTH):
            heap1.remove()
        end = time.time()
        print("Popping time: %.2f" %(end-start))


class TestBinHeap(unittest.TestCase):
    
    def runTest(self):
        self.Testinsert()
        self.Testremove()
        self.Testheapify()
    
    def Testinsert(self):
        heap1 = BinHeap_Array()
        heap1.insert(9)
        self.assertEqual(heap1.peek(),9)
        heap1.insert(5)
        self.assertEqual(heap1.peek(),5)
        heap1.insert(4)
        self.assertEqual(heap1.peek(),4)
        heap1.insert(6)
        self.assertEqual(heap1.peek(),4)
        
    def Testremove(self):
        heap1 = BinHeap_Array()
        heap1.insert(9)
        heap1.insert(5)
        heap1.insert(4)
        heap1.insert(3)
        heap1.insert(2)
        self.assertEqual(heap1.remove(),2)
        self.assertEqual(heap1.remove(),3)
        self.assertEqual(heap1.remove(),4)
        
    def Testheapify(self):
        heap1 = BinHeap_Array()
        heap1.heapify([9])
        self.assertEqual(heap1._print(),[9])
        heap1.heapify([5,4,3,2])
        self.assertEqual(heap1._print(),[2,3,4,9,5])

a = TestBinHeap()
suite = unittest.TestLoader().loadTestsFromModule(a)
unittest.TextTestRunner().run(suite)
