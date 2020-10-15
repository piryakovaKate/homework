import sys

def swap(function):
    def the_wrapper(arr):
        for i in range(len(arr)//2):
            arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i]
        x = int(arr[1])
        y = int(arr[2])
        show = arr[3]
        x, y = y, x
        res = y / x
        if show:
            print(res)        
        
        return res


    return the_wrapper

@swap
def div(arr):
    x = int(arr[1])
    y = int(arr[2])
    show = arr[3]
    res = x / y
    if show:
        return res



arr = sys.argv
print(arr)
div(arr)

