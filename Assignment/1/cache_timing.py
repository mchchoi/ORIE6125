import numpy as np
from random import randint
import time
import sys
print sys.getsizeof(int())

x=[randint(0,10000) for p in range(0,100000)]

def f(arr, passes):
    result = 0
    for p in range(passes):
        for x in arr[p::passes]:
            result += x * p
    return result

elapsed = []
for i in range(0,30000,1000):
    start = time.clock()
    f(x,i)
    end = time.clock()
    elapsed.append(end - start)

print elapsed

import matplotlib.pyplot as plt
plt.plot(range(0,30000,1000),elapsed)
plt.show()
