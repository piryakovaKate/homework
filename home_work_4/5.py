def decorator_fun(function):
    def the_wrapper(argument):
        k = function(argument)

        if k == 0:
            return 'НЕТ'
        elif k > 10:
            return 'Очень много'
        else:
            return k

    return the_wrapper 

@decorator_fun
def simple_fun(array):
    k = 0
    
    for i in range(len(array)):
        if array[i]%2 == 0:
            k += 1
    return k


array = [int(x) for x in input().split()]
print(simple_fun(array))
