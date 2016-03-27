import random
import time
import Queue

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
    
    def peek(self):
        """Peek the top element of the heap
        Raise exception if the heap is empty"""
        if self.size > 0:
            return self.root.data
        else:
            raise Exception
    
    def insert(self,k):
        """Insert element k to the heap"""
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
    
    def heapify_insert(self,node):
        """Heapify after insertion of node"""
        while(node.parent != None):
            if (node.parent.data > node.data):
                self.swap(node.parent,node)
            node = node.parent
    
    def swap(self,node1,node2):
        """Swap the data in node1 and node2"""
        tmp = node2.data
        node2.data = node1.data
        node1.data = tmp
        
    def remove(self):
        """Remove the smallest element in the heap (i.e. the root)
        Raise exception if the heap is empty"""
        if self.size > 0:
            rootdata = self.root.data
            if self.size > 1:
                self.heapify_remove()
            return rootdata
        else:
            raise Exception
    
    def findminchild(self,node):
        """Given a node in the heap, return the node which contains smaller data
        Return None if the node is a leaf"""
        if (node.left == None and node.right == None):
            return None
        elif (node.left == None and node.right != None):
            return node.right
        elif (node.left != None and node.right == None):
            return node.left
        else:
            return node.left if (node.left.data < node.right.data) else node.right
    
    def heapify_remove(self):
        """Heapify the array after removal of the smallest element"""
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
            
    def _print(self):
        """Print heap in array format"""
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
    
    def rand(self,LENGTH,SEED):
        """Time and print the insertion and popping process"""
        random.seed(SEED)
        heap1 = BinHeap_Ptr()

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
                                 
