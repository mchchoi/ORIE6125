import unittest
from BinHeap_Array import BinHeap_Array

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
