from flask import Flask, render_template, request
import random
import time
import Queue
from BinHeap_Array import BinHeap_Array
from BinHeap_Ptr import Node, BinHeap_Ptr

app = Flask(__name__)
heapdict = {}  # A dictionary containing all heaps

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

    # Request LENGTH
    LENGTH = request.args.get('length', type=int)
    if LENGTH == None or LENGTH <= 0:
	return "Please enter a valid length!", 400
   
    # Request SEED
    SEED = request.args.get('seed', 100) # Use a default seed of 100
    (insert_time, remove_time) = BinHeap_Array().rand(LENGTH,SEED)
    return "The length is " + str(LENGTH) + ", and the seed is " + str(SEED) + '\n' \
	   "The insertion time is " + str(insert_time) + '\n' + "The popping time is " + str(remove_time) + '\n'

@app.route('/heap/time/pointer', methods=['GET'])
def heap_timeptr():
    
    # Request LENGTH
    LENGTH = request.args.get('length', type=int)
    if LENGTH == None or LENGTH <= 0:
        return "Please enter a valid length!", 400
    
    # Request SEED
    SEED = request.args.get('seed', 100) # Use a default seed of 100
    (insert_time, remove_time) = BinHeap_Ptr().rand(LENGTH,SEED)
    return "The length is " + str(LENGTH) + ", and the seed is " + str(SEED) + '\n' \
	   "The insertion time is " + str(insert_time) + '\n' + "The popping time is " + str(remove_time) + '\n'

if __name__ == "__main__":
    app.run(debug=True)                                          
