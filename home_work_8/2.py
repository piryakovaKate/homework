def fibonaci(n):
    a,b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a+b

arr = list(fibonaci(10))
for idx, elem in enumerate(arr, 1):
    print("{:2}: {:>7}".format(idx, elem))



