import itertools

def get_combinations(s, n):
    array = []
    for i in range(1,n+1):
        for item in itertools.combinations(s, i):
            array.append(''.join(item))

    print(array)


get_combinations("cat", 2) 
