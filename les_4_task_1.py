import timeit


# Посчитать четные и нечетные цифры введенного натурального числа.

def odd_even_1(x):
    x = x
    odd, even = 0, 0
    while x > 0:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
        x = x // 10
    return f"четных - {even}, нечетных - {odd}"


def odd_even_2(x):
    x = str(x)
    even, odd = 0, 0
    for i in x:
        if i in {'0', '2', '4', '6', '8'}:
            even += 1
        else:
            odd += 1
    return f"четных - {even}, нечетных - {odd}"


def odd_even_3(x, even_=0, odd_=0):
    if x == 0:
        return even_, odd_
    if x % 2 == 0:
        even_ += 1
    else:
        odd_ += 1
    x = x // 10
    return odd_even_3(x, even_, odd_)


print('Тест odd_even_1:')
print(timeit.timeit('odd_even_1(234)', number=10000, globals=globals()))  # 0.0085789
print(timeit.timeit('odd_even_1(65676576)', number=10000, globals=globals()))  # 0.013283499999999997
print(timeit.timeit('odd_even_1(345354321213416)', number=10000, globals=globals()))  # 0.024331599999999995

print('Тест odd_even_2:')
print(timeit.timeit('odd_even_2(234)', number=10000, globals=globals()))  # 0.009115200000000004
print(timeit.timeit('odd_even_2(65676576)', number=10000, globals=globals()))  # 0.011858099999999996
print(timeit.timeit('odd_even_2(345354321213416)', number=10000, globals=globals()))  # 0.0164073

print('Тест odd_even_3:')
print(timeit.timeit('odd_even_3(234)', number=10000, globals=globals()))  # 0.007456400000000002
print(timeit.timeit('odd_even_3(65676576)', number=10000, globals=globals()))  # 0.018155000000000004
print(timeit.timeit('odd_even_3(345354321213416)', number=10000, globals=globals()))  # 0.03586539999999999

# По результатам исследования выяснилось, что оптимальный вариант - второй,
# с использованием форматирования числа в строку.
# Для определения оптимального варианта потребовалось значительно увеличить диапазон значений х и число N,
# так как на меньших разница во времени практически не прослеживалась.
