# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.

from collections import deque

numbers_16 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F')

numbers_10 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}


def sum_numb(a, b):
    x = a.copy()
    y = b.copy()
    if len(b) > len(a):
        x,y = y,x
    y.extendleft('0' * (len(x) - len(y)))
    result = deque()
    over = 0
    while len(x) != 0:
        x_num = numbers_10[x.pop()]
        y_num = numbers_10[y.pop()]
        result_num = x_num + y_num + over
        if result_num >= 16:
            over = 1
            result_num -= 16
        else:
            over = 0
        result.appendleft(numbers_16[result_num])
    if over == 1:
        result.appendleft('1')
    return result


a = deque(input('Введите первое шестнадцатеричное число: ').upper())
b = deque(input('Введите второе шестнадцатеричное число: ').upper())

c = sum_numb(a, b)
c_str = ''
for i in range(len(c)):
    c_str += c[i]
print(f'Сумма чисел равна {c_str} ')
