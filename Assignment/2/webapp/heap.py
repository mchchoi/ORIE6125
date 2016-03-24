from flask import Flask, render_template, request
import random
import time
import Queue

app = Flask(__name__)
heapdict = {}  # A dictionary containing all heaps

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
        #print("Insertion time: %.2f" %(end-start))
        insert_time = end - start

        # Time the removal process
        start = time.time()
        for i in range(0,LENGTH):
            heap1.remove()
        end = time.time()
        #print("Popping time: %.2f" %(end-start))
        remove_time = end - start
        return (insert_time, remove_time)

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
        #print("Insertion time: %.2f" %(end-start))
        insert_time = end - start

        # Time the removal process
        start = time.time()
        for i in range(0,LENGTH):
            heap1.remove()
        end = time.time()
        #print("Popping time: %.2f" %(end-start))
        remove_time = end - start
        return (insert_time, remove_time)




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/heap/<name>', methods=['GET'])
def heap_get(name=None):
    if name == None:
        return "Please enter a name for the heap you want to inquiry!", 400
    if name in heapdict.keys():
	v = heapdict[name]
        name = BinHeap_Array()
        name.heapify(v)
        return "The size of the heap is " + str(name.size) + '\n' + "The heap is (in array format):" + ','.join(map(str,name._print()))
    else:
        return "There is no heap with desired name", 400

@app.route('/project', methods=['GET'])
def project_get():
    return render_template('project.html')

@app.route('/heap/<name>', methods=['POST'])
def heap_post(name):
    els = request.form.get('values', None)

    if els is None:
        return 'No "values" parameter was provided', 400

    try:
        els = [int(e) for e in els.split(',')]
    except ValueError as e:
        return str(e), 400
    
    if name in heapdict.keys():
        heapdict[name] = heapdict[name] + els
    else:
        heapdict[name] = els
        
    return "Successfully inserted!"
  
@app.route('/heap/<name>/pop', methods=['GET'])
def heap_pop(name):
    if name in heapdict.keys():
        tmp = name
        v = heapdict[name]
        name = BinHeap_Array()
        name.heapify(v)
        out = str(name.remove())
        heapdict[tmp] = name._print()
        return out
    else:
        return "There is no heap with desired name", 400
 
@app.route('/heap/<name>/peak', methods=['GET'])
def heap_peak(name):
    if name in heapdict.keys():
        v = heapdict[name]
        name = BinHeap_Array()
        name.heapify(v)
        return str(name.peek())
    else:
        return "There is no heap with desired name", 400

@app.route('/heap/time/array', methods=['GET'])
def heap_timearray():
    LENGTH = request.args.get('length', type=int)
    SEED = request.args.get('seed', type=int)
    #if (not isinstance(LENGTH,int)):
    #    return "length should be an integer", 400
    
    (insert_time, remove_time) = BinHeap_Array().rand(LENGTH,SEED)
    return "The insertion time is " + str(insert_time) + '\n' + "The popping time is " + str(remove_time)

@app.route('/heap/time/pointer', methods=['GET'])
def heap_timeptr():
    LENGTH = request.args.get('length', type=int)
    SEED = request.args.get('seed', type=int)
    #if (not isinstance(LENGTH,int)):
    #    return "length should be an integer", 400
    
    (insert_time, remove_time) = BinHeap_Ptr().rand(LENGTH,SEED)
    return "The insertion time is " + str(insert_time) + '\n' + "The popping time is " + str(remove_time)

if __name__ == "__main__":
    app.run(debug=True)                                          
