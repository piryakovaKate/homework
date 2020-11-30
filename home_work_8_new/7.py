import itertools

def get_combinations_with_r(s, n):
    array =[]
    for item in itertools.combinations_with_replacement(s,n):
        array.append(''.join(item))
    array.sort()
    print(array)
    
    

get_combinations_with_r("cat", 2)
