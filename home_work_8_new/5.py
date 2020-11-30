import itertools


def get_permutations(s, n):
    array = []
    for item in itertools.permutations(s, n):
        array.append(''.join(item))
    array.sort()
    print(array)

        


get_permutations("cat", 2)
