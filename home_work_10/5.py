import threading

def func1(v1 = [1,3], v2 = [2,4]):
    res = 0
    for (i, j) in zip(v1, v2):
        res += i*j
    print(res)

threads = threading.Thread(target = func1)

threads.start()



