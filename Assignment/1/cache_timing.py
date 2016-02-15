import numpy as np
from random import randint
import time
import sys
#print sys.getsizeof(int())

x=[randint(0,10000) for p in range(0,100000)]

def f(arr, passes):
    result = 0
    for p in range(passes):
        for x in arr[p::passes]:
            result += x * p
    return result

elapsed = []
for i in range(0,25000,500):
    start = time.clock()
    f(x,i)
    end = time.clock()
    elapsed.append(end - start)

start = time.clock()
f(x,16384)
end = time.clock()
worst = (end - start)


#print elapsed

npasses = range(0,25000,500)


import matplotlib.pyplot as plt
plt.rcParams['legend.numpoints'] = 1
normal, = plt.plot(npasses,elapsed,'r.',label="npass from 0 to 25000")
worstl, = plt.plot(16384,worst,'b*',label="worst case npass")
plt.legend(handles=[normal,worstl], loc=4)
plt.xlabel('npasses')
plt.ylabel('run time (in second)')
plt.savefig('cache_timing.jpg')
plt.show()

