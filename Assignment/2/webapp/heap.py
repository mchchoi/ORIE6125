from flask import Flask, render_template, request

app = Flask(__name__)
heapdict = {}  # A dictionary containing all heaps

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
        v = heapdict[name]
        name = BinHeap_Array()
        name.heapify(heapdict[name])
        return name.remove()
    else:
        return "There is no heap with desired name", 400
    
@app.route('/heap/<name>/peak', methods=['GET'])
def heap_peak(name):
    if name in heapdict.keys():
        v = heapdict[name]
        name = BinHeap_Array()
        name.heapify(heapdict[name])
        return name.peek()
    else:
        return "There is no heap with desired name", 400

@app.route('/heap/time/array', methods=['GET'])
def heap_timearray(name):
    LENGTH = request.args.get('length')
    SEED = request.args.get('seed')
    if (not isinstance(LENGTH,int)):
        return "length should be an integer", 400
    
    (insert_time, remove_time) = BinHeap_Array().rand(LENGTH,SEED)
    return "The insertion time is " + str(insert_time) + '\n' + "The popping time is " + str(remove_time)

@app.route('/heap/time/pointer', methods=['GET'])
def heap_timeptr(name):
    LENGTH = request.args.get('length')
    SEED = request.args.get('seed')
    if (not isinstance(LENGTH,int)):
        return "length should be an integer", 400
    
    (insert_time, remove_time) = BinHeap_Ptr().rand(LENGTH,SEED)
    return "The insertion time is " + str(insert_time) + '\n' + "The popping time is " + str(remove_time)

if __name__ == "__main__":
    app.run(debug=True)                                          
