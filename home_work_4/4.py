import argparse


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-a', '--show-all', action = 'store_true')
    parser.add_argument ('-f', '--file', nargs = '?')
    parser.add_argument ('pos_arg1')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    print (namespace)



if namespace.pos_arg1:  
    n = int(namespace.pos_arg1)
    arr = []
    array = [0]*n
    for k in range(2, 2000):
        if all(k % i != 0 for i in range(2, k)):
            arr.append(k)
    for i in range(n):
        array[i] = arr[i]
    print(array[n-1])

if namespace.show_all:
    n = int(namespace.pos_arg1)
    arr = []
    array = [0]*n
    for k in range(2, 2000):
        if all(k % i != 0 for i in range(2, k)):
            arr.append(k)
    for i in range(n):
        array[i] = arr[i]
    print(array)

if namespace.file:
    n = int(namespace.pos_arg1)
    arr = []
    array = [0]*n
    for k in range(2, 2000):
        if all(k % i != 0 for i in range(2, k)):
            arr.append(k)
    for i in range(n):
        array[i] = arr[i]
    f = namespace.file
    file = open(f,'w')
    res = str(array[n-1])
    file.write(res)
    file.close()


