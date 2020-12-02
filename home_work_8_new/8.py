from itertools import groupby
from itertools import zip_longest


def compress_string(s):
    p = []
    q = []
    for k, g in groupby(s):
        p.append(len(list(g)))
        q.append(int(k))
    print(list(zip_longest(p,q)))
    

compress_string('1222311')
