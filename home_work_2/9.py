print('введите число')

try:
    a = int(input())
except ValueError:
    print('введено не число')
finally:
    print('Дошел до finally')
