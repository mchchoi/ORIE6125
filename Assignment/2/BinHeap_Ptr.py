import Queue
import random
import time
import unittest

class Node:
    def __init__(self,data = None,parent = None,left = None,right = None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

"""Implement a binary heap using pointer"""
class BinHeap_Ptr:
    def __init__(self, root = None):
        self.root = root
        self.size = 0
    
    """Peek the top element of the heap"""
    """Raise exception if the heap is empty"""
    def peek(self):
        if self.size > 0:
            return self.root.data
        else:
            raise Exception
    
    """Insert element k to the heap"""
    def insert(self,k):
        nnode = Node(k) # Create a new node with data k
        
        # Empty heap
        if (self.size == 0):
            self.root = nnode
            self.size = self.size + 1
            return
            
        # Non-empty heap
        # Find the parent of the new node 
        s = "{0:b}".format(self.size+1)
        findparent = self.root
        for i in range(1,len(s)-1):
            if (s[i] == '1'):
                findparent = findparent.right
            else:
                findparent = findparent.left
                
        # Insert the new node
        if (s[len(s)-1] == '1'):
            findparent.right = nnode
            nnode.parent = findparent
        else:
            findparent.left = nnode
            nnode.parent = findparent
        
        # Increase the size of heap
        self.size = self.size + 1
        
        # Heapify after insertion
        self.heapify_insert(nnode)
    
    """Heapify after insertion of node"""
    def heapify_insert(self,node):
        while(node.parent != None):
            if (node.parent.data > node.data):
                self.swap(node.parent,node)
            node = node.parent
    
    """Swap the data in node1 and node2"""
    def swap(self,node1,node2):
        tmp = node2.data
        node2.data = node1.data
        node1.data = tmp
        
    """Remove the smallest element in the heap (i.e. the root)"""
    """Raise exception if the heap is empty"""
    def remove(self):
        if self.size > 0:
            rootdata = self.root.data
            if self.size > 1:
                self.heapify_remove()
            return rootdata
        else:
            raise Exception
    
    """Given a node in the heap, return the node which contains smaller data"""
    """Return None if the node is a leaf"""
    def findminchild(self,node):
        if (node.left == None and node.right == None):
            return None
        elif (node.left == None and node.right != None):
            return node.right
        elif (node.left != None and node.right == None):
            return node.left
        else:
            return node.left if (node.left.data < node.right.data) else node.right
    
    """Heapify the array after removal of the smallest element"""
    def heapify_remove(self):
        # Find the position of the last node 
        s = "{0:b}".format(self.size)
        findlast = self.root
        for i in range(1,len(s)):
            if (s[i] == '1'):
                findlast = findlast.right
            else:
                findlast = findlast.left
        
        # Set the root data to be the data of the last node
        self.root.data = findlast.data
        
        # Remove the last node
        if (s[len(s)-1] == '1'):
            findlast.parent.right = None
        else:
            findlast.parent.left = None
        
        # Decrease the size of heap
        self.size = self.size - 1
        
        # Top-down heapify
        tmp = self.root
        while(self.findminchild(tmp)!=None):
            minchild = self.findminchild(tmp)
            if (tmp.data > minchild.data):
                self.swap(tmp,minchild)
            tmp = minchild
            
    """Print heap in array format"""
    def _print(self):
        q = Queue.Queue()
        q.put(self.root)
        out = []
        while q.empty() == False:
            tmp = q.get()
            out.append(tmp.data)
            if (tmp.left != None):
                q.put(tmp.left)
            if (tmp.right != None):
                q.put(tmp.right)
        return out
    
    """Time and print the insertion and popping process"""
    def rand(self,LENGTH,SEED):
        random.seed(SEED)
        heap1 = BinHeap_Ptr()

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
