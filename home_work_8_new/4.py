import itertools


def get_cartesian_product(a, b):
    return list(itertools.product(a,b))

a = [ 1, 2]
b = [ 3, 4]
print(get_cartesian_product(a, b))
