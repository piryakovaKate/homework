import itertools


def get_permutations(s, n):
    array = []
    arr = list(itertools.permutations(s, n))
    arr.sort()
    res = list(map(list, arr))
    #print(arr)
    #print(res)
    for i in range(len(res)):
        array.append(res[i][0] + res[i][1])
    print(array)

        


get_permutations("cat", 2) #["ac", "at", "ca", "ct", "ta", "tc"]

