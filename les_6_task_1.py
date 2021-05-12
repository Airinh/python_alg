import sys
import random

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = random.randint(100, 999)
print(a)

# вариант 1
a_str = str(a)
print('сумма цифр числа равна', int(a_str[0]) + int(a_str[1]) + int(a_str[2]))
print('произведение цифр числа равно', int(a_str[0]) * int(a_str[1]) * int(a_str[2]))
print(f'занято памяти по варианту 1: {sys.getsizeof(a) + sys.getsizeof(a_str)}\n')
# занято памяти: 80

# вариант 2
a_1 = a // 100
a_2 = a % 100 // 10
a_3 = a % 10
print('сумма цифр числа равна', a_1 + a_2 + a_3)
print('произведение цифр числа равно', a_1 * a_2 * a_3)
print(f'занято памяти по варианту 2: {sys.getsizeof(a) + sys.getsizeof(a_1) + sys.getsizeof(a_2) + sys.getsizeof(a_3)}\n')
# занято памяти: 112

# вариант 3
a_str = str(a)
summ = 0
mult = 1
for i in a_str:
    summ += int(i)
    mult *= int(i)
print('сумма цифр числа равна', summ)
print('произведение цифр числа равно', mult)
print(f'занято памяти по варианту 3: {sys.getsizeof(a) + sys.getsizeof(a_str) + sys.getsizeof(a_str[1]) + sys.getsizeof(summ) + sys.getsizeof(mult)}')
# занято памяти: 186

# Наибольший объем памяти занимает вариант 3, за счет переменных суммы и произведения и использования перебора в цикле.
# В первом, наиболее оптимальном, варианте всего 2 небольших по размеру переменных.
# Версия Python - 3.9,  64-bit
