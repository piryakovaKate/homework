print('введите два числа')
a = int(input())
b = int(input())

try:
    k = a / b
except ZeroDivisionError:
    k = 'Делим на ноль'
print(k)
