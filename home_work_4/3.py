import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n', nargs='?')
    parser.add_argument('pos_arg1', nargs = '?')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()


    if namespace.n:
        number_fib = namespace.n

    if namespace.pos_arg1:
        number_fib = namespace.pos_arg1


prew = cur = 1
element = int(number_fib)
for n in range(int(element-2)):
    prew, cur = cur, prew + cur
print(str(cur))
