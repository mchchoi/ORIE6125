import unittest
from BinHeap_Ptr import BinHeap_Ptr

class TestBinHeap_Ptr(unittest.TestCase):
    
    def runTest(self):
        self.Testinsert()
        self.Testremove()
        #self.Testheapify()
    
    def Testinsert(self):
        heap1 = BinHeap_Ptr()
        heap1.insert(9)
        self.assertEqual(heap1.peek(),9)
        heap1.insert(5)
        self.assertEqual(heap1.peek(),5)
        heap1.insert(4)
        self.assertEqual(heap1.peek(),4)
        heap1.insert(6)
        self.assertEqual(heap1.peek(),4)
        
    def Testremove(self):
        heap1 = BinHeap_Ptr()
        heap1.insert(9)
        heap1.insert(5)
        heap1.insert(4)
        heap1.insert(3)
        heap1.insert(2)
        self.assertEqual(heap1.remove(),2)
        self.assertEqual(heap1.remove(),3)
        self.assertEqual(heap1.remove(),4)
        self.assertEqual(heap1.remove(),5)
        self.assertEqual(heap1.remove(),9)


a = TestBinHeap_Ptr()
suite = unittest.TestLoader().loadTestsFromModule(a)
unittest.TextTestRunner().run(suite)
