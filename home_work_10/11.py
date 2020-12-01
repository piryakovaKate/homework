from multiprocessing import Pool
import random

def func1(x, y):
    global res
    res += x*y
    return res

res = 0
v1 = []
for i in range(10):
    v1.append(random.randint(1, 100))
v2 = []
for i in range(10):
    v2.append(random.randint(1, 100))

pool = Pool(processes=4)
results = [pool.apply(func1,args = (v1[i],v2[i])) for i in range(10)]
print(sum(results))



