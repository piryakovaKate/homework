import threading
import random 

def func1(x, y):
    global res
    res += x*y
    print(res)
res = 0
v1 = []
for i in range(10):
    v1.append(random.randint(1, 100))
v2 = []
for i in range(10):
    v2.append(random.randint(1, 100))


threads = [threading.Thread(target = func1, args = (v1[i],v2[i])) for i in range(10)]

for thread in threads:
    thread.start()



